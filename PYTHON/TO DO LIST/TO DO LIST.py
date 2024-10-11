todo_list = []

def add_task(task):
    todo_list.append({"task": task, "completed": False})
    print(f'Task "{task}" added to the list')

def view_tasks():
    if not todo_list:
        print("Your to-do list is empty")
    else:
        print("\nTo-Do List:")
        for i, item in enumerate(todo_list, 1):
            status = " Done" if item["completed"] else " Not Done"
            print(f"{i}. {item['task']} [{status}]")
        print()

def mark_complete(task_number):
    if 0<task_number<=len(todo_list):
        todo_list[task_number - 1]["completed"]=True
        print(f'Task {task_number} marked as complete.')
    else:
        print("Invalid task number.")

def delete_task(task_number):
    if 0 < task_number <= len(todo_list):
        removed_task = todo_list.pop(task_number - 1)
        print(f'Task "{removed_task["task"]}" deleted from the list')
    else:
        print("Invalid task number")

def main():
    while True:
        print('TO-DO LIST')
        print("\nOptions:")
        print("1. Add a task")
        print("2. View tasks")
        print("3. Mark a task as complete")
        print("4. Delete a task")
        print("5. Exit")
        
        choice = input("Choose an option (1/2/3/4/5): ")
        if choice=='1':
            task=input("Enter the task: ")
            add_task(task)
        elif choice=='2':
            view_tasks()
        elif choice=='3':
            try:
                task_number=int(input("Enter the task number to mark as complete: "))
                mark_complete(task_number)
            except ValueError:
                print("Please enter a valid number")
        elif choice=='4':
            try:
                task_number = int(input("Enter the task number to delete: "))
                delete_task(task_number)
            except ValueError:
                print("Please enter a valid number.")
        elif choice=='5':
            print("Exiting To-Do List application")
            break
        else:
            print("Invalid choice Please try again")

if __name__=="__main__":
    main()
