# Flowcharts

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
