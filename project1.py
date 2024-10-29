import json
from datetime import datetime


class Task:
    def __init__(self, description, due_date=None, priority='Medium'):
        self.description = description
        self.due_date = due_date
        self.priority = priority
        self.completed = False

    def to_dict(self):
        return {
            'description': self.description,
            'due_date': self.due_date,
            'priority': self.priority,
            'completed': self.completed
        }


class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, description, due_date=None, priority='Medium'):
        task = Task(description, due_date, priority)
        self.tasks.append(task)
        print(f"Task added: {description}")

    def view_tasks(self):
        for index, task in enumerate(self.tasks):
            status = "✓" if task.completed else "✗"
            due_date = task.due_date if task.due_date else "No due date"
            print(f"{index + 1}. [{status}] {task.description} (Due: {due_date}, Priority: {task.priority})")

    def update_task(self, index, description=None, due_date=None, priority=None):
        if 0 <= index < len(self.tasks):
            if description:
                self.tasks[index].description = description
            if due_date:
                self.tasks[index].due_date = due_date
            if priority:
                self.tasks[index].priority = priority
            print("Task updated.")
        else:
            print("Invalid task index.")

    def complete_task(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index].completed = True
            print("Task marked as completed.")
        else:
            print("Invalid task index.")

    def delete_task(self, index):
        if 0 <= index < len(self.tasks):
            removed_task = self.tasks.pop(index)
            print(f"Task removed: {removed_task.description}")
        else:
            print("Invalid task index.")

    def save_tasks(self, filename='tasks.json'):
        with open(filename, 'w') as f:
            json.dump([task.to_dict() for task in self.tasks], f)
        print(f"Tasks saved to {filename}.")

    def load_tasks(self, filename='tasks.json'):
        try:
            with open(filename, 'r') as f:
                tasks_data = json.load(f)
                self.tasks = [Task(**task) for task in tasks_data]
            print(f"Tasks loaded from {filename}.")
        except FileNotFoundError:
            print("No saved tasks found.")


def main():
    todo_list = TodoList()
    todo_list.load_tasks()

    while True:
        print("\nOptions:")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Update Task")
        print("4. Complete Task")
        print("5. Delete Task")
        print("6. Save Tasks")
        print("7. Load Tasks")
        print("8. Exit")

        choice = input("Select an option: ")

        if choice == '1':
            description = input("Task description: ")
            due_date = input("Due date (YYYY-MM-DD) or leave empty: ")
            priority = input("Priority (High, Medium, Low): ")
            todo_list.add_task(description, due_date if due_date else None, priority.capitalize())

        elif choice == '2':
            todo_list.view_tasks()

        elif choice == '3':
            index = int(input("Task index to update: ")) - 1
            description = input("New description (leave empty to keep current): ")
            due_date = input("New due date (leave empty to keep current): ")
            priority = input("New priority (leave empty to keep current): ")
            todo_list.update_task(index, description if description else None, due_date if due_date else None,
                                  priority if priority else None)

        elif choice == '4':
            index = int(input("Task index to complete: ")) - 1
            todo_list.complete_task(index)

        elif choice == '5':
            index = int(input("Task index to delete: ")) - 1
            todo_list.delete_task(index)

        elif choice == '6':
            todo_list.save_tasks()

        elif choice == '7':
            todo_list.load_tasks()

        elif choice == '8':
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
