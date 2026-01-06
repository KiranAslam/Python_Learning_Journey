contacts={}
for i in range(1,4):
    name=input("Enter a contact Name: ")
    phone_no=input("Enter a contact number: ")
    contacts[name]=phone_no
print(contacts)
print("Whoes number do you want to find?: ")
find=input("Enter a Name: ")
if find in contacts:
    print(contacts[find])
else:
    print("number is not found!")


