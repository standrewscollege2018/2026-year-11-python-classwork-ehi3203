'''Demonstrate while loop in a guessing game'''

import random
#Pick a ramdom integer from 1 to 10
NUMBER = random.randist(1,10)

ask_guess=True

while ask_guess==True:
    #Get the guess and check if it is correct
    #If correct, set ask_guess to False
    guess=int(input("Guess a number from 1 to 10"))
    if guess ==NUMBER:
        ask_guess = False
    elif guess < NUMBER:
        print("Too low")
    else:
        print("Too high")

print("well done")
