import random

print("welcome to guessing game ! \n you got only 5 atemp")

numberToGuess= random.randrange(50,100)
chance =5

guessCounter =0

while guessCounter < chance:
    guessCounter+= 1
    myGuess = int(input(" enter your number"))

    if myGuess == numberToGuess:
        print (f"the numberis {numberToGuess} : and you found it right")

        break
    elif guessCounter >=chance and myGuess != numberToGuess:
        print (f"oops sory  your nmber is {numberToGuess} try again ")
    elif myGuess < numberToGuess:
        print (" your guess is very low")
    elif myGuess > numberToGuess:
        print ( f" your guess is low")





