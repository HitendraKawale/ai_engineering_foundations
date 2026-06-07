import json
import os

FILE_NAME = "todo.json"


def load_todo():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as f:
            return json.load(f)

    else:
        return []


def save_todos(todos):
    with open(FILE_NAME, "w") as f:
        json.dump(todos, f, indent=2)


def add_todo(task):
    todos = load_todo()
    todos.append({"task": task, "done": False})

    save_todos(todos)


def view_todos():
    todos = load_todo()

    for index, todo in enumerate(todos, start=1):
        checkbox = "[]" if not todo["done"] else "[x]"
        print(f"{index}. task: {checkbox}, task : {todo['task']}")
