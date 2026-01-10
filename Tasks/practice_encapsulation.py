#Task 01
class Account:
    def __init__(self, balance):
        self.__balance=balance
    def deposite(self,amount):
        if amount>0:
            self.__balance+=amount
            print(f"{amount} deposited successfully!")
        else:
            print("Invalid amount!")
    def get_balance(self):
        return self.__balance

my_acc=Account(10000)

# print(my_acc.__balance) this line gave error
my_acc.deposite(800)
print(my_acc.get_balance()) 

#Task 02

class Student:
    def __init__(self,name,marks):
        self.name=name
        self.__marks=marks
    def set_marks(self,value):
        if value>=0 and value<=100:
            self.__marks=value
            print(f"Marks updated to {value}")
        else:
            print("Invalid marks!")
    def get_marks(self):
        return self.__marks

s1=Student("kiran",100)
print(s1.set_marks(90))
print(s1.get_marks())