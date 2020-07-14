from hangman_word import Word
from hangman_diagrams import hangman_diagrams

# Check if input is a letter


def letter_check(prompt):
    is_a_letter = False
    while not is_a_letter:
        user = input(prompt)
        if user.isalpha():
            return user
        else:
            print("Please enter a valid letter!")


# Check if input is a number


def number_check(prompt):
    is_a_number = False
    while not is_a_number:
        user = input(prompt)
        if user == "0":
            print("Don't be silly, pick a number greater than 0!")
        elif user.isnumeric():
            user = int(user)
            return user
        else:
            print("Please enter a valid number!")


# Takes guess from user
def get_user_guess():
    user_input = letter_check("Guess a letter!\n").upper()
    return user_input


def get_user_difficulty():
    user_input = number_check("Please choose a difficulty!  1 = Easy, 2 = Medium, 3 = Hard\n")
    return user_input

# Set - Return True of False depending on if the user wants to play again


def play_again():
    user_play_again = letter_check("Would you like to play again? Y/N\n").upper()
    if user_play_again == "Y":
        return True
    elif user_play_again == "N":
        return False


class Game:

    def __init__(self):
        self.greeting = "WELCOME TO ALEX SAM'S HANGMAN GAME!"
        self.hangman_word = None
        self.guess = None
        self.past_letters = []
        self.lives_left = 6
        self.game_run = False
        self.run()

# This resets all attributes that change during a game
    def reset_game(self):
        self.past_letters = []
        self.hangman_word = Word(get_user_difficulty())
        self.guess = ('_' * self.hangman_word.length)
        self.lives_left = 6

# Helper function: Changing the characters in the guess string with the provided letter
# at the specific indexes in the index_list

    def reveal_letters(self, index_list, replacement_letter):
        for i in range(len(self.guess)):
            if i in index_list:
                self.guess = self.guess[:i] + replacement_letter + self.guess[i + 1:]

# Updates the guess string with correctly guessed letters
    def update_guess(self, user_input):
        for letter in self.hangman_word.word:
            if user_input == letter:
                # Calls a method to get index of the letter/s
                indexes = self.hangman_word.get_index_of_letter(letter)

                # Calls a method from within the class to change letters in self_guess
                self.reveal_letters(indexes, letter)

# Returns True of False depending if the complete guessed word is correct
    def is_correct_word(self):
        if self.guess == self.hangman_word.word:
            print("Congratulations you guessed the word!!!")
            print(self.hangman_word.word)
            return True
        return False

# Handles all instances of user input and following actions
    def handle_user_input(self, user_input):
        if user_input in self.hangman_word.word:
            if user_input not in self.past_letters:
                self.past_letters.append(user_input)
                self.update_guess(user_input)
                print(f"Nice one! You have guessed {user_input} correctly! "
                      f"Be careful, you have {self.lives_left} lives left!")
            elif user_input in self.past_letters:
                print(f"You have already guess {user_input} correctly! Try another letter")

        elif user_input not in self.hangman_word.word:
            if user_input not in self.past_letters:
                self.past_letters.append(user_input)
                self.lives_left -= 1
                print(hangman_diagrams[6 - self.lives_left])
                print(f"{user_input} is not in the word. You have {self.lives_left} lives left!")

            elif user_input in self.past_letters:
                print(f"You have already tried the letter {user_input}! Keep up!")
        else:
            print("Please enter a letter")

        # if user_input in self.hangman_word.word and user_input not in self.past_letters:
        #     self.past_letters.append(user_input)
        #     self.update_guess(user_input)
        #     print(f"Nice one! You have guessed {user_input} correctly! "
        #           f"Be careful, you have {self.lives_left} lives left!")
        #
        # elif user_input in self.hangman_word.word and user_input in self.past_letters:
        #     print(f"You have already guess {user_input} correctly! Try another letter")
        #
        # elif user_input not in self.hangman_word.word and user_input not in self.past_letters:
        #     self.past_letters.append(user_input)
        #     self.lives_left -= 1
        #     print(hangman_diagrams[6-self.lives_left])
        #     print(f"{user_input} is not in the word. You have {self.lives_left} lives left!")
        #
        # elif user_input not in self.hangman_word.word and user_input in self.past_letters:
        #     print(f"You have already tried the letter {user_input}! Keep up!")
        #
        # else:
        #     print("Please enter a letter")

# NB. game_run is in init to help break the while loop
    def run(self):
        while not self.game_run:
            print(f"{self.greeting}")
            self.reset_game()
            print(self.guess)  # This is where the game starts!
            while self.lives_left != 0 and not self.is_correct_word():
                self.handle_user_input(get_user_guess())
                print(f"You have currently guessed {sorted(self.past_letters)}")
                print(self.guess)
            if self.lives_left == 0:
                print(f"Uh oh, looks like you ran out of lives! The word was {self.hangman_word.word} !")
            if not play_again():
                self.game_run = True

