secret_number=18
while True:
    guess=int(input("Guess The number: "))
    if guess==secret_number:
        print("Congratulations! you won the game")
        break
    elif guess<secret_number:
        print("too low!")
    elif guess>secret_number:
        print("To High!")
    else:
        print("Invalid input!")