import math
import random
from datetime import datetime

now=datetime.now()
print(f"current time:{now}")
print(f"year: {now.year}")
formatted_date = now.strftime("%d/%m/%Y")
print(f"formatted date:{formatted_date} ")

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


student_list=["kiran","samiya","mariyam","munazzah","noor","faizan","rehan"]
random.shuffle(student_list)

seat_no_start=101
for s in student_list:
    print(f"Seat No: {seat_no_start} | Student Name: {s}")
    seat_no_start+=1

secret_number=random.randint(1,100)
attempts=0
print("You have 5 attemps only!")
while attempts<5:
       user_guess=int(input("Guess The number Between 1-100: "))
       attempts+=1
       if user_guess<secret_number:
            print("Too Low!")
       elif user_guess>secret_number:
            print("Too High!")
       elif user_guess==secret_number:
            print(f" You won! You guessed it in {attempts} attempts.")
            break 
       else:
          print("Invalid input!")
else:
    print(f"Game over! The Number is {secret_number}.")

