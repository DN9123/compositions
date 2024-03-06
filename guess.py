# This program is a "Guess my number" style game.
import random
print("Hello, friend! What is your name?")
name = input()
print("Well met, " + name + ". Say, I have a challenge for you.")
print("If you can guess the number that I am thinking of, you'll win bragging rights.")
secretNumber = random.randint(1,10)
for guessesTaken in range (1,6):
    print("Go ahead, kind stranger, take a guess.")
    guess = int(input())
    if guess > secretNumber:
        print("No, not at all. Your guess is too high.")
    elif guess < secretNumber:
        print("No, not at all. Your guess is too low.")
    else:
        break
if guess == secretNumber:
    print("Congratulations! You've guessed the number!")
else:
    print("No, you've failed. My number was " + str(secretNumber) + ".")
input("")