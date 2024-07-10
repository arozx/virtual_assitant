from reminders import ReminderSystem


def test_set_reminder():
    reminder_system = ReminderSystem()
    reminder_system.set_reminder("Meeting", "2022-01-01 10:00 AM")
    assert len(reminder_system.get_reminders()) == 1


def test_get_reminder():
    reminder_system = ReminderSystem()
    reminder_system.set_reminder("Meeting", "2022-01-01 10:00 AM")
    assert reminder_system.get_reminder("Meeting") == "2022-01-01 10:00 AM"


def test_get_reminder_names():
    reminder_system = ReminderSystem()
    reminder_system.set_reminder("Meeting", "2022-01-01 10:00 AM")
    reminder_system.set_reminder("Appointment", "2022-01-02 02:00 PM")
    assert reminder_system.get_reminder_names() == ["Meeting", "Appointment"]


def test_remove_reminder():
    reminder_system = ReminderSystem()
    reminder_system.set_reminder("Meeting", "2022-01-01 10:00 AM")
    reminder_system.set_reminder("Appointment", "2022-01-02 02:00 PM")
    reminder_system.remove_reminder("Meeting")
    assert len(reminder_system.get_reminders()) == 1
    assert reminder_system.get_reminder("Meeting") is None


def test_reminder_system():
    reminder_system = ReminderSystem()
    reminder_system.set_reminder("Meeting", "2022-01-01 10:00 AM")
    reminder_system.set_reminder("Appointment", "2022-01-02 02:00 PM")
    assert len(reminder_system.get_reminders()) == 2
    assert reminder_system.get_reminder("Meeting") == "2022-01-01 10:00 AM"
    assert reminder_system.get_reminder("Appointment") == "2022-01-02 02:00 PM"
    assert reminder_system.get_reminder_names() == ["Meeting", "Appointment"]
    reminder_system.remove_reminder("Meeting")
    assert len(reminder_system.get_reminders()) == 1
    assert reminder_system.get_reminder("Meeting") is None


test_set_reminder()
test_get_reminder()
test_get_reminder_names()
test_remove_reminder()
test_reminder_system()
print("All test cases passed!")
