import pickle
import os

class Task:
    def __init__(self, description, due_date, priority, completed=False):
        self.description = description
        self.due_date = due_date
        self.priority = priority
        self.completed = completed

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def list_tasks(self):
        for i, task in enumerate(self.tasks):
            print(f"{i + 1}. Description: {task.description}")
            print(f"   Due Date: {task.due_date}")
            print(f"   Priority: {task.priority}")
            print(f"   Status: {'Completed' if task.completed else 'Incomplete'}")
            print("")

    def update_task(self, task_index, updated_task):
        if task_index < 0 or task_index >= len(self.tasks):
            print("Invalid task index.")
            return
        self.tasks[task_index] = updated_task

    def delete_task(self, task_index):
        if task_index < 0 or task_index >= len(self.tasks):
            print("Invalid task index.")
            return
        del self.tasks[task_index]

    def save_to_file(self, filename):
        with open(filename, 'wb') as file:
            pickle.dump(self.tasks, file)

    def load_from_file(self, filename):
        if os.path.exists(filename):
            with open(filename, 'rb') as file:
                self.tasks = pickle.load(file)

def main():
    to_do_list = ToDoList()
    filename = "todolist.pkl"

    if os.path.exists(filename):
        to_do_list.load_from_file(filename)

    while True:
        print("To-Do List Application")
        print("1. Add Task")
        print("2. List Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Save and Quit")
        choice = input("Enter your choice: ")

        if choice == "1":
            description = input("Task Description: ")
            due_date = input("Due Date: ")
            priority = input("Priority: ")
            task = Task(description, due_date, priority)
            to_do_list.add_task(task)

        elif choice == "2":
            print("\nList of Tasks:")
            to_do_list.list_tasks()

        elif choice == "3":
            task_index = int(input("Enter the task index to update: ")) - 1
            description = input("Updated Task Description: ")
            due_date = input("Updated Due Date: ")
            priority = input("Updated Priority: ")
            completed = input("Is it completed? (y/n): ").lower() == 'y'
            updated_task = Task(description, due_date, priority, completed)
            to_do_list.update_task(task_index, updated_task)

        elif choice == "4":
            task_index = int(input("Enter the task index to delete: ")) - 1
            to_do_list.delete_task(task_index)

        elif choice == "5":
            to_do_list.save_to_file(filename)
            break

if __name__ == "__main__":
    main()
