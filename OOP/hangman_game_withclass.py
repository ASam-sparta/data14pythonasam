from hangman_brain import Word

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
        if user.isnumeric():
            user = int(user)
            return user
        else:
            print("Please enter a valid number!")


# Takes guess from user
def get_user_guess():
    user_input = letter_check("Guess a letter!\n").upper()
    return user_input


class Game:

    def __init__(self):
        self.greeting = "Welcome to Hangman... good luck!"
        self.hangman_word = Word()
        self.guess = ('_' * self.hangman_word.length)
        self.entered_letters = []
        self.lives_left = 0
        self.active_game = True
        self.game_run = False
        self.run()
# Setter: Changing the characters in self.guess with the provided replacement_letter
#         at the specific indexes in the index_list

    def reveal_letters(self, index_list, replacement_letter):
        for i in range(len(self.guess)):
            if i in index_list:
                self.guess = self.guess[:i] + replacement_letter + self.guess[i + 1:]

# Set self.guess to a new string
    def update_guess(self, user_input):
        for letter in self.hangman_word.word:
            if user_input == letter:
                # Calls a method to get index of the letter/s
                indexes = self.hangman_word.get_index_of_letter(letter)

                # Calls a method from within the class to change letters in self_guess
                self.reveal_letters(indexes, letter)

# Returns True of False depending if the complete guessed word is correct
    def correct_word(self):
        if self.guess == self.hangman_word.word:
            print("Congratulations you guessed the word!!!")
            print(self.hangman_word.word)
            self.active_game = False
            self.play_again()
            return True
        return False

# Set - Prompt user to play again
    def play_again(self):
        user_play_again = letter_check("Would you like to play again? Y/N\n").upper()
        if user_play_again == "Y":
            self.entered_letters = []
            self.hangman_word = Word()
            self.guess = ('_' * self.hangman_word.length)
            self.active_game = False
        elif user_play_again == "N":
            self.active_game = False
            self.game_run = True

    def handle_user_input(self, user_input):

        if user_input in self.hangman_word.word and user_input not in self.entered_letters:
            self.entered_letters.append(user_input)
            self.update_guess(user_input)
            print(f"Nice one! You have guessed {user_input} correctly! "
                  f"Be careful, you have {self.lives_left} lives left!")
        elif user_input in self.hangman_word.word and user_input in self.entered_letters:
            print(f"You have already guess {user_input} correctly! Try another letter")
        elif user_input not in self.hangman_word.word and user_input not in self.entered_letters:
            self.entered_letters.append(user_input)
            self.lives_left -= 1
            print(f"{user_input} is not in the word. You have {self.lives_left} lives left!")
        elif user_input not in self.hangman_word.word and user_input in self.entered_letters:
            print(f"You have already tried the letter {user_input}! Keep up!")
        else:
            print("Please enter a letter")

    def run(self):
        while not self.game_run:
            print("You have decided to play hangman... good luck!")
            self.lives_left = number_check("How many lives would you like?\n")
            # print(self.hangman_word.word)
            print(self.guess)
            self.active_game = True # This is set to false in the play_again method and this resets the flag so that the game can begin
            while self.active_game:
                if self.lives_left == 0:
                    print("Uh oh, looks like you ran out of lives!")
                    self.play_again()
                else:
                    while self.lives_left != 0 or self.correct_word():
                        self.handle_user_input(get_user_guess())
                        print(f"You have currently guessed {sorted(self.entered_letters)}")
                        print(self.guess)