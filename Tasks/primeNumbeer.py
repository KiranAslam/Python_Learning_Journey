num=int(input("Enter the number: "))
is_prime=True
if num>1:
    for i in range(2,num):
        if num%i==0:
            is_prime=False
            break
    if is_prime==True:
        print("The number is prime")
    else:
        print("the number is not prime")

for num in range(2,51):
    is_prime=True
    for j in range(2,num):
        if num%j==0:
            is_prime=False
            break
    if is_prime==True:
        print(num, end=" ")