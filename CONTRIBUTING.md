# Contributing to Hey Assistant

Thanks for your interest in contributing! This guide covers the plugin architecture and contribution workflow.

---

## Table of Contents

- [Getting Started](#getting-started)
- [Plugin Architecture](#plugin-architecture)
- [Building a New Plugin](#building-a-new-plugin)
- [Submitting a Pull Request](#submitting-a-pull-request)
- [Code Style](#code-style)

---

## Getting Started

1. Fork the repository on GitHub
2. Clone your fork:
   ```bash
   git clone https://github.com/<your-username>/virtual_assitant.git
   cd virtual_assitant
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   python -m spacy download en_core_web_sm
   ```
4. Copy and configure environment variables:
   ```bash
   cp example.env .env
   # Edit .env with your API keys
   ```
5. Create a feature branch:
   ```bash
   git checkout -b feature/my-new-plugin
   ```

---

## Plugin Architecture

Each feature is a self-contained module in its own directory. The `CommandProcessor` routes spoken commands to the appropriate plugin based on keyword matching.

```
virtual_assitant/
├── commands/
│   └── command_processor.py   ← Add your elif branch here
├── your_plugin/
│   ├── __init__.py            ← Export your class
│   └── your_plugin.py         ← Your plugin logic
└── main.py                    ← Wire up your plugin here
```

---

## Building a New Plugin

### Step 1 — Create your module directory

```bash
mkdir my_plugin
```

### Step 2 — Write your plugin class (`my_plugin/my_plugin.py`)

```python
class MyPlugin:
    def handle(self, command: str) -> str:
        """
        Parse the command string and return a response to be spoken.
        Raise an exception or return an empty string if the command can't be handled.
        """
        return f"You said: {command}"
```

Keep plugin classes stateless where possible. If you need state (e.g. a to-do list stored on disk), encapsulate it fully inside the class.

### Step 3 — Export from `__init__.py` (`my_plugin/__init__.py`)

```python
from .my_plugin import MyPlugin
```

### Step 4 — Wire into `main.py`

```python
from my_plugin import MyPlugin

# inside main():
my_plugin = MyPlugin()

cp = CommandProcessor(
    ...,
    my_plugin=my_plugin,
)
```

### Step 5 — Add a constructor parameter and elif branch in `commands/command_processor.py`

```python
class CommandProcessor:
    def __init__(self, ..., my_plugin):
        ...
        self.my_plugin = my_plugin

    def process_command(self, command):
        ...
        elif "trigger phrase" in command:
            result = self.my_plugin.handle(command)
            self.read(result)
```

### Step 6 — Add tests

Place tests alongside your module or in a top-level `tests/` directory:

```
my_plugin/
├── __init__.py
├── my_plugin.py
└── test_my_plugin.py
```

Run existing tests before opening a PR:

```bash
python -m pytest
```

---

## Submitting a Pull Request

1. Ensure your branch is up to date with `main`
2. Verify tests pass: `python -m pytest`
3. Open a pull request against `main` with a clear description of what your plugin does and example voice commands that trigger it

---

## Code Style

- Follow [PEP 8](https://peps.python.org/pep-0008/)
- Use type hints where practical
- Keep plugin classes focused on a single responsibility
- Prefer returning strings from plugin methods so `CommandProcessor` controls all TTS output
