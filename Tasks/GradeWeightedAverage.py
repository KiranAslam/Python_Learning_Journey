midterms=int(input("Enter your midterm marks out of 100:"))
finalterms=int(input("Enter your final exam marks out of 100: "))
weighted_average=(midterms*0.30)+(finalterms*0.70)
total_score=weighted_average>=60
print("your weighted average is", weighted_average)
print("You passed the course:", total_score)