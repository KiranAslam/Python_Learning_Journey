year=int(input("Enter the year: "))
if (year%4==0 and year%100!=0 )or year%400==0:
    print("The year is a leap year.")
else:
    print("no, its not a leap year.")