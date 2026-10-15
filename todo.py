import json
import os


# Task Class
class Task:

    def __init__(self, Task_Id, Title, Status="Pending"):
        self.Id = Task_Id
        self.Title = Title
        self.Status = Status

    def to_dict(self):
        return {
            "Id": self.Id,
            "Title": self.Title,
            "Status": self.Status
        }


# JSON File Name
FILE_NAME = "task.json"


# Load Tasks from JSON File
def load_task():

    if os.path.exists(FILE_NAME):

        with open(FILE_NAME, "r") as file:
            return json.load(file)

    return []


# Save Tasks to JSON File
def save_task(tasks):

    with open(FILE_NAME, "w") as file:
        json.dump(tasks, file, indent=4)


# Add a New Task
def add_tasks(tasks):

    title = input("Enter Task: ")

    if title.strip() == "":
        print("Task cannot be empty!")
        return

    elif tasks:
        Id = max(task["Id"] for task in tasks) + 1

    else:
        Id = 1

    task = Task(Id, title)

    tasks.append(task.to_dict())

    save_task(tasks)

    print("Task added successfully!")


# View All Tasks
def view_tasks(tasks):

    if not tasks:
        print("No tasks available!")
        return

    print("\n========== TASK LIST ==========")

    for task in tasks:

        print(
            f"ID: {task['Id']} | "
            f"Task: {task['Title']} | "
            f"Status: {task['Status']}"
        )

    print("===============================")


# Mark Task as Completed
def mark_task(tasks):

    if not tasks:
        print("No tasks available!")
        return

    try:
        task_id = int(input("Enter Task ID: "))

    except ValueError:
        print("Please enter a valid number!")
        return

    for task in tasks:

        if task["Id"] == task_id:

            task["Status"] = "Completed"

            save_task(tasks)

            print("Task marked as completed!")

            return

    print("Task ID not found!")


# Delete Task
def delete_task(tasks):

    if not tasks:
        print("No tasks available!")
        return

    try:
        task_id = int(input("Enter Task ID: "))

    except ValueError:
        print("Please enter a valid number!")
        return

    for task in tasks:

        if task["Id"] == task_id:

            tasks.remove(task)

            save_task(tasks)

            print("Task deleted successfully!")

            return

    print("Task ID not found!")


# Main Program

tasks = load_task()


while True:

    print("\n========== TO-DO LIST ==========")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Completed")
    print("4. Delete Task")
    print("5. Exit")
    print("================================")

    choice = input("Enter your choice: ")


    # Add Task
    if choice == "1":

        add_tasks(tasks)


    # View Tasks
    elif choice == "2":

        view_tasks(tasks)


    # Mark Task
    elif choice == "3":

        mark_task(tasks)


    # Delete Task
    elif choice == "4":

        delete_task(tasks)


    # Exit
    elif choice == "5":

        print("Thank you for using To-Do List App!")

        break


    # Invalid Choice
    else:

        print("Invalid choice! Please enter 1 to 5.")



        
        