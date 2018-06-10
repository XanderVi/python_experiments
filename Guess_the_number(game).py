'''
Game 'Guess the number from 0 to 1000'
'''

import random

number = random.randint(0, 1000)

your_answer = int(input('Enter the number from 0 to 1000: '))

while your_answer != number:
    if your_answer < number:
        your_answer = int(input('The number is greater. Enter the number from 0 to 1000: '))
    else:
        your_answer = int(input('The number is less. Enter the number from 0 to 1000: '))

print('You guessed! The number was:', number)