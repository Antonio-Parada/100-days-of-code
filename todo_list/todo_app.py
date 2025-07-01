class TodoList:
    def __init__(self):
        self.tasks = []
        self.task_id_counter = 0

    def add_task(self, description, status="todo"):
        self.task_id_counter += 1
        task = {
            'id': self.task_id_counter,
            'description': description,
            'status': status
        }
        self.tasks.append(task)
        print(f"Task '{description}' added with ID {self.task_id_counter}.")

    def update_task_status(self, task_id, new_status):
        for task in self.tasks:
            if task['id'] == task_id:
                task['status'] = new_status
                print(f"Task {task_id} status updated to '{new_status}'.")
                return
        print(f"Task with ID {task_id} not found.")

    def display_tasks(self, status=None):
        print("\n--- Your Tasks ---")
        found_tasks = False
        for task in self.tasks:
            if status is None or task['status'] == status:
                print(f"ID: {task['id']}, Description: {task['description']}, Status: {task['status']}")
                found_tasks = True
        if not found_tasks:
            if status:
                print(f"No tasks found with status '{status}'.")
            else:
                print("No tasks added yet.")
        print("------------------")

if __name__ == "__main__":
    todo_list = TodoList()

    print("Welcome to your CLI ToDo List!")
    while True:
        print("\nCommands: add, update, show all, show todo, show ongoing, show completed, exit")
        command = input("Enter command: ").lower()

        if command == "add":
            desc = input("Enter task description: ")
            todo_list.add_task(desc)
        elif command == "update":
            try:
                task_id = int(input("Enter task ID to update: "))
                new_status = input("Enter new status (todo, ongoing, completed): ").lower()
                if new_status in ["todo", "ongoing", "completed"]:
                    todo_list.update_task_status(task_id, new_status)
                else:
                    print("Invalid status. Please use 'todo', 'ongoing', or 'completed'.")
            except ValueError:
                print("Invalid task ID.")
        elif command == "show all":
            todo_list.display_tasks()
        elif command == "show todo":
            todo_list.display_tasks("todo")
        elif command == "show ongoing":
            todo_list.display_tasks("ongoing")
        elif command == "show completed":
            todo_list.display_tasks("completed")
        elif command == "exit":
            print("Goodbye!")
            break
        else:
            print("Unknown command. Please try again.")