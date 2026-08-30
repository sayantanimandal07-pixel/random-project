import json
import os
from datetime import datetime


FILE_NAME = "tasks.json"


# ==========================================================
# FILE HANDLING
# ==========================================================

def load_tasks():
    """Load tasks from JSON file."""

    if not os.path.exists(FILE_NAME):
        return []

    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)

    except (json.JSONDecodeError, FileNotFoundError):
        return []


def save_tasks(tasks):
    """Save tasks to JSON file."""

    with open(FILE_NAME, "w") as file:
        json.dump(tasks, file, indent=4)


# ==========================================================
# TASK ID
# ==========================================================

def get_next_id(tasks):
    """Generate the next task ID."""

    if not tasks:
        return 1

    return max(task["id"] for task in tasks) + 1


# ==========================================================
# PRIORITY
# ==========================================================

def choose_priority():

    while True:

        print("\nPriority")
        print("1. 🔴 High")
        print("2. 🟡 Medium")
        print("3. 🟢 Low")

        choice = input("Choose priority: ").strip()

        if choice == "1":
            return "High"

        elif choice == "2":
            return "Medium"

        elif choice == "3":
            return "Low"

        else:
            print("❌ Invalid choice. Please try again.")


# ==========================================================
# DATE
# ==========================================================

def get_due_date():

    while True:

        date = input(
            "\nEnter due date (DD-MM-YYYY)"
            "\nPress Enter to skip: "
        ).strip()

        if date == "":
            return None

        try:
            datetime.strptime(date, "%d-%m-%Y")
            return date

        except ValueError:
            print("❌ Invalid date.")
            print("Please use DD-MM-YYYY format.")


# ==========================================================
# OVERDUE CHECK
# ==========================================================

def is_overdue(task):

    if task["completed"]:
        return False

    if task["due_date"] is None:
        return False

    due_date = datetime.strptime(
        task["due_date"],
        "%d-%m-%Y"
    ).date()

    return due_date < datetime.now().date()


# ==========================================================
# STATUS
# ==========================================================

def get_status(task):

    if task["completed"]:
        return "✅ Completed"

    if is_overdue(task):
        return "⚠️ Overdue"

    return "⏳ Pending"


# ==========================================================
# DISPLAY SINGLE TASK
# ==========================================================

def display_task(task):

    print("\n" + "-" * 50)

    print(f"ID       : {task['id']}")
    print(f"Task     : {task['name']}")
    print(f"Category : {task['category']}")
    print(f"Priority : {task['priority']}")

    if task["due_date"]:
        print(f"Due Date : {task['due_date']}")
    else:
        print("Due Date : No deadline")

    print(f"Status   : {get_status(task)}")

    print("-" * 50)


# ==========================================================
# VIEW TASKS
# ==========================================================

def view_tasks(tasks):

    if not tasks:
        print("\n📭 No tasks found.")
        return

    print("\n" + "=" * 55)
    print("                    ALL TASKS")
    print("=" * 55)

    for task in tasks:
        display_task(task)


# ==========================================================
# ADD TASK
# ==========================================================

def add_task(tasks):

    print("\n" + "=" * 55)
    print("                    ADD TASK")
    print("=" * 55)

    name = input("Enter task name: ").strip()

    if not name:
        print("❌ Task name cannot be empty.")
        return

    category = input(
        "Enter category (Study/Work/Personal/etc.): "
    ).strip()

    if not category:
        category = "General"

    priority = choose_priority()

    due_date = get_due_date()

    new_task = {

        "id": get_next_id(tasks),

        "name": name,

        "category": category,

        "priority": priority,

        "due_date": due_date,

        "completed": False

    }

    tasks.append(new_task)

    save_tasks(tasks)

    print("\n✅ Task added successfully!")


# ==========================================================
# EDIT TASK
# ==========================================================

