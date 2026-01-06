correct_user="Kiran"
correct_pin=2828
input_user=input("Enter user Name: ")
input_pin=int(input("Enter your PIN: "))
access_granted=(input_user==correct_user and input_pin==correct_pin)
print("Access granted:",access_granted)