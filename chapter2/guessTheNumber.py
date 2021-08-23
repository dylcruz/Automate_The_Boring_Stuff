#This is a guess the number game. The player has 6 tries to guess a random number between 1 and 20

import random
import sys

number = random.randint(1,20)
guess = 0
tries = 0

print('I\'m thinking of a number between 1 and 20.')

while guess != number:
    if tries > 5:
        print("You lose! My number was " + str(number) + ".")
        sys.exit()
    
    print ('Take a guess:')
    
    guess = input()
    guess = int(guess)
    tries = tries + 1
    
    if guess < number:
        print("Your guess is too low.")
    elif guess > number:
        print("Your guess is too high.")

print("You got it! You guessed my number in " + str(tries) + ' tries!')