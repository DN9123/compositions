print('How many dogs do you have? Please enter your response as an integer.')
numDogs = input('> ')
try:
    if int(numDogs) >= 4:
        print("That is a lot of dogs!")
    else:
        print("That isn't a lot of dogs.")
except ValueError:
    print("Error. You did not enter an integer.")
