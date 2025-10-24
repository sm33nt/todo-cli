# Simple CLI to-do List application
# Author: Sameen Tanveer
# Date: 2025-10-24

tasks = []

def show_menu():
    print("\n To-Do List App")
    print("1. Add a Task")
    print("2. View Tasks")
    print("3. Remove a Task")
    print("4. Quit")

while True:
    show_menu()
    choice = input("Choose an option (1-4): ").strip()

    if choice == "1":
        task = input("Enter a new task: ").strip()
        if task:
            tasks.append(task)
            print(f" Task added: '{task}'")
        else:
            print(" Task cannot be empty!")

    elif choice == "2":
        if not tasks:
            print(" No tasks yet. Add one!")
        else:
            print("\nYour Tasks:")
            for i, task in enumerate(tasks, 1):
                print(f"{i}. {task}")

    elif choice == "3":
        if not tasks:
            print(" No tasks to remove.")
        else:
            for i, task in enumerate(tasks, 1):
                print(f"{i}. {task}")
            try:
                index = int(input("Enter task number to remove: ")) - 1
                if 0 <= index < len(tasks):
                    removed = tasks.pop(index)
                    print(f" Removed: '{removed}'")
                else:
                    print(" Invalid number.")
            except ValueError:
                print(" Please enter a number.")

    elif choice == "4":
        print(" Goodbye!")
        break

    else:
        print(" Invalid choice. Please pick between 1–4.")
