import json
import os
from datetime import datetime

class TodoApp:
    def __init__(self, filename="todos.json"):
        self.filename = filename
        self.todos = []
        self.load_todos()

    def load_todos(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as f:
                self.todos = json.load(f)

    def save_todos(self):
        with open(self.filename, 'w') as f:
            json.dump(self.todos, f, indent=2)

    def add_todo(self, task):
        todo = {
            'id': len(self.todos) + 1,
            'task': task,
            'completed': False,
            'created_at': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        self.todos.append(todo)
        self.save_todos()
        print(f"Added: {task}")

    def list_todos(self):
        if not self.todos:
            print("No todos found!")
            return
        for todo in self.todos:
            status = "✓" if todo['completed'] else " "
            print(f"[{status}] {todo['id']}. {todo['task']}")

    def complete_todo(self, id):
        for todo in self.todos:
            if todo['id'] == id:
                todo['completed'] = True
                self.save_todos()
                print(f"Marked todo #{id} as complete")
                return
        print(f"Todo #{id} not found")

    def delete_todo(self, id):
        for todo in list(self.todos):
            if todo['id'] == id:
                self.todos.remove(todo)
                 Reassign IDs for consistency
                for idx, t in enumerate(self.todos, start=1):
                    t['id'] = idx
                self.save_todos()
                print(f"Deleted todo #{id}")
                return
        print(f"Todo #{id} not found")

def main():
    app = TodoApp()
    while True:
        print("\n1. Add todo")
        print("2. List todos")
        print("3. Complete todo")
        print("4. Delete todo")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ").strip()
        if choice == '1':
            task = input("Enter todo: ").strip()
            if task:
                app.add_todo(task)
            else:
                print("Task cannot be empty.")
        elif choice == '2':
            app.list_todos()
        elif choice == '3':
            try:
                id = int(input("Enter todo ID to complete: "))
                app.complete_todo(id)
            except ValueError:
                print("Please enter a valid number.")
        elif choice == '4':
            try:
                id = int(input("Enter todo ID to delete: "))
                app.delete_todo(id)
            except ValueError:
                print("Please enter a valid number.")
        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Enter a number 1‑5.")

if __name__ == "__main__":
    main()
