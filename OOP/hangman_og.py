from hangman_word import Word
# Counter for lives
# Show the letters that have been guessed wrongly
# Show letters that have been guessed correctly
# Show the position of these letters
# Ensure message during repeat letter
# Allow to play again
#
class HangmanGame:


new_word = Word()
# print(f"{new_word.word} {str(new_word.length)} {new_word.first_letter}")
# print(f"The length of the word is {new_word.length}")
#
# print("_ " * new_word.length)
new_word = Word().word
guess = ('_' * new_word.length)
print(guess)


def get_index_of_letter(letter_searched, word):
    indexes = []
    for index_search in range(len(word)):
        if letter_searched == word[index_search]:
            indexes.append(index_search)
    return indexes

# Replaces letter at the index specified


def replace_letter_at_index(index_list, letter_in_word, word):
    for i in range(len(word)):
        if i in index_list:
            word = word[:i] + letter_in_word + word[i + 1:]
    return word


x = 0
correct_word = False
while not correct_word and x < 10:
    user_input = input("Guess a letter!\n")
    if user_input.upper() in new_word:
        print(user_input.upper())
        for letter in new_word:
            if user_input.upper() == letter:
                indexes = get_index_of_letter(letter, new_word)
                guess = replace_letter_at_index(indexes, letter, guess)
                print(guess)
                if guess == new_word:
                    correct_word = True
    else:
        x += 1
        print(f"You have {10-x} lives left!")
        continue