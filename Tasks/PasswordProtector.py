attempts=3
correct_pass="Kiran28"
while attempts>0:
    user_pass=input('Enter your password: ')
    if user_pass==correct_pass:
        print("Access Granted")
        break
    else:
        attempts-=1
        if attempts > 0:
            print(f"Wrong! {attempts} chances left.")
        else:
            print("Account Locked!  Too many failed attempts.")