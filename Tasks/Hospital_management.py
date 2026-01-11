# --- 1. Inheritance (Staff Hierarchy) ---
class Staff:
    def __init__(self, name, staff_id, base_salary):
        self.name = name
        self.staff_id = staff_id
        self._base_salary = base_salary  # Protected: Manager/Child classes use kar sakti hain

    def perform_duty(self):
        print("Staff is performing generic duties...")

# --- 2. Polymorphism (Role-Based Duty) ---
class Doctor(Staff):
    def perform_duty(self):
        print(f"Dr. {self.name} is examining patients and prescribing medicines. 🩺")

    def calculate_pay(self):
        # Doctor ko 20,000 extra allowance milta hai
        return self._base_salary + 20000

class Nurse(Staff):
    def perform_duty(self):
        print(f"Nurse {self.name} is monitoring vitals and giving injections. 💉")

    def calculate_pay(self):
        # Nurse ko 5,000 extra allowance milta hai
        return self._base_salary + 5000

# --- 3. Encapsulation (Secure Patient Data) ---
class Patient:
    def __init__(self, p_id, name, disease, bill):
        self.__p_id = p_id          # Private
        self.__disease = disease    # Private
        self.__bill = bill          # Private
        self.name = name            # Public

    # Getter for Security check
    def get_patient_details(self, entered_id):
        if entered_id == self.__p_id:
            print(f"Patient: {self.name} | Disease: {self.__disease} | Bill: Rs.{self.__bill}")
        else:
            print(f"Access Denied! ID {entered_id} is incorrect for patient {self.name}.")

# --- 4. Central Management (The Controller) ---

# Objects banate hain
doc1 = Doctor("Kiran", "D101", 150000)
nurse1 = Nurse("Samiya", "N502", 60000)

patient1 = Patient("P786", "Zayan", "Flu", 2500)

# --- Testing System ---

print("--- Hospital Staff Management ---")
hospital_staff = [doc1, nurse1]

for member in hospital_staff:
    member.perform_duty()
    print(f"Monthly Salary: Rs.{member.calculate_pay()}")
    print("-" * 30)

print("\n--- Patient Security Check ---")
# Galat ID se check karte hain
patient1.get_patient_details("P000")

# Sahi ID se check karte hain
patient1.get_patient_details("P786")