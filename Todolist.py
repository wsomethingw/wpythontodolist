def todo_list():
    tasks = []

    while True:
        print("\n===== To-Do List =====")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")

        print("\nOptions:")
        print("1. Add Task")
        print("2. Mark Task as Completed")
        print("3. Quit")

        choice = input("Enter your choice (1/2/3): ")

        if choice == "1":
            new_task = input("Enter the new task: ")
            tasks.append(new_task)
        elif choice == "2":
            task_number = int(input("Enter the task number to mark as completed: "))
            if 1 <= task_number <= len(tasks):
                del tasks[task_number - 1]
            else:
                print("Invalid task number. Try again.")
        elif choice == "3":
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    todo_list()
