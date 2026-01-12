import math
import random

print(math.sqrt(16))
print(math.log(30))
print(math.ceil(3.1))
print(math.floor(4.3))
print(math.factorial(5))
print(math.pow(2,3))

lucky_num=random.randint(1,100)
print(f"Todays lucky Number is {lucky_num}")

member_lists=["Kiran","Samiya","mariyam","Rehan","Munazzah","Noor","Faizan","Hassan","Gulam u din"]
lucky_member=random.choice(member_lists)
print(f"Lucky member is {lucky_member}")
random.shuffle(member_lists)
print(member_lists)
print(random.sample(member_lists,3))
print(random.random())
