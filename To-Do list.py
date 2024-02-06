class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print("Task added successfully.")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks.")
        else:
            print("Tasks:")
            for i, task in enumerate(self.tasks, start=1):
                print(f"{i}. {task}")

    def mark_task_completed(self, index):
        if 1 <= index <= len(self.tasks):
            self.tasks[index - 1] += " (Completed)"
            print("Task marked as completed.")
        else:
            print("Invalid task index.")

    def delete_task(self, index):
        if 1 <= index <= len(self.tasks):
            del self.tasks[index - 1]
            print("Task deleted successfully.")
        else:
            print("Invalid task index.")

def main():
    todo_list = ToDoList()
    
    while True:
        print("\nTo-Do List Menu:")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Completed")
        print("4. Delete Task")
        print("5. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            task = input("Enter task: ")
            todo_list.add_task(task)
        elif choice == "2":
            todo_list.view_tasks()
        elif choice == "3":
            try:
                index = int(input("Enter index of task to mark as completed: "))
                todo_list.mark_task_completed(index)
            except ValueError:
                print("Invalid input. Please enter a valid integer.")
        elif choice == "4":
            try:
                index = int(input("Enter index of task to delete: "))
                todo_list.delete_task(index)
            except ValueError:
                print("Invalid input. Please enter a valid integer.")
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
