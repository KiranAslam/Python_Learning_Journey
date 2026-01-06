Lists=["kiran", "Samiya", "Mariyam", "Gulam u haiyu din", "rehan"]
for name in Lists:
    print(name)

price=[100,100,100,100,100]
total=0
for p in price:
    total+=p
print(total)

f_food=[]
for i in range(1,4):
   user_input=input("enter your favorite food: ")
   f_food.append(user_input)
print(f_food)

student_marks=[45,50,60,35,67,87,96,51,23]
pass_marks=[]
fail_marks=[]
for mark in student_marks:
    if mark<50:
        fail_marks.append(mark)
    else:
        pass_marks.append(mark)
print("Student who passed:", pass_marks)
print("Student who failed:", fail_marks)

cart = ["Mobile", "Laptop", "Watch", "Headphones"]
user_input=input("Enter what item you want to delete.")
if user_input in cart:
    cart.remove(user_input)
    print(cart)
else:
    print("Item not found in cart.")


num=[0,1,2,3,4,5,6,7,8,9]
print(num[1:6])
print(num[5:])
print(num[:])
print(num[::-1])