from todo_list import TodoList


def test_set_todo():
    todo_list = TodoList()
    todo_list.set_todo("Buy groceries")
    assert len(todo_list.tasks) == 1
    assert todo_list.tasks[0][0] == "Buy groceries"
    assert todo_list.tasks[0][1] is None


def test_get_todos():
    todo_list = TodoList()
    todo_list.set_todo("Buy groceries")
    todo_list.set_todo("Do laundry")
    todos = todo_list.get_todos()
    assert len(todos) == 2
    assert "Buy groceries" in todos
    assert "Do laundry" in todos


def test_get_todo_names():
    todo_list = TodoList()
    todo_list.set_todo("Buy groceries")
    todo_list.set_todo("Do laundry")
    todo_names = todo_list.get_todo_names()
    assert len(todo_names) == 2
    assert "Buy groceries" in todo_names
    assert "Do laundry" in todo_names


def test_get_todo():
    todo_list = TodoList()
    todo_list.set_todo("Buy groceries")
    todo_list.set_todo("Do laundry")
    assert todo_list.get_todo("Buy groceries") == "Buy groceries"
    assert todo_list.get_todo("Do laundry") == "Do laundry"
    assert todo_list.get_todo("Clean the house") is None


def test_remove_todo():
    todo_list = TodoList()
    todo_list.set_todo("Buy groceries")
    todo_list.set_todo("Do laundry")
    todo_list.remove_todo("Buy groceries")
    assert len(todo_list.tasks) == 1
    assert todo_list.tasks[0][0] == "Do laundry"
    assert todo_list.tasks[0][1] is None
    todo_list.remove_todo(
        "Clean the house"
    )  # Removing non-existent todo should not raise an error


# Run all the test cases
test_set_todo()
test_get_todos()
test_get_todo_names()
test_get_todo()
test_remove_todo()
print("All test cases passed!")
