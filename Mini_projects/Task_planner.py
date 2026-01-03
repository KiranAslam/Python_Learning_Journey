def add_task():
    try:
        with open("tasks.txt","a") as f:
            task=input("Enter your Task: ")
            priority=input("Enter your Priority: ")
            deadline=input("Enter your Deadline: ")
            status="pending"
            f.write(f"{task},{priority},{deadline},{status}\n")
            print("=======================================")
            print("Task Added Successfully!") 
            print("=======================================")
    except Exception as e:
        print(f"Error: {e}")

def view_task():
    try:
        with open("tasks.txt","r") as f:
            tasks=f.readlines()
            if not tasks:
                print("No tasks found.")
            else:
               print("=======================================")
               print("           Your Tasks details          ")
               print("=======================================")
               for index, task in enumerate(tasks,start=1):
                    parts=task.strip().split(',')
                    if len(parts)==4:
                        print(f"{index}. [{parts[3]}] {parts[0]} | Priority: {parts[1]} | Due: {parts[2]}")
                    else:
                        print(f"{index}. Incomplete task data")
    except FileNotFoundError:
        print("No tasks found. Start by adding one!")
    except Exception as e:
        print(f"Error: {e}")       

def marked_completed():
    try:
        with open("tasks.txt","r") as f:
            tasks=f.readlines()
            if not tasks:
                print("There is no task to marked!")
                return
            view_task()
            print("=======================================")
            task_num=int(input("Enter The task number you want to mark as completed: "))
            with open("tasks.txt","w") as f:
                      for index, task in enumerate(tasks, start=1):
                           if index==task_num:
                              parts=task.strip().split(',')
                              if len(parts)==4:
                                  f.write(f"{parts[0]},{parts[1]},{parts[2]},completed\n")
                                  print("=======================================")
                                  print(f"Task '{parts[0]}' marked as completed!")
                                  print("=======================================")
                              else:
                                f.write(task)
                           else:
                                f.write(task)
    except ValueError:
        print("Invalid Input!")
    except Exception as e:
        print(f"Error: {e}")

def delete_task():
    try:
        with open("tasks.txt","r") as f:
            tasks=f.readlines()
            if not tasks:
                print("There is no tasks")
                return
            view_task()
            print("=======================================")
            task_num=int(input("Enter the task number you want to delete:"))
            print("=======================================")
            with open("tasks.txt","w") as f:
                for index, task in enumerate(tasks,start=1):
                    if index==task_num:
                        print(f"Task '{index}' deleted successfully!")
                    else:
                        f.write(task)
    except ValueError:
        print("Invalid Input!")
    except FileNotFoundError:
        print("No tasks found.")

def save_to_file():
    try:
        with open("tasks.txt","r") as f:
            tasks=f.readlines()
            with open("tasks_backup.txt","w") as backup:
                for task in tasks:
                    backup.write(task)
            print("==========================================")
            print("Tasks saved to backup file  successfully!")
            print("==========================================")
    except Exception as e:
        print(f"Error: {e}")

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
            print("=======================================")
            if choice==6:
                print("=======================================")
                print("Thank you for using To-Do List Manager")
                print("=======================================")
                break
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

main()