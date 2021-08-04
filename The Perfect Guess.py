import random

randNo = random.randint(1, 100)


userGuess = None
Guesses = 0
while(userGuess != randNo):

    userGuess = int(input("Guess the number:"))
    Guesses += 1
    if (userGuess == randNo):
        print("You Guess right")
    else:
        if (userGuess>randNo):
            print("You Guess it Wrong! Enter a smaller number")
        else:
            print("You Guess it Wrong! Enter a larger number")

print(f"You Guess the number in {Guesses} Guesses")

with open("highscore.txt", "r") as f:
    hiscore = int(f.read())

if (Guesses < hiscore):
    print("you have just Broken the high score! ")
    with open("highscore.txt", "w") as f:
        f.write(str(Guesses))









































