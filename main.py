import os

from dotenv import load_dotenv

from commands import CommandProcessor
from jokes import Jokes
from math_operations import MathOperations
from news import NewsUpdate
from reminders import ReminderSystem
from todo import TodoList
from voice_recognition import VoiceRecognition
from weather import WeatherUpdate
from web import WebSearch


def main():
    vr = VoiceRecognition(wake_word="Hey Assistant")

    # Load environment variables
    load_dotenv()
    WEATHER_API_KEY = os.getenv("WEATHER_API_KEY")

    web_search = WebSearch(api_key="YOUR_API_KEY")
    reminder_system = ReminderSystem()
    todo_list = TodoList()
    weather_update = WeatherUpdate(WEATHER_API_KEY)
    jokes = Jokes(api_key="YOUR_API_KEY")
    math_operations = MathOperations()
    news_update = NewsUpdate(api_key="YOUR_API_KEY")

    cp = CommandProcessor(
        voice_recognition=vr,
        web_search=web_search,
        reminder_system=reminder_system,
        todo_list=todo_list,
        weather_update=weather_update,
        jokes=jokes,
        math_operations=math_operations,
        news_update=news_update,
    )

    while True:
        print("Say 'Hey Assistant' to start...")
        command = vr.listen()
        if vr.detect_wake_word(command):
            print("Wake word detected, listening for command...")
            command = vr.listen()
            cp.process_command(command)


if __name__ == "__main__":
    main()
