def add_expense(budget):
    try:
        description=input("Enter expense description: ")
        amount=float(input("Enter expense amount: "))

        current_expense=get_total_expense()
        if current_expense + amount > budget:
            print("warning: Expense exceeds budget.")
            print("you have", budget - current_expense, "remaining.")
        else:
            with open("Expensefile.txt", 'a') as f:
                f.write(f"{description},{amount}\n")
                new_balance = budget - (current_expense + amount)
                
                print("Expense added successfully!")
                print("new balance:", new_balance)
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

def calculate_total(budget):
    try:
        total=get_total_expense()
        balance = budget - total
        print("\n========= Summary =========")
        print(f"Total Budget:    {budget}")
        print(f"Total Spent:     {total}")
        print(f"Remaining:       {balance}")
    
        if balance < 0:
            print("You are exceeding your budget!")
        elif balance < (budget * 0.1): 
            print("Alert: you are running low on budget!")
            print("===========================")
    except ValueError:
        print("File format is not correct.")

def reset_tracker():
    try:
        with open("Expensefile.txt","w") as f:
            print("file reset successfully.")
    except FileNotFoundError:
        print("File not found.")
def save_budget(amount):
    with open("budget.txt", "w") as f:
        f.write(str(amount))

def load_budget():
    try:
        with open("budget.txt", "r") as f:
            content = f.read().strip()
            if content:
                return float(content)
            return 0.0 
    except FileNotFoundError:
        return 0.0
def get_total_expense():
    total=0
    try:
        with open("Expensefile.txt", "r") as f:
            for line in f:
                if "," in line:
                    parts=line.strip().split(',')
                    total+=float(parts[1])
    except FileNotFoundError:
        print("File not found.")
    except ValueError:
        print("File format is not correct.")
    return total

def main():
    try:
        budget = load_budget()
        if budget == 0:
           budget = float(input("Enter your monthly budget: "))
           save_budget(budget)
        while True:
            print("============Expense Tracker Menu==============")
            print(f"your current budget: {budget}")
            print("1. Add Expense")
            print("2. View All Expenses")
            print("3. Calculate Total")
            print("4. Reset Tracker")
            print("5. Update Budget")
            print("6. Exit")
            choice=int(input("Enter your choice: "))
            if choice==6:
                print("========Thank you for using Expense Tracker========")
                break
            elif choice==1:
                add_expense(budget)
            elif choice==2:
                view_all_expenses()
            elif choice==3:
                calculate_total(budget)
            elif choice==4:
                reset_tracker()
            elif choice==5:
                new_budget = float(input("Enter new budget: "))
                budget = new_budget
                save_budget(budget) 
                print("Budget updated!")
            else:
                print("Invalid choice. Please try again.")
    except ValueError:
        print("Invalid input. Please enter a number.")

main()