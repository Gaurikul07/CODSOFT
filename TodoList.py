import json

tasks_file = "tasks.json"

def load_tasks():
    try:
        with open(tasks_file, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_tasks(tasks):
    with open(tasks_file, "w") as file:
        json.dump(tasks, file, indent=2)

def show_tasks(tasks):
    if not tasks:
        print("No tasks yet!")
    else:
        for i, task in enumerate(tasks, 1):
            status = "✅" if task["done"] else "❌"
            print(f"{i}. {task['title']} {status}")

def add_task(tasks):
    title = input("Enter task: ").strip()
    if title:
        tasks.append({"title": title, "done": False})
        save_tasks(tasks)
        print("Task added!")
    else:
        print("Task title cannot be empty.")

def get_valid_index(prompt, tasks):
    try:
        index = int(input(prompt)) - 1
        if 0 <= index < len(tasks):
            return index
        else:
            print("Invalid index!")
    except ValueError:
        print("Please enter a number.")
    return None

def mark_done(tasks):
    show_tasks(tasks)
    index = get_valid_index("Mark which task as done? ", tasks)
    if index is not None:
        tasks[index]["done"] = True
        save_tasks(tasks)
        print("Task marked as done!")

def delete_task(tasks):
    show_tasks(tasks)
    index = get_valid_index("Delete which task? ", tasks)
    if index is not None:
        tasks.pop(index)
        save_tasks(tasks)
        print("Task deleted!")

def main():
    tasks = load_tasks()
    while True:
        print("\n1. View Tasks\n2. Add Task\n3. Mark Task as Done\n4. Delete Task\n5. Exit")
        choice = input("Choose an option: ").strip()
        if choice == "1":
            show_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            mark_done(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()
        