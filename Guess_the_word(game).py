'''
Game 'Guess the word'
'''

import random

#the list(tuple) of words for the game
WORDS = ('money', 'country', 'capital', 'vacancy', 'weekend', 'thousand', 'village',
         'director', 'military', 'vacation', 'bestseller', 'movie')

#random chooser of the word for the game
word = random.choice(WORDS)

#word for players will display as '*a**ta*' or something like that
hidden_word = ['*' for i in range(len(word))]

#letters which players have try to guess the word
letters = []

level = input('Choose a difficulty: Hard(3 lives), Medium(5 lives), Easy(7 lives): ')
while level.lower() not in ['hard', 'medium', 'easy']:
    level = input('Please, choose a difficulty: Hard(3 lives), Medium(5 lives), Easy(7 lives): ')

if level.lower() == 'hard':
    lives = 3
elif level.lower() == 'medium':
    lives = 5
elif level.lower() == 'easy':
    lives = 7

#main game loop
while lives > 0:
    letters = list(set(letters))
    
    print('The word is:', ''.join(hidden_word))
    print(lives, 'lives are left. Choose wisely.')
    l = input('Try to guess the letter: ')
    
    if l not in letters:
        letters.append(l)
    else:
        print("You've chosen this letter already. Try another one.")
        if l not in word:
            lives += 1
    
    if l in word:
        print("It's the right letter! Let's proceed.")
        lives += 1
        for i in range(len(word)):
            if l == word[i]:
                hidden_word[i] = l
    
    if ''.join(hidden_word) == word:
        print("You've made it! The right word is:", word)
        break
    
    print('\n')

    lives -= 1

if lives <= 0:
    print("Sorry, you didn't guess...")
    print("The word was:", word)