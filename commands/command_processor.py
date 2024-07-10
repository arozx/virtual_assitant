class CommandProcessor:
    def __init__(
        self,
        voice_recognition,
        text_to_speech,
        web_search,
        reminder_system,
        todo_list,
        weather_update,
        jokes,
        math_operations,
        news_update,
        email_manager,
    ):
        self.voice_recognition = voice_recognition
        self.text_to_speech = text_to_speech
        self.web_search = web_search
        self.reminder_system = reminder_system
        self.todo_list = todo_list
        self.weather_update = weather_update
        self.jokes = jokes
        self.math_operations = math_operations
        self.news_update = news_update
        self.email_manager = email_manager

    def process_command(self, command):
        if "search" in command:
            self.web_search.search(command)
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
        elif "email" in command:
            self.email_manager.send_email(command)
        elif "exit" in command:
            self.text_to_speech.speak("Goodbye!")
            exit()
        else:
            self.text_to_speech.speak("Sorry, I didn't understand that command.")
