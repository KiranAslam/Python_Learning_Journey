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
s1.set_marks(90)
print(s1.get_marks())

#Task 03
class DoorLock:
    def __init__(self,pin):
        self.__pin=pin
        self.__is_lock=True
    def unlock(self,entered_pin):
        self.entered_pin=entered_pin
        if self.entered_pin==self.__pin:
            self.__is_lock=False
            print("door unloacked Welcome!")
        else:
            print("Access denaied Wrong PIN!")
    def locked(self):
        self.__is_lock=True
        print("Now door is locked!")

my_door=DoorLock(1234)
my_door.unlock(1234)
my_door.locked()

#Task 04

class Employee:
    def __init__(self,name,salary):
        self.name=name
        self._salary=salary
class Manager(Employee):
    def show_bonus_salary(self):
        bonus=self._salary+5000
        print(f"Salary after Bonus: {bonus}")

e1=Employee("kiran",10000000)
m1=Manager("samiya",10000000)
print(e1._salary)
m1.show_bonus_salary()