class Staff:
    def __init__(self, name, staff_id, base_salary):
        self.name = name
        self.staff_id = staff_id
        self._base_salary = base_salary

    def perform_duty(self):
        print("Staff is performing generic duties...")
class Doctor(Staff):
    def perform_duty(self):
        print(f"Dr. {self.name} is examining patients and prescribing medicines. 🩺")

    def calculate_pay(self):
        return self._base_salary + 20000

class Nurse(Staff):
    def perform_duty(self):
        print(f"Nurse {self.name} is monitoring vitals and giving injections. 💉")

    def calculate_pay(self):
        return self._base_salary + 5000
class Patient:
    def __init__(self, p_id, name, disease, bill):
        self.__p_id = p_id          
        self.__disease = disease    
        self.__bill = bill          
        self.name = name            

    def get_patient_details(self, entered_id):
        if entered_id == self.__p_id:
            print(f"Patient: {self.name} | Disease: {self.__disease} | Bill: Rs.{self.__bill}")
        else:
            print(f"Access Denied! ID {entered_id} is incorrect for patient {self.name}.")
doc1 = Doctor("Kiran", "D101", 150000)
nurse1 = Nurse("Samiya", "N502", 60000)
patient1 = Patient("P786", "Zayan", "Flu", 2500)
print("--- Hospital Staff Management ---")
hospital_staff = [doc1, nurse1]
for member in hospital_staff:
    member.perform_duty()
    print(f"Monthly Salary: Rs.{member.calculate_pay()}")
    print("-" * 30)
print("\n--- Patient Security Check ---")
patient1.get_patient_details("P000")
patient1.get_patient_details("P786")