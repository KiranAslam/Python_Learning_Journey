input_inches=float(input("Enter length in inches: "))
input_cm=float(input("Enter length in cm: "))
conversion=input_inches*2.54
is_inches_longer=int(conversion>input_cm)
print("result", is_inches_longer)