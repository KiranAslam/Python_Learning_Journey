unique_num=set()
while True:
    user_input=int(input("Enter a number (or 0 if want to exit.): "))
    if user_input==0:
        print("Thank u!")
        break
    else:
        unique_num.add(user_input)
print("Number in the set are", unique_num)