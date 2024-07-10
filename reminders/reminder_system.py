class ReminderSystem:
    def __init__(self):
        self.reminders = []

    def set_reminder(self, reminder: str, time: str) -> None:
        # Sets a new reminder
        self.reminders.append((reminder, time))

    def get_reminders(self) -> list:
        # Returns a list of all reminders
        return self.reminders

    def get_reminder(self, reminder: str) -> str:
        # Returns the reminder with the given name
        for r in self.reminders:
            if r[0] == reminder:
                return r[1]
        return None

    def get_reminder_names(self) -> list:
        # Returns a list of all reminder names
        return [r[0] for r in self.reminders]

    def remove_reminder(self, reminder: str) -> None:
        # Removes the reminder with the given name
        self.reminders = [r for r in self.reminders if r[0] != reminder]
