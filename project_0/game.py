"""Guess the number game"""
    
import numpy as np

number = np.random.randint (1,101) # Guess the number from 1 to 100

# number of guesses
count = 0

while True:
    count += 1
    predict_number = int (input ('Guess the number from 1 to 100: '))
    
    if  predict_number > number:
        print ('The number should be less')
    
    elif predict_number < number:
        print ('The number must be greater ')
    
    else:
        print (f'You guessed the number! This is the number {number} for {count} attemptsf')
        break # End of game, exit from cycle