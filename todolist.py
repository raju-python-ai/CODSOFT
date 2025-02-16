# Simple To-Do List Application
todo_list = []

def show_tasks():
    if not todo_list:
        print("\nYour to-do list is empty.")
    else:
        print("\nYour To-Do List:")
        for index, task in enumerate(todo_list, start=1):
            print(f"{index}. {task}")

def add_task():
    task = input("\nEnter a task: ")
    todo_list.append(task)
    print(f'"{task}" has been added to your to-do list.')

def remove_task():
    show_tasks()
    try:
        task_num = int(input("\nEnter the task number to remove: ")) - 1
        if 0 <= task_num < len(todo_list):
            removed_task = todo_list.pop(task_num)
            print(f'"{removed_task}" has been removed.')
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def main():
    while True:
        print("\nTo-Do List Menu:")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Remove Task")
        print("4. Exit")
        
        choice = input("Choose any option: ")
        
        if choice == "1":
            show_tasks()
        elif choice == "2":
            add_task()
        elif choice == "3":
            remove_task()
        elif choice == "4":
            print("Tatahhhhhh!!!")
            break
        else:
            print("Invalid choice!!!")

if __name__ == "__main__":
    main()
