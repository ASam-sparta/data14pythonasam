# import random
from random import choice
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
scores_dict = {'A': 1, 'B': 3, 'C': 3, 'D': 2, 'E': 1, 'F': 4, 'G': 2, 'H': 4, 'I': 1, 'J': 8, 'K': 5, 'L': 1, 'M': 3,
               'N': 1, 'O': 1, 'P': 3, 'Q': 10, 'R': 1, 'S': 1, 'T': 1, 'U': 1, 'V': 4, 'W': 4, 'X': 8, 'Y': 4, 'Z': 10}

class ScrabbleGame():

    def calculate_score(self, word):
        word_score = 0
        if word.isalpha():
            for letter in word.upper():
                if letter in scores_dict:
                    word_score += scores_dict.get(letter)
            return word_score
        else:
            return None

    def generate_tile_hand(self):
        tile_hand = []
        for num in range(0, 7):
            tile_hand.append(choice(alphabet))
        return tile_hand

    def is_valid_word(self, word, word_bank):
        if not word_bank:
            return None
        return word in word_bank

    def replace_tiles(self, tile_hand_input):
        if len(tile_hand_input) != 7:
            tile_hand_input.append(choice(alphabet))
        return tile_hand_input
