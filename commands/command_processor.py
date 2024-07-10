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
                    tts(r[0])

        elif "reminder" in command:
            self.reminder_system.set_reminder(command)
        elif "todo" in command:
            self.todo_list.add_task(command)
        elif "weather" in command:
            self.weather_update.get_weather(command)
        elif "joke" in command:
            self.jokes.tell_joke()
        elif "calculate" in command:
            self.math_operations.calculate(command)
        elif "news" in command:
            self.news_update.get_news(command)
        elif "stop" or "exit" in command:
            tts("Goodbye!")
            exit(1)
