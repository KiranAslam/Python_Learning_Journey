def add_task():
    try:
        with open("tasks.txt","a") as f:
            task=input("Enter your Task: ")
            priority=input("Enter your Priority: ")
            deadline=input("Enter your Deadline: ")
            status="pending"
            f.write(f" {task},{priority},{deadline},{status}\n")
            print("====Task Added Successfully====") 
    except Exception as e:
        print(f"Error: {e}")

def view_task():
    try:
        with open("tasks.txt","r") as f:
            tasks=f.readlines()
            if not tasks:
                print("No tasks found.")
            else:
                for index, task in enumerate(tasks,start=1):
                    parts=task.strip().split(',')
                    if len(parts)==4:
                        print(f"{index}. [{parts[3]}] {parts[0]} | Priority: {parts[1]} | Due: {parts[2]}")
                    else:
                        print(f"{index}. Incomplete task data")
    except FileNotFoundError:
        print("fNo tasks found. Start by adding one!")
    except Exception as e:
        print(f"Error: {e}")       

def marked_completed():
    print("hi")
                     
def delete_task():
    print("hi")

def save_to_file():
    print("hi")

def main():
    try:
        while True:
            print("==========To-Do List Manager==========")
            print("1. Add Task")
            print("2. View Tasks")
            print("3. Mark Task as Completed")
            print("4. Delete Task")
            print("5. Save Tasks to File")
            print("6. Exit")
            print("=======================================")
            choice=int(input("Enter your choice: "))
            if choice==6:
                print("==Thank you for using To-Do List Manager==")
            elif choice==1:
                add_task()
            elif choice==2:
                view_task()
            elif choice==3:
                marked_completed()
            elif choice==4:
                delete_task()
            elif choice==5:
                save_to_file()
            else:
                print("Invalid choice. Please try again.")
    except ValueError:
        print("Invalid input. Please enter a number.")