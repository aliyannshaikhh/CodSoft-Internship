tasks = []

def add_task():
    task = input("Enter task: ")
    tasks.append(task)
    print("Task added successfully!")

def delete_task():
    task_index = int(input("Enter task index to delete: ")) - 1
    if 0 <= task_index < len(tasks):
        del tasks[task_index]
        print("Task deleted successfully!")
    else:
        print("Invalid task index!")

def update_task():
    task_index = int(input("Enter task index to update: ")) - 1
    if 0 <= task_index < len(tasks):
        new_task = input("Enter new task: ")
        tasks[task_index] = new_task
        print("Task updated successfully!")
    else:
        print("Invalid task index!")

def display_tasks():
    print("Your To-Do List:")
    if tasks:
        for i in range(len(tasks)):
            print(f"{i + 1}. {tasks[i]}")
    else:
        print("Your to-do list is empty!")

def main():
    while True:
        print("\nMenu:")
        print("1. Add Task")
        print("2. Delete Task")
        print("3. Update Task")
        print("4. Display Tasks")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            add_task()
        elif choice == '2':
            delete_task()
        elif choice == '3':
            update_task()
        elif choice == '4':
            display_tasks()
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice! Please enter a valid option.")


if __name__ == "__main__":
    main()