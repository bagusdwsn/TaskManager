from tasks.task_manager import TaskManager

def print_tasks(tasks):
    if not tasks:
        print("No tasks available.")
    else:
        print("Tasks:")
        for index, task in enumerate(tasks):
            print(f"{index + 1}. {task}")

def main():
    task_manager = TaskManager()
    task_manager.load_tasks("data/tasks.json")  # Load tasks from file

    while True:
        print("\nTask Manager Menu:")
        print("1. View tasks")
        print("2. Add task")
        print("3. Complete task")
        print("4. Delete completed tasks")
        print("5. Save and Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            tasks = task_manager.list_tasks()
            print_tasks(tasks)
        elif choice == "2":
            task_name = input("Enter task name: ")
            task_manager.add_task(task_name)
            print("Task added successfully.")
        elif choice == "3":
            tasks = task_manager.list_tasks()
            print_tasks(tasks)
            task_index = int(input("Enter task number to mark as complete: ")) - 1
            if 0 <= task_index < len(tasks):
                task_manager.complete_task(task_index)
                print("Task marked as complete.")
            else:
                print("Invalid task number.")
        elif choice == "4":
            task_manager.delete_completed_tasks()
            print("Completed tasks deleted.")
        elif choice == "5":
            task_manager.save_tasks("data/tasks.json")  # Save tasks to file
            print("Tasks saved. Exiting...")
            break
        else:
            print("Invalid choice. Please enter a number from the menu.")

if __name__ == "__main__":
    main()
