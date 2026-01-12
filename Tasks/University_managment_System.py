class University_member:
    def __init__(self,name,age,member_ID):
        self.name=name
        self.age=age
        self.member_ID=member_ID

class Professor(University_member):
    def  __init__(self,name,age,member_ID,subject):
        self.subject=subject
        super().__init__(name,age,member_ID)
    def activity(self):
        print(f"Professor {self.name} is teaching {self.subject}.")

class Student(University_member):
    def __init__(self,name,age,member_ID,gpa,bank_balance,exam_paper):
        self.__gpa=gpa
        self.__bank_balance=bank_balance
        self.__exam_paper=exam_paper
        self.secret_pin="1234"
        super().__init__(name,age,member_ID)
    def get_gpa(self):
        return self.__gpa
    def activity(self):
        print(f"Student {self.name} is studying has GPA {self.__gpa}")
    def pay_fees(self,amount):
        self.amount=amount
        self.__fees_paid=False
        print(f"\nAttempting to pay fees for {self.name}: Rs.{self.amount}")
        if self.__bank_balance>=self.amount:
            self.__bank_balance-=amount
            self.__fees_paid=True
            print(f"Fees Paid! Remaining Balance: Rs.{self.__bank_balance}")
        else:
           print("Insufficient Balance") 
    
    def view_exam_paper(self,pin):
        self.pin=pin
        if self.secret_pin==self.pin:
            print("Now you are allow to view your exam papers!")
        else:
            print("Incorrect PIN!")

P1=Professor("Mohsin",34,6657,"Knowledge Representation and reasoing")
P2=Professor("Naeem",45,8482,"Machine Learning")
S1=Student("Kiran",22,"23BSAI028",3.94,100000,"english")
S2=Student("Samiya",20,"23BSAI036",3.34,40000,"ML")

member_lists=[P1,P2,S1,S2]
print("----------------------------")
S1.pay_fees(40000)
S2.pay_fees(50000)
print("---------------------------")
S1.view_exam_paper("1234")
S2.view_exam_paper("7646")
print("---------------------------")
for i in member_lists:
    i.activity()
print("---------------------------")
for i in member_lists:
    if isinstance(i,Student):
        if i.get_gpa()>3.5:
             print(f"Student Name: {i.name} | GPA: {i.get_gpa()}")