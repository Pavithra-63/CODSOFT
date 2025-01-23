# To-Do List Application
def display_menu():
    print("\nTo-Do List Application")
    print("1. View To-Do List")
    print("2. Add Task")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Mark Task as Completed")
    print("6. Exit")

def view_tasks(tasks):
    if not tasks:
        print("\nYour to-do list is empty!")
    else:
        print("\nTo-Do List:")
        for i, task in enumerate(tasks, 1):
            status = "✓ Completed" if task["completed"] else "⨯ Not Completed"
            print(f"{i}. {task['task']} [{status}]")

def add_task(tasks):
    task = input("\nEnter the task: ")
    tasks.append({"task": task, "completed": False})
    print("Task added successfully!")

def update_task(tasks):
    view_tasks(tasks)
    try:
        task_no = int(input("\nEnter the task number to update: ")) - 1
        if 0 <= task_no < len(tasks):
            new_task = input("Enter the updated task: ")
            tasks[task_no]["task"] = new_task
            print("Task updated successfully!")
        else:
            print("Invalid task number!")
    except ValueError:
        print("Please enter a valid number.")

def delete_task(tasks):
    view_tasks(tasks)
    try:
        task_no = int(input("\nEnter the task number to delete: ")) - 1
        if 0 <= task_no < len(tasks):
            tasks.pop(task_no)
            print("Task deleted successfully!")
        else:
            print("Invalid task number!")
    except ValueError:
        print("Please enter a valid number.")

def mark_completed(tasks):
    view_tasks(tasks)
    try:
        task_no = int(input("\nEnter the task number to mark as completed: ")) - 1
        if 0 <= task_no < len(tasks):
            tasks[task_no]["completed"] = True
            print("Task marked as completed!")
        else:
            print("Invalid task number!")
    except ValueError:
        print("Please enter a valid number.")

def main():
    tasks = []
    while True:
        display_menu()
        choice = input("\nEnter your choice (1-6): ")
        
        if choice == "1":
            view_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            update_task(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            mark_completed(tasks)
        elif choice == "6":
            print("\nThank you for using the To-Do List application. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
