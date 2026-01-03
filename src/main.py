from . import services

def print_task(task):
    """Helper function to print a single task."""
    status = "Done" if task.completed else "Incomplete"
    print(f"ID: {task.id} | Title: {task.title} | Description: {task.description} | Status: {status}")

def view_tasks():
    """Displays all tasks."""
    tasks = services.find_all_tasks()
    if not tasks:
        print("\nNo tasks found.")
    else:
        print("\n--- All Tasks ---")
        for task in tasks:
            print_task(task)
        print("-----------------")

def add_task():
    """Handles adding a new task."""
    print("\n--- Add New Task ---")
    title = input("Enter task title: ")
    description = input("Enter task description: ")
    task, error = services.create_task(title, description)
    if error:
        print(f"\nError: {error}")
    else:
        print(f"\nSuccess: Task '{task.title}' added with ID {task.id}.")

def update_task():
    """Handles updating an existing task."""
    print("\n--- Update Task ---")
    try:
        task_id = int(input("Enter the ID of the task to update: "))
        task = services.find_task_by_id(task_id)
        if not task:
            print("\nError: Task not found.")
            return
            
        print("Enter new details (leave blank to keep current value):")
        title = input(f"New title ({task.title}): ") or task.title
        description = input(f"New description ({task.description}): ") or task.description
        
        updated_task, error = services.edit_task(task_id, title, description)
        if error:
            print(f"\nError: {error}")
        else:
            print(f"\nSuccess: Task {task_id} updated.")
    except ValueError:
        print("\nError: Invalid ID. Please enter a number.")

def delete_task():
    """Handles deleting a task."""
    print("\n--- Delete Task ---")
    try:
        task_id = int(input("Enter the ID of the task to delete: "))
        success, error = services.remove_task(task_id)
        if error:
            print(f"\nError: {error}")
        elif success:
            print(f"\nSuccess: Task {task_id} deleted.")
    except ValueError:
        print("\nError: Invalid ID. Please enter a number.")

def toggle_complete():
    """Handles marking a task as complete or incomplete."""
    print("\n--- Toggle Task Completion ---")
    try:
        task_id = int(input("Enter the ID of the task to toggle: "))
        task, error = services.toggle_task_completion(task_id)
        if error:
            print(f"\nError: {error}")
        else:
            status = "completed" if task.completed else "incomplete"
            print(f"\nSuccess: Task {task.id} marked as {status}.")
    except ValueError:
        print("\nError: Invalid ID. Please enter a number.")

def main_menu():
    """Displays the main menu and handles user choices."""
    while True:
        print("\n===== To-Do List Main Menu =====")
        print("1. Add Task")
        print("2. View All Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Mark Task Complete/Incomplete")
        print("6. Exit")
        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            add_task()
        elif choice == '2':
            view_tasks()
        elif choice == '3':
            update_task()
        elif choice == '4':
            delete_task()
        elif choice == '5':
            toggle_complete()
        elif choice == '6':
            print("\nExiting application. Goodbye!")
            break
        else:
            print("\nInvalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    print("Welcome to the In-Memory To-Do List!")
    main_menu()
