import json
from tabulate import tabulate
from colorama import Fore, Style, init

init(autoreset=True)  # Automatically reset colors

tasks = []

# Function to add multiple tasks at once
def add_task():
    task_names = input(Fore.YELLOW + "Enter tasks (separate by commas): ")
    tasks_list = [task.strip() for task in task_names.split(",")]
    for task_name in tasks_list:
        task = {"name": task_name, "status": "Pending"}
        tasks.append(task)
    print(Fore.GREEN + f"✔ Added {len(tasks_list)} tasks!")
    save_tasks()

# Function to view all tasks
def view_tasks():
    if not tasks:
        print(Fore.RED + "No tasks available.")
    else:
        table = [[i+1, task["name"], task["status"]] for i, task in enumerate(tasks)]
        print("\n" + tabulate(table, headers=["No.", "Task", "Status"], tablefmt="fancy_grid"))

# Function to mark multiple tasks as completed
def complete_task():
    view_tasks()
    task_nums = input(Fore.YELLOW + "Enter task numbers to complete (separate by commas): ")
    
    try:
        task_indices = [int(num.strip()) - 1 for num in task_nums.split(",")]
        completed_count = 0

        for index in task_indices:
            if 0 <= index < len(tasks):
                tasks[index]["status"] = "Completed"
                completed_count += 1

        print(Fore.GREEN + f"✔ Marked {completed_count} tasks as completed!")
        save_tasks()
    except ValueError:
        print(Fore.RED + "⚠ Please enter valid task numbers.")

# Function to delete multiple tasks
def delete_task():
    view_tasks()
    task_nums = input(Fore.YELLOW + "Enter task numbers to delete (separate by commas): ")
    
    try:
        task_indices = sorted([int(num.strip()) - 1 for num in task_nums.split(",")], reverse=True)
        deleted_count = 0

        for index in task_indices:
            if 0 <= index < len(tasks):
                deleted_task = tasks.pop(index)
                deleted_count += 1
                print(Fore.GREEN + f"❌ Task '{deleted_task['name']}' deleted!")

        print(Fore.GREEN + f"✔ Deleted {deleted_count} tasks!")
        save_tasks()
    except ValueError:
        print(Fore.RED + "⚠ Please enter valid task numbers.")

# Function to save tasks to a file
def save_tasks():
    with open("tasks.json", "w") as file:
        json.dump(tasks, file)

# Function to load tasks from a file
def load_tasks():
    global tasks
    try:
        with open("tasks.json", "r") as file:
            tasks.extend(json.load(file))
    except FileNotFoundError:
        tasks = []

# Load tasks when the program starts
load_tasks()

# Main menu function
def main():
    while True:
        print("\n" + Fore.CYAN + "=" * 40)
        print(Fore.CYAN + "📌 TO-DO LIST MENU 📌".center(40))
        print(Fore.CYAN + "=" * 40)
        print(Fore.MAGENTA + "1️⃣ Add Tasks")
        print(Fore.MAGENTA + "2️⃣ View Tasks")
        print(Fore.MAGENTA + "3️⃣ Complete Tasks")
        print(Fore.MAGENTA + "4️⃣ Delete Tasks")
        print(Fore.MAGENTA + "5️⃣ Exit")
        print(Fore.CYAN + "=" * 40)

        choice = input(Fore.YELLOW + "Choose an option: ")

        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            complete_task()
        elif choice == "4":
            delete_task()
        elif choice == "5":
            print(Fore.GREEN + "Goodbye! ✅")
            break
        else:
            print(Fore.RED + "⚠ Invalid choice. Try again.")

# Run the program
if __name__ == "__main__":
    main()
