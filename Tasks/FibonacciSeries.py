n = int(input("Kitne numbers print karne hain? "))
a = 0
b = 1
count = 0

print("Fibonacci Series:")
while count < n:
    print(a, end=" ")
    c = a + b
    a = b
    b = c
    count += 1
n=15
a=0
b=1
print(a , b , end=" ")
for i in range(n-2):
    c=a+b
    print(c, end=" ")
    a=b
    b=c