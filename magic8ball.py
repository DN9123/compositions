import random, sys, pyperclip
while True:
    print("What is your question for the Magic 8-Ball? Type 'exit' to exit the program.")
    exit = input()
    if exit == "exit": # Exit is currently broken.
        sys.exit

    answer = random.randint(1,10)
    if answer == 1:
        print("Yes")
    elif answer == 2:
        print("No")
    elif answer == 3:
        print("Answer unclear, try again later.")
    elif answer == 4:
        print("Obviously")
    elif answer == 5:
        print("Probably not")
    elif answer == 6:
        print("Obviously not")
    elif answer == 7:
        print("Probably")
    elif answer == 8:
        print("Try again")
    elif answer == 9:
        print("My reply is no")
    