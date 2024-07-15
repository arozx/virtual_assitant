# What is this project?

An opensouce voice assistant that can perform various tasks like setting reminders, searching the web, getting weather, etc. It is built using Python and uses the Vosk library for voice recognition and the pyttsx3 library for text-to-speech conversion.

## Features

- Voice recognition
- Text-to-speech conversion
- Web search
- Reminder system
- Todo list
- Weather updates
- Jokes
- Math operations (__Coming soon__)
- News updates

## How to use

1. Clone the repository
2. Install the required libraries using `pip install -r requirements.txt`
3. Install the Vosk model from [here](https://alphacephei.com/vosk/models)
4. Extract the model and place it in the `models` folder
5. Create a .env file (e.g. example.env) in the root directory and add the following variables:
    - `WEATHER_API_KEY` - API key for the OpenWeatherMap API
    - `NEWS_API_KEY` - API key for the News API
6. Download the GeoNames data for places from [here](https://download.geonames.org/export/dump/). Then tun `extract.py` with the downloaded file as an argument to extract the data.
7. Run the `main.py` file

## VoiceRecognition & TTS

```mermaid
graph TD
    A[VoiceRecognition]
    B[TextToSpeech]
    A --> |Listens for command| B
    B --> |Converts text to speech| A

```

## CommandProcessor

```mermaid
flowchart TD
    A[CommandProcessor]
    B[VoiceRecognition]
    C[TextToSpeech]
    D[WebSearch]
    E[ReminderSystem]
    F[TodoList]
    G[WeatherUpdate]
    H[Jokes]
    I[MathOperations]
    J[NewsUpdate]
    K[EmailManager]

    A --> B
    A --> C
    A --> D
    A --> E
    A --> F
    A --> G
    A --> H
    A --> I
    A --> J
    A --> K
```

## WebSearch

```mermaid
graph TD
    A[WebSearch]
    B[CommandProcessor]
    A --> |Performs web search| B
    B --> |Processes command| A
```

## ReminderSystem

```mermaid
graph TD
    A[ReminderSystem]
    B[CommandProcessor]
    A --> |Sets or gets reminders| B
    B --> |Processes command| A
```

## TodoList

```mermaid
graph TD
    A[TodoList]
    B[CommandProcessor]
    A --> |Adds or removes tasks| B
    B --> |Processes command| A
```

## WeatherUpdate

```mermaid
graph TD
    A[WeatherUpdate]
    B[CommandProcessor]
    A --> |Gets weather updates| B
    B --> |Processes command| A
```

## Jokes

```mermaid
graph TD
    A[Jokes]
    B[CommandProcessor]
    A --> |Gets jokes| B
    B --> |Processes command| A
```

## MathOperations

```mermaid
graph TD
    A[MathOperations]
    B[CommandProcessor]
    A --> |Performs math operations| B
    B --> |Processes command| A
```

## NewsUpdate

```mermaid
graph TD
    A[NewsUpdate]
    B[CommandProcessor]
    A --> |Gets news updates| B
    B --> |Processes command| A
```

## EmailManager

```mermaid
graph TD
    A[EmailManager]
    B[CommandProcessor]
    A --> |Manages emails| B
    B --> |Processes command| A
```

## Main

```mermaid
graph TD
    A[Main]
    B[VoiceRecognition]
    C[TextToSpeech]
    D[CommandProcessor]
    E[WebSearch]
    F[ReminderSystem]
    G[TodoList]
    H[WeatherUpdate]
    I[Jokes]
    J[MathOperations]
    K[NewsUpdate]
    L[EmailManager]

    A --> B
    A --> C
    A --> D
    D --> E
    D --> F
    D --> G
    D --> H
    D --> I
    D --> J
    D --> K
    D --> L
```
