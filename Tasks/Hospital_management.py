class patient:
    def __init__(self,patient_ID,disease):
        self.__patient_ID=patient_ID
        self.__disease=disease
        self.secret_pin="1234"
    def get_details(self,pin):
        self.pin=pin
        if self.pin==self.secret_pin:
            print(f"Patient ID: {self.__patient_ID} , Diseases: {self.__disease}")
        else:
            print("Incorrect Pin!")
    
class person:
    def __init__(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender

class doctor(person):
    def __init__(self,name,age,gender,spacilization):
        self.spacilization=spacilization
        super().__init__(name,age,gender)
    def perform_duty(self):
        print(f"Dr. {self.name} {self.spacilization} is doing treatment.")

class Nurse(person):
    def __init__(self,name,age,gender,floor_num):
        self.floor_num=floor_num
        super().__init__(name,age,gender)
    def perform_duty(self):
        print(f"Nurse {self.name} is taking care of patients on floor {self.floor_num}.")

D1=doctor("Naeem",35,"Male","Heart Surgeon")
N1=Nurse("Asma",25,"female",2)
p1=patient(21,"heart attack")
N2=Nurse("Farhan",20,"male",1)
p2=patient(13,"food posioning")

staff_Lists=[D1,N1,N2]
for member in staff_Lists:
    member.perform_duty()

print("==security checck==")
p1.get_details("00000")
p1.get_details("1234")
p2.get_details("1234")