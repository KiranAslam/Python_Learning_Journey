def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    if b==0:
        print("Divided by zero is not allowed!")
    else:
        return a/b

def main():
    operations={1:add,2:sub,3:mul,4:div}
    while True:
       print("Calculator Functions")
       print("1. addition")
       print("2. subtraction")
       print("3. multiplication")
       print("4. division")
       print("5. Exit")
       user_input=int(input("Enter your choice: "))

       if user_input==5:
        print("Thank you for using the calculator!")
        break
       if user_input in operations:
        a=float(input("Enter first number: "))
        b=float(input("Enter second number: "))
        print("Result:", operations[user_input](a,b))
       else:
        print("Invalid choice")

main()
#Task 2
def greetings(name, message="Welcome to our app!"):
    print(name,message)

greetings("kiran","Asalam u alikum")
greetings("kiran")


#task 3
def get_stats(numbers):
    if not numbers:
        return 0,0
    else:
        return min(numbers), max(numbers)

def main():
    numbers=[]
    lists=int(input("Enter the number of elements in the list or 0 if want to exit: "))
    if lists==0:
        return
    elif lists>0:
        for i in range(lists):
            numbers.append(float(input("Enter number: ")))

    min_val, max_val = get_stats(numbers)

    print("Maximum:", max_val)
    print("Minimum:", min_val)

main()
#task 4
def sum_all(*args):
    return sum(args)
def main():
    print("Sum of all numbers:", sum_all(1,2,3,4,5))
main()

#Task 5

def num_seperator(numbers):
    even=[]
    odd=[]
    for n in numbers:
        if n%2==0:
            even.append(n)
        else:
            odd.append(n)
    return even, odd

number=[10,23,2,67,1,82,14,71,41,66,3,5]

even_num,odd_num=num_seperator(number)
print("Even list:", even_num)
print("Odd list:", odd_num)

#Task 6
def max_finder(a,b,c):
    if a>=b and a>=c:
        return a
    elif b>=a and b>=c:
        return b
    else:
        return c

a=45
b=3
c=97
print("Maximum number is:", max_finder(a,b,c))


#Task 7

def get_factorial(n):
    if n==0:
        return 1
    elif n>0:
        return n*get_factorial(n-1)
def main():
    fact= get_factorial(5)
    print("factorial",fact)
main()

# Task 8
def pass_strength(passward):
    if len(passward)>=8 and any(c.isupper() for c in passward) and any(c.islower() for c in passward) and any(c.isdigit() for c in passward):
        return "Strong"
    elif len(passward)>=8 and any(c.isdigit() for c in passward):
        return "good"
    else:
        return "Weak"

def main():
    passward=input("Enter your passward: ")
    strength=pass_strength(passward)
    print("passward strength: ", strength)

main()

# Task 9
def build_profile(name,**details):
    profile={}
    profile["name"]=name
    for key, value in details.items():
        profile[key]=value
    return profile

def main():
    profile = build_profile("kiran", age=25, city="hyderabad", occupation="software engineer")
    print(profile)

main()


#Task 10

def countdown(n):
    if n<=0:
        print("Blast off!")
    else:
        print(n)
        countdown(n-1)


countdown(10)
