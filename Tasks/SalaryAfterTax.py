base_salary=int(input("Enter your salary:"))
tax=base_salary*(10/100)
bonus=base_salary*(2/100)
net_salary=base_salary
net_salary -=tax
net_salary +=bonus
print("base salary is", base_salary)
print("tax is", tax)
print("bonus is", bonus)
print("net salary is", net_salary)