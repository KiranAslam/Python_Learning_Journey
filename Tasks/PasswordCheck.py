correct_password="KiranAslam"
guess_pass=input("Enter your password: ")
while guess_pass!=correct_password:
    print("Invalid password try again")
    guess_pass=input("enter password: ")
else:
    print("Acess granted.")