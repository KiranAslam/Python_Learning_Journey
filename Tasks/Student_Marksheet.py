sub1=int(input("enter marks of maths subject out of 100: "))
sub2=int(input("enter marks of science subject out of 100: "))
sub3=int(input("enter marks of english subject out of 100: "))
average=(sub1+sub2+sub3)/3
percentage=(average/100)*100
result=average>50
print("average is: ", average)
print("result is: ", result)
print("percentage is: ", percentage)