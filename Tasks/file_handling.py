
#Tassk 1
with open("text.txt", "w") as f:
    f.write("Hello Kiran \n")
    f.write("This is my first file\n")


    
#Task 2
with open("text.txt","r") as f:
    content=f.read()
    print("file content\n", content)

#Task 3
with open("text.txt", "a") as f:
    f.write("This is my third line\n")
    f.write("this is my four line\n")
with open("text.txt", "r") as f:
    content=f.read()
    print("Updated file content\n", content)
#Task 4
with open("text.txt","r") as f:
    count=f.readlines()
    print("Number of lines in the file:", len(count))
#Task 5
with open("fruite.txt","w") as f:
    f.write("fruite lists")
    f.write("I like Apple")
    f.write("I like banana")
    f.write("I like orange")
with open("fruite.txt","r") as f:
    content=f.read().lower()
    user_input=input("Enter the fruite you like: ").lower()
    if user_input in content:
        print("Found!")
    else:
        print("not found")
#Task 6 
with open("fruite.txt","r") as f:
    content=f.read().upper()
with open("UPPERCASE.txt","w") as f:
    f.write(content)
with open("UPPERCASE.txt","r") as f:
    content=f.read()
    print("UPPERCASE file content\n", content)

#Task 7
with open("numbers.txt", "w") as f:
    f.write("1\n2\n3\n4\n5")
with open("numbers.txt", "r") as f:
    content=(f.readlines())
    sum=0
    for n in content:
        sum+=int(n.strip())
print("Sum of numbers in the file:", sum)

#Task 8
# Phone Book Program
with open("contacts.txt", "a") as file:
    while True:
        name = input("Enter name (or type 'stop' to finish): ")
        if name.lower() == "stop":
            break
        phone = input("Enter phone number: ")
        file.write(f"{name}: {phone}\n")

print("\nAll Contacts:\n")
with open("contacts.txt", "r") as file:
    contacts = file.read()
    print(contacts)
