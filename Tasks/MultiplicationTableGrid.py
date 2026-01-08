num=int(input("how many tables you want to print: "))
for i in range(1,11):
    for j in range(1,num+1):
        print(i*j , end="\t")
    print()