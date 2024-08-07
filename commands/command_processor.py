import json

import spacy

from tts import tts


class CommandProcessor:
    def __init__(
        self,
        voice_recognition,
        web_search,
        reminder_system,
        todo_list,
        weather_update,
        jokes,
        math_operations,
        news_update,
    ):
        self.voice_recognition = voice_recognition
        self.web_search = web_search
        self.reminder_system = reminder_system
        self.todo_list = todo_list
        self.weather_update = weather_update
        self.jokes = jokes
        self.math_operations = math_operations
        self.news_update = news_update

        self.nlp = spacy.load("en_core_web_sm")  # Load the English model

        json_file = "places.json"  # Path to the JSON file containing known locations

        # Initialize an empty dictionary to store the loaded data
        self.known_locations = {}

        # Load data from JSON file into Python dictionary
        with open(json_file, "r", encoding="utf-8") as f:
            self.known_locations = json.load(f)

    def extract_locations(self, text):
        # Process the text with spaCy
        doc = self.nlp(text)

        # Extract known locations
        for token in doc:
            if token.text.lower() in self.known_locations:
                print("Known location found:", token.text.lower())
                # return location and longitude and latitude from the JSON file
                print(
                    "this: ",
                    [token.text.lower(), self.known_locations[token.text.lower()]],
                )
                print(
                    "weather",
                    token.text.lower(),
                    self.known_locations[token.text.lower()].get("latitude"),
                    self.known_locations[token.text.lower()].get("longitude"),
                    "end",
                )
                # return the location, latitude and longitude individually
                return (
                    token.text.lower(),
                    self.known_locations[token.text.lower()].get("latitude"),
                    self.known_locations[token.text.lower()].get("longitude"),
                )

    def process_command(self, command):
        if "search" in command:
            print("Searching...")
            result = self.web_search.verify_query(command)
            # format as website name then content
            results = []
            for r in result:
                # print the title and the content
                results.append([r["title"], r["body"]])

            # use tts to read the results
            if results:
                for r in results:
                    self.read(r[0])

        elif "reminder" in command:
            self.reminder_system.set_reminder(command)
        elif "todo" in command:
            self.todo_list.add_task(command)
        elif "weather" in command:
            # Extract the location from the command
            locations, latitudes, longitudes = self.extract_locations(command)
            if locations:
                self.weather_update.get_weather(locations, latitudes, longitudes)

        elif "joke" in command:
            joke = self.jokes.get_joke()
            # split into setup and delivery or just return the joke
            if "..." in joke:
                setup, delivery = joke.split("... ")
                self.read(setup)
                self.read(delivery)
            else:
                self.read(joke)
        elif "calculate" in command:
            self.math_operations.calculate(command)

        elif "news" in command:
            """
            if "from" not in command:
                # get date in 2024-07-13 format
                date = datetime.now().strftime("%Y-%m-%d")
                # current - 3months
                to_date = datetime.now() - timedelta(days=90)
                to_date = to_date.strftime("%Y-%m-%d")
                news = self.news_update.fetch_news(command, from_date=date)
            else:
                print("date found")
            """

            news = self.news_update.fetch_news(command)
            news = self.news_update.parse_news(news)
            # read the news
            for n in news:
                self.read(n["publishedAt"])
                self.read(n["title"])
                self.read(n["content"])

        """
        elif "stop" or "exit" in command:
            tts("Goodbye!")
            exit(1)
        """

    def read(self, data: str):
        # read in new process so that it can be stopped by keyboard interrupt
        try:
            tts(data)
        except KeyboardInterrupt:
            print("Interrupted")
            exit(1)
        except Exception as e:
            print("Error:", e)
            tts("Sorry, I couldn't read that.")
            exit(1)
