#Task 1
class Leptop:

        def __init__(self,brand,ram,processor):
           self.brand=brand
           self.ram=ram
           self.processor=processor

        def show_specs(self):
            print(f"--- {self.brand} Laptop Specs ---")
            print(f"Processor: {self.processor}")
            print(f"RAM: {self.ram}GB")
            print("----------------------------") 

Leptop1=Leptop("dell",8,"i7")
Leptop2=Leptop("Hp",16,"i9")

Leptop1.show_specs()
Leptop2.show_specs()

#Task 2

class Book:
    def __init__(self,title,author,pages):
        self.title=title
        self.author=author
        self.pages=pages

    def read_info(self):
        print(f"-------{self.title} reading Info--------")
        print(f"Reading {self.title} by {self.author} which has {self.pages} pages.")

Book1=Book("Atomic habit","James clear",300)
Book2=Book("Steal Like an artist","Austisn",200)

Book1.read_info()
Book2.read_info()

#Task 3
class Oven:
    def __init__(self,brand,max_temp):
        self.brand=brand
        self.max_temp=max_temp

    def bake(self,item,temp):
        if temp<=self.max_temp:
            print(f"Baking {item} in {self.brand} oven at {temp}°C.")
        else:
            print(f"Error: {temp}°C exceeds the maximum temperature of {self.max_temp}°C for the {self.brand} oven.")

Oven1=Oven("Dawlance",200)
Oven2=Oven("Dell",250)

Oven1.bake("cookies",180)
Oven2.bake("bread",260)

#Task 4

class Insta:
    def __init__(self,username,bio):
        self.username=username
        self.bio=bio
        self.followers=0
    def post_photo(self,caption):
        print(f"Posted a photo: {caption}")

    def get_followed(self):
        self.followers+=1
    
    def show_profile(self):
        print(f"\n--- Instagram Profile: {self.username} ---")
        print(f"Bio: {self.bio}")
        print(f"Total Followers: {self.followers}")
        print("---------------------------------------")

Insta1=Insta("Kiran28","I am a developer")
Insta2=Insta("Writer","I am a writer")

Insta1.post_photo("Beautiful sunset.")
Insta1.get_followed()
Insta1.get_followed()
Insta1.show_profile()
Insta2.post_photo("What a lovely book.")
Insta2.show_profile()

#Task 5

class Employee:
    def __init__(self,name,designation,base_salary):
        self.name=name
        self.designation=designation
        self.base_salary=base_salary

    def bonus(self):
        return self.base_salary*0.10
        

    def payroll(self):
        bonus_val=self.bonus()
        total_salary=self.base_salary + bonus_val
        print(f"====={self.name}'s Payroll=====")
        print(f'Name: {self.name}')
        print(f'Designation: {self.designation}')
        print(f'Base Salary: ${self.base_salary}')
        print(f'Bonus: ${bonus_val}')
        print(f'Total Salary: ${total_salary}')

Employee1=Employee("Kiran","CEO",90000000)
Employee2=Employee("Ali","Manager",5000000)

Employee1.payroll()
Employee2.payroll()