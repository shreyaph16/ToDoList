# To-Do List 📝

A simple and interactive **command-line To-Do List application** built using **Python**. It allows users to efficiently manage tasks by adding, viewing, marking as completed, and deleting multiple tasks at once.

## Features ✨
- ✅ Add multiple tasks at once
- 📋 View tasks in a formatted table
- ✅ Mark multiple tasks as completed
- ❌ Delete multiple tasks at once
- 💾 Auto-save functionality using JSON
- 🎨 Colored UI for better readability (using `colorama`)
- 📊 Neatly formatted output using `tabulate`

## Installation 🛠
To run this project, make sure you have **Python** installed on your system.

### 1️⃣ Clone the Repository
```sh
git clone https://github.com/shreyaph16/ToDoList.git
cd ToDoList
```

### 2️⃣ Install Dependencies
```sh
pip install -r requirements.txt
```
If `requirements.txt` is not available, install manually:
```sh
pip install tabulate colorama
```

## Usage 🚀
Run the program with:
```sh
python main.py
```

### Main Menu 🏠
```
========================================
📌 TO-DO LIST MENU 📌
========================================
1️⃣ Add Task(s)
2️⃣ View Tasks
3️⃣ Mark Task(s) as Completed
4️⃣ Delete Task(s)
5️⃣ Exit
========================================
```

### Add Multiple Tasks 📝
When prompted, enter multiple tasks **separated by commas**.
```
Enter tasks (comma-separated): Buy milk, Complete assignment, Read a book
✔ Task 'Buy milk' added!
✔ Task 'Complete assignment' added!
✔ Task 'Read a book' added!
```
