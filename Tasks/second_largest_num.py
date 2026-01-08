lists=[2,4,7,8,34,23,67]
a=-1
b=-1
for i in lists:
    if i>a:
        b=a
        a=i
    elif i > b and i != a:
        b=i
print("Second largest number is:", b)