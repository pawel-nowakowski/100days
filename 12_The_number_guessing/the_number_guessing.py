from random import randint

def guessNumber():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
    tries = 0
    number = randint(1, 100)
    if difficulty == 'easy':
        tries = 10
    elif difficulty == 'hard':
        tries = 5
    while tries != 0:
        print(f"You have {tries} attempts remaining to guess the number.")
        tries -= 1
        guess = int(input("Make a guess: "))
        if guess == number:
            return print(f"You got it! The answer was {number}.")
        elif guess < number:
            print("Too low.")
        elif guess > number:
            print("Too high")
        if tries == 0:
            print("You did not guess a number.")


guessNumber()