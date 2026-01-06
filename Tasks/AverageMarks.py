total_marks=0
count=0
while True:
    marks=int(input("Enter your marks or -1 to calculate average:"))
    if marks ==-1:
        break
    total_marks+=marks
    count+=1
if count>0:
    average=total_marks/count
    print(average)