import random


def generateSecretNumber(a, b):
    return random.randint(a, b)


def Intro():
    print("Let's play a game: ")
    print("I will ask you for a range of numbers, and a number of guesses that will be allowed.")
    print("Then you will have to guess a randomly generated number from that range in those number of guesses")
    print("Ready?")
    print("\n")

# Plays the Introduction
Intro()

a = int(input("Enter your lower range: "))
b = int(input("Enter your upper range: "))
secretNumber = generateSecretNumber(a, b)
guesses = int(input("Enter the number of attempts you would like: "))
count = 0

while 1:
    guess = int(input("Take a guess.\n"))

    if guess == secretNumber:
        print("Good Job! You guessed my number in " + str(count + 1) + " guesses")
        break
    elif secretNumber < guess <= b:
        print("Your guess is too high")
        guesses = guesses - 1
    elif secretNumber > guess >= a:
        print("Your guess is too low")
        guesses = guesses - 1

    if guesses == 0:
        print("Oops! Your out of guesses! Sorry, the number was " + str(secretNumber) + ".")
        break
    count = count + 1
