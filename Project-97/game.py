import random

print("number Guessing game")
number=random.randint(1,9)
chances=0
print("guess a number between 1 and 9!")

while chances <5:
    guess=int(input("enter your guess"))

    if guess ==number:
        print("Congratulations you Won the game")
        break
    elif guess<number:
        print("your guess was to low: guess a number higher then it",guess)
    else:
        print("your guess was too high guess another number",guess)
    chances+1
if not chances < 5:
    print("You lose!! the number was",number)
         

