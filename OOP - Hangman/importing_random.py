# from random import randint

# print(random.randint(1, 100))
#
# print(random.random())

# print(randint(1, 100))

# from random import *
# import random as rn

import random

my_list = [1, 2, 7, 8, 10]
print(random.choice(my_list))

from classes_intro import Dog

new_dog = Dog("Fido", "White")
print(new_dog.intro())

from hangman_words import word_list
from random import choice
print(choice(word_list))

# Hangman game
# A class that handles the brain of hangman, that will know the word,
# methods to return things about the word, separate class to run the
# game logic, take input keep track of score
# third file to load them in

# Hangman "Brain" Class
#   Knows the word to guess
#   Has methods to return information about that word

# Hangman "Game" Class
#    Handle all the game logic
#    Get guesses off the player
#    Keep track of the scores