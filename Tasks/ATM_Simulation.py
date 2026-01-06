Balance=1000
while True:
    print("\n--- Current Balance:", Balance, "---")
    print("ATM Simulation")
    print("1. check balance.")
    print("2. deposit money.")
    print("3. withdraw money.")
    print("4. exit.")
    choice=int(input("Enter your choice(1-4): "))
    if choice==1:
        print("Your Balance is:", Balance)
    elif choice==2:
        dep=int(input("Enter how much amount you want to deposit: "))
        Balance+=dep
        print("your updated balance is:", Balance)
    elif choice==3:
        withd=int(input("Enter how much you amount to withdraw: "))
        if withd<=Balance:
           Balance-=withd
           print("Withdrawal successful.")
           print("Your updated balance is:", Balance)
        else:
           print("Insufficient funds.")
    elif choice==4:
         print("Thank you for using the ATM.")
         break
    else:
         print("Invalid choice.")