def edit_task(tasks):

    if not tasks:
        print("\n📭 No tasks available.")
        return

    view_tasks(tasks)

    try:
        task_id = int(
            input("\nEnter Task ID to edit: ")
        )

    except ValueError:
        print("❌ Please enter a valid ID.")
        return

    for task in tasks:

        if task["id"] == task_id:

            print("\nPress Enter to keep the current value.")

            # Task name
            new_name = input(
                f"Task name [{task['name']}]: "
            ).strip()

            if new_name:
                task["name"] = new_name

            # Category
            new_category = input(
                f"Category [{task['category']}]: "
            ).strip()

            if new_category:
                task["category"] = new_category

            # Priority
            change_priority = input(
                f"Change priority? Current: "
                f"{task['priority']} (y/n): "
            ).lower()

            if change_priority == "y":
                task["priority"] = choose_priority()

            # Due date
            change_date = input(
                "Change due date? (y/n): "
            ).lower()

            if change_date == "y":
                task["due_date"] = get_due_date()

            save_tasks(tasks)

            print("\n✅ Task updated successfully!")

            return

    print("❌ Task ID not found.")


# ==========================================================
# MARK COMPLETE / PENDING
# ==========================================================

def toggle_task(tasks):

    if not tasks:
        print("\n📭 No tasks available.")
        return

    view_tasks(tasks)

    try:
        task_id = int(
            input("\nEnter Task ID: ")
        )

    except ValueError:
        print("❌ Please enter a valid ID.")
        return

    for task in tasks:

        if task["id"] == task_id:

            task["completed"] = not task["completed"]

            save_tasks(tasks)

            if task["completed"]:
                print("\n🎉 Task marked as completed!")
            else:
                print("\n🔄 Task marked as pending!")

            return

    print("❌ Task ID not found.")


# ==========================================================
# DELETE TASK
# ==========================================================

def delete_task(tasks):

    if not tasks:
        print("\n📭 No tasks available.")
        return

    view_tasks(tasks)

    try:
        task_id = int(
            input("\nEnter Task ID to delete: ")
        )

    except ValueError:
        print("❌ Please enter a valid ID.")
        return

    for task in tasks:

        if task["id"] == task_id:

            confirm = input(
                f"Delete '{task['name']}'? (y/n): "
            ).lower()

            if confirm == "y":

                tasks.remove(task)

                save_tasks(tasks)

                print("\n🗑️ Task deleted successfully!")

            else:
                print("\nDeletion cancelled.")

            return

    print("❌ Task ID not found.")


# ==========================================================
# SEARCH
# ==========================================================

def search_tasks(tasks):

    if not tasks:
        print("\n📭 No tasks available.")
        return

    keyword = input(
        "\nSearch task/category: "
    ).strip().lower()

    if not keyword:
        print("❌ Search cannot be empty.")
        return

    results = []

    for task in tasks:

        if (
            keyword in task["name"].lower()
            or keyword in task["category"].lower()
        ):
            results.append(task)

    if not results:

        print("\n❌ No matching tasks found.")
        return

    print("\n🔎 SEARCH RESULTS")

    for task in results:
        display_task(task)


# ==========================================================
# FILTER
# ==========================================================

def filter_tasks(tasks):

    if not tasks:
        print("\n📭 No tasks available.")
        return

    print("\n" + "=" * 40)
    print("                FILTER")
    print("=" * 40)

    print("1. Completed")
    print("2. Pending")
    print("3. Overdue")
    print("4. High Priority")
    print("5. Medium Priority")
    print("6. Low Priority")

    choice = input("\nChoose filter: ").strip()

    results = []

    for task in tasks:

        if choice == "1" and task["completed"]:
            results.append(task)

        elif choice == "2" and not task["completed"]:
            results.append(task)

        elif choice == "3" and is_overdue(task):
            results.append(task)

        elif choice == "4" and task["priority"] == "High":
            results.append(task)

        elif choice == "5" and task["priority"] == "Medium":
            results.append(task)

        elif choice == "6" and task["priority"] == "Low":
            results.append(task)

    if not results:
        print("\n❌ No tasks found.")
        return

    print("\n🎯 FILTER RESULTS")

    for task in results:
        display_task(task)


