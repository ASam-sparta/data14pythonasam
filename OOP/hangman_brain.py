from hangman_words import word_list
from random import choice


class Word:

    def __init__(self):#, difficulty):
        self.word = choice(word_list)
        self.length = len(self.word)
        #self.difficulty = difficulty
        self.easy = [8, 9]
        self.medium = [10,11]
        self.hard = [12, 13, 14, 15]
        self.dict = {1: self.easy, 2: self.medium, 3: self.hard}

# Getter: Returns a list of indexes where "letter_to_find" is found in self.word
    # - self.word is a property of the current object
    def get_index_of_letter(self, letter_to_find):
        indexes = []
        letter_to_find = letter_to_find.upper()
        for index_search in range(self.length):
            if letter_to_find == self.word[index_search]:
                indexes.append(index_search)
        return indexes

    # def generate_word(self):
    #     picked_word = choice(word_list)
    #     while len(picked_word) not in self.dict[self.difficulty]:
    #         picked_word = choice(word_list)
    #     return picked_word


# new_word = Word()
# print(new_word.get_index_of_letter("l"))
# # print(f"{new_word.word} {str(new_word.length)} {new_word.first_letter}")
# user_input = input("Choose a word")
# # P
#
# print(new_word.word)
# print(new_word.get_letter(5))