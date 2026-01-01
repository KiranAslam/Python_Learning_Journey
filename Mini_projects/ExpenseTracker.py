def add_expense():
    try:
        description=input("Enter expense description: ")
        amount=float(input("Enter expense amount: "))
        with open("Expensefile.txt", 'a') as f:
            f.write(f"{description},{amount}\n")
            print("Expense added successfully.")
    except ValueError:
        print("Invalid input. Please enter a valid amount.")

def view_all_expenses():
    try:
      with open("Expensefile.txt", "r")  as f:
        expense=f.readlines()
        if not expense:
            print("No expenses recorded yet.")
        else:
            print("========Expense Details========")
            for index,line in enumerate(expense, start=1):
                description,amount=line.strip().split(',')
                print(f"{index}. Description: {description}, Amount: {amount}")
    except FileNotFoundError:
        print("File not found.")

def calculate_total():
    try:
        total=0
        with open("Expensefile.txt", "r") as f:
            for line in f:
                description,amount=line.strip().split(',')
                total+=float(amount)
            print(f"Total expenses:{total}")
    except FileNotFoundError:
        print("File not found.")
    except ValueError:
        print("File format is not correct.")

def reset_tracker():
    try:
        with open("Expensefile.txt","w") as f:
            print("file reset successfully.")
    except FileNotFoundError:
        print("File not found.")
def main():
    try:
        budget=int(input("Enter your budget: "))
        while True:
            print("============Expense Tracker Menu==============")
            print("1. Add Expense")
            print("2. View All Expenses")
            print("3. Calculate Total")
            print("4. Reset Tracker")
            print("5. Exit")
            choice=int(input("Enter your choice: "))
            if choice==5:
                print("========Thank you for using Expense Tracker========")
                break
            elif choice==1:
                add_expense()
            elif choice==2:
                view_all_expenses()
            elif choice==3:
                calculate_total()
            elif choice==4:
                reset_tracker()
            else:
                print("Invalid choice. Please try again.")
    except ValueError:
        print("Invalid input. Please enter a number.")

main()