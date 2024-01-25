a = [1, 2, 3, 4]
while a:
    print(a.pop())

'''
OUTPUT : {4 3 2 1}
'''

print(a)
'''
[]
'''

'''
# Simple game example

import random

def main():
    print("Welcome to the game!")
    print("Guess a number between 1 and 100.")
    print("You have 10 tries to guess the number.")

    # Generate a random number between 1 and 100
    number = random.randint(1, 100)

    # Keep track of the number of guesses
    guesses = 0

    # Loop until the user guesses the number or runs out of guesses
    while guesses < 10:
        # Get the user's guess
        guess = int(input("Enter your guess: "))

        # Increment the number of guesses
        guesses += 1

        # Check if the guess is correct
        if guess == number:
            print("Congratulations! You guessed the number in", guesses, "tries.")
            return

        # Check if the guess is too high
        elif guess > number:
            print("Your guess is too high. Try again.")

        # The guess must be too low
        else:
            print("Your guess is too low. Try again.")

    # The user has run out of guesses
    print("Sorry, you ran out of guesses. The number was", number)

if __name__ == "__main__":
    main()
'''

b = [ 1, 2, 3]
print(b.pop())
print(b)
'''
OUTPUT : 
3
[1, 2]
'''