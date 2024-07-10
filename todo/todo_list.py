class TodoList:
    def __init__(self):
        self.tasks = []

    def set_todo(self, todo: str) -> None:
        # Sets a new todo
        self.tasks.append((todo, None))

    def get_todos(self) -> list:
        # Returns a list of all todos
        return [r[0] for r in self.tasks if r[1] is None]

    def get_todo_names(self) -> list:
        # Returns a list of all todo names
        return [r[0] for r in self.tasks if r[1] is None]

    def get_todo(self, todo: str) -> str:
        # Returns the todo with the given name
        for r in self.tasks:
            if r[0] == todo and r[1] is None:
                return r[0]
        return None

    def remove_todo(self, todo: str) -> None:
        # Removes the todo with the given name
        self.tasks = [r for r in self.tasks if r[0] != todo or r[1] is not None]
