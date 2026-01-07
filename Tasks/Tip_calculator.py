bill=float(input("Enter your total bill: "))
total_person=int(input("Enterr how many people you are: "))
total_bill=bill*(0.15)+bill
tip_shares=total_bill/total_person
print("The share of each person is", tip_shares)