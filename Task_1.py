# To-Do List by Arpit Raj

tasks = []

def show_tasks():
    if not tasks:
        print("No tasks yet.")
    else:
        print("\nYour To-Do List:")
        for idx, task in enumerate(tasks, start=1):
            print(f"{idx}. {task}")

def add_task():
    task = input("Enter a new task: ")
    tasks.append(task)
    print("Task added successfully!")

def remove_task():
    show_tasks()
    try:
        task_num = int(input("Enter task number to remove: "))
        if 1 <= task_num <= len(tasks):
            removed = tasks.pop(task_num - 1)
            print(f"Removed task: {removed}")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def main():
    while True:
        print("\nTo-Do List Menu:")
        print("1. Show Tasks")
        print("2. Add Task")
        print("3. Remove Task")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            show_tasks()
        elif choice == '2':
            add_task()
        elif choice == '3':
            remove_task()
        elif choice == '4':
            print("Goodbye! 👋")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
