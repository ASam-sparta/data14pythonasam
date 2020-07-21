import random
from random import choice
#alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


scores_dict = {'A': 1, 'B': 3, 'C': 3, 'D': 2, 'E': 1, 'F': 4, 'G': 2, 'H': 4, 'I': 1, 'J': 8, 'K': 5, 'L': 1, 'M': 3,
               'N': 1, 'O': 1, 'P': 3, 'Q': 10, 'R': 1, 'S': 1, 'T': 1, 'U': 1, 'V': 4, 'W': 4, 'X': 8, 'Y': 4, 'Z': 10}

class ScrabbleGame():
    def __init__(self):
        self.scrabble_pool = {'A': 9, 'B': 2, 'C': 2, 'D': 4, 'E': 12, 'F': 2, 'G': 3, 'H': 2, 'I': 9, 'J': 1, 'K': 1,
                              'L': 4, 'M': 2, 'N': 6, 'O': 8, 'P': 2, 'Q': 1, 'R': 6, 'S': 4, 'T': 6, 'U': 4, 'V': 2,
                              'W': 2, 'X': 1, 'Y': 2,'Z': 1}

    def calculate_score(self, word):
        word_score = 0
        if word.isalpha():
            for letter in word.upper():
                if letter in scores_dict:
                    word_score += scores_dict.get(letter)
            return word_score
        else:
            return None

    def tile_hand(self, tile_hand_input):
# This will return a list of 7 letters for the scrabble hard, and can refill hand
        while len(tile_hand_input) != 7 and self.scrabble_pool:
            rand_letter = choice(list(self.scrabble_pool.keys()))
            self.scrabble_pool[rand_letter] = self.scrabble_pool.get(rand_letter) - 1
            if self.scrabble_pool[rand_letter] == 0:
                self.scrabble_pool.pop(rand_letter)
            tile_hand_input.append(rand_letter)
        return tile_hand_input

    def is_valid_word(self, word, word_bank):
        if not word_bank:
            return None
        return word in word_bank

    def shuffle_hand(self, current_hand):
        shuffled_hand = random.sample(current_hand, len(current_hand))
        return current_hand != shuffled_hand

game = ScrabbleGame()
# print(game.shuffle_hand(["A", "B", "C", "D", "E", "F", "G"]))
print(game.tile_hand([]))