# ==========================================================
# SORT TASKS
# ==========================================================

def sort_tasks(tasks):

    if not tasks:
        print("\n📭 No tasks available.")
        return

    print("\n" + "=" * 40)
    print("                SORT")
    print("=" * 40)

    print("1. Priority")
    print("2. Due Date")
    print("3. Task Name")
    print("4. Category")

    choice = input("\nChoose sorting option: ").strip()

    sorted_tasks = tasks.copy()

    if choice == "1":

        priority_order = {
            "High": 1,
            "Medium": 2,
            "Low": 3
        }

        sorted_tasks.sort(
            key=lambda task:
            priority_order[task["priority"]]
        )

    elif choice == "2":

        sorted_tasks.sort(
            key=lambda task:
            datetime.strptime(
                task["due_date"],
                "%d-%m-%Y"
            )
            if task["due_date"]
            else datetime.max
        )

    elif choice == "3":

        sorted_tasks.sort(
            key=lambda task:
            task["name"].lower()
        )

    elif choice == "4":

        sorted_tasks.sort(
            key=lambda task:
            task["category"].lower()
        )

    else:

        print("❌ Invalid option.")
        return

    print("\n↕️ SORTED TASKS")

    for task in sorted_tasks:
        display_task(task)


# ==========================================================
# DASHBOARD
# ==========================================================

def dashboard(tasks):

    total = len(tasks)

    completed = sum(
        1
        for task in tasks
        if task["completed"]
    )

    pending = sum(
        1
        for task in tasks
        if not task["completed"]
    )

    overdue = sum(
        1
        for task in tasks
        if is_overdue(task)
    )

    high_priority = sum(
        1
        for task in tasks
        if task["priority"] == "High"
        and not task["completed"]
    )

    if total > 0:

        completion_rate = (
            completed / total
        ) * 100

    else:

        completion_rate = 0

    print("\n" + "=" * 55)
    print("                    📊 DASHBOARD")
    print("=" * 55)

    print(f"Total Tasks        : {total}")
    print(f"Completed Tasks    : {completed}")
    print(f"Pending Tasks      : {pending}")
    print(f"Overdue Tasks      : {overdue}")
    print(f"High Priority      : {high_priority}")
    print(
        f"Completion Rate    : "
        f"{completion_rate:.2f}%"
    )

    print("=" * 55)


# ==========================================================
# MAIN MENU
# ==========================================================

def main():

    tasks = load_tasks()

    while True:

        print("\n")
        print("=" * 60)
        print("             📝 SMART TO-DO LIST")
        print("=" * 60)

        print("1.  📋 View All Tasks")
        print("2.  ➕ Add Task")
        print("3.  ✏️ Edit Task")
        print("4.  ✅ Complete / Pending")
        print("5.  🗑️ Delete Task")
        print("6.  🔎 Search Tasks")
        print("7.  🎯 Filter Tasks")
        print("8.  ↕️ Sort Tasks")
        print("9.  📊 Dashboard")
        print("10. 🚪 Exit")

        print("=" * 60)

        choice = input(
            "Enter your choice: "
        ).strip()

        if choice == "1":
            view_tasks(tasks)

        elif choice == "2":
            add_task(tasks)

        elif choice == "3":
            edit_task(tasks)

        elif choice == "4":
            toggle_task(tasks)

        elif choice == "5":
            delete_task(tasks)

        elif choice == "6":
            search_tasks(tasks)

        elif choice == "7":
            filter_tasks(tasks)

        elif choice == "8":
            sort_tasks(tasks)

        elif choice == "9":
            dashboard(tasks)

        elif choice == "10":

            print("\n👋 Thank you for using Smart To-Do List!")
            print("Keep being productive! 🚀")

            break

        else:

            print(
                "\n❌ Invalid choice. "
                "Please enter a number from 1-10."
            )


# ==========================================================
# START PROGRAM
# ==========================================================

if __name__ == "__main__":
    main()
