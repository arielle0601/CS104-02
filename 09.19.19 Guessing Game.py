import random

theComputerNumber = random.randint(1, 1000000)
gameOver = False 

numberOfGuesses = 0
guess = 0

highGuessRange = 1000000
lowGuessRange = 1
    
while guess != theComputerNumber and numberOfGuesses <= 20 and gameOver != True:

    guess = int(input("Enter a guess: "))

    if guess < lowGuessRange or guess > highGuessRange:
        print("Your guess is out of range.")
        
    elif guess > theComputerNumber:
        highGuessRange = guess
        print("Your guess is too high.")
        
    elif guess < theComputerNumber:
        lowGuessRange = guess
        print("Your guess is too low.")

    else:
        print("Your guess is correct!")

    numberOfGuesses += 1

if guess == theComputerNumber:
    numberOfGuesses = str(numberOfGuesses)
    print("Good job! You guessed my number in " + numberOfGuesses + " guesses!")

if guess != theComputerNumber:
    theComputerNumber = str(theComputerNumber)
    print("Sorry, you ran out of tries. The correct number was " + theComputerNumber)
