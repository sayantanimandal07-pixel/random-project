import json
import os

FILE_NAME = "tasks.json"


# Load tasks from file
def load_tasks():
    if os.path.exists(FILE_NAME):
        try:
            with open(FILE_NAME, "r") as file:
                return json.load(file)
        except json.JSONDecodeError:
            return []
    return []


# Save tasks to file
def save_tasks(tasks):
    with open(FILE_NAME, "w") as file:
        json.dump(tasks, file, indent=4)


# Display all tasks
def view_tasks(tasks):
    if not tasks:
        print("\nNo tasks available!")
        return

    print("\n------ YOUR TASKS ------")

    for i, task in enumerate(tasks, start=1):
        status = "✓ Completed" if task["completed"] else "Pending"
        print(f"{i}. {task['name']} [{status}]")


# Add a new task
def add_task(tasks):
    task_name = input("\nEnter task: ")

    if task_name.strip():
        tasks.append({
            "name": task_name,
            "completed": False
        })

        save_tasks(tasks)
        print("Task added successfully!")
    else:
        print("Task cannot be empty!")


# Mark task as completed
def complete_task(tasks):
    view_tasks(tasks)

    if not tasks:
        return

    try:
        task_number = int(input("\nEnter task number to mark as completed: "))

        if 1 <= task_number <= len(tasks):
            tasks[task_number - 1]["completed"] = True
            save_tasks(tasks)
            print("Task marked as completed!")
        else:
            print("Invalid task number!")

    except ValueError:
        print("Please enter a valid number!")


# Delete a task
def delete_task(tasks):
    view_tasks(tasks)

    if not tasks:
        return

    try:
        task_number = int(input("\nEnter task number to delete: "))

        if 1 <= task_number <= len(tasks):
            deleted_task = tasks.pop(task_number - 1)
            save_tasks(tasks)

            print(f"Task '{deleted_task['name']}' deleted successfully!")
        else:
            print("Invalid task number!")

    except ValueError:
        print("Please enter a valid number!")


# Main program
def main():
    tasks = load_tasks()

    while True:
        print("\n==============================")
        print("       PYTHON TO-DO LIST")
        print("==============================")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Mark Task as Completed")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("\nEnter your choice (1-5): ")

        if choice == "1":
            view_tasks(tasks)

        elif choice == "2":
            add_task(tasks)

        elif choice == "3":
            complete_task(tasks)

        elif choice == "4":
            delete_task(tasks)

        elif choice == "5":
            print("\nThank you for using To-Do List App!")
            break

        else:
            print("\nInvalid choice! Please try again.")


if __name__ == "__main__":
    main()