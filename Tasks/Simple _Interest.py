principle=float(input("Enter the principle amount: "))
time=int(input("Enter duration of time: "))
rate=float(input("Enter the percentage of rate: "))
total_interest=(principle*time*rate)/100
print("total interest is ", total_interest)