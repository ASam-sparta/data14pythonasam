from hangman_word import Word

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


class Game:

    def __init__(self):
        self.hangman_word = Word()
        self.guess = ('_' * self.hangman_word.length)
        self.entered_letters = []
        self.run()
        self.lives_left = 0

# Setter: Changing the characters in self.guess with the provided replacement_letter
#         at the specific indexes in the index_list
    def reveal_letters(self, index_list, replacement_letter):
        for i in range(len(self.guess)):
            if i in index_list:
                self.guess = self.guess[:i] + replacement_letter + self.guess[i + 1:]

    # def guess_correct_word(self):
    #     if self.guess == self.hangman_word.word:
    #         print("Congratulations you guessed the word!!!")
    #         print(self.hangman_word.word)
    #         correct_word = True
    #         user_play_again = letter_check("Would you like to play again? Y/N\n").upper()
    #         if user_play_again == "Y":
    #             self.entered_letters = []
    #             Game()
    #             self.guess = ('_' * self.hangman_word.length)
    #             self.run()
    #         elif user_play_again == "N":
    #             break


# This runs the game with user inputs

    def run(self):
        game_run = False
        while not game_run:
            print("You have decided to play hangman... good luck!")
            self.lives_left = number_check("How many lives would you like?\n")
            while True:
                correct_word = False
                print(self.guess)
                if self.lives_left == 0:
                    print("Uh oh, looks like you ran out of lives!")
                    user_play_again = letter_check("Would you like to play again? Y/N\n").upper()
                    if user_play_again == "Y":
                        self.guess = ('_' * self.hangman_word.length)
                        self.entered_letters = []
                        Game()
                        correct_word = True
                    elif user_play_again == "N":
                        game_run = True
                        break

                while not correct_word and self.lives_left != 0:
                    user_input = letter_check("Guess a letter!\n").upper()

                    # Checks if entered letter matched any letters of the hangman word and the guessed letter list
                    if user_input in self.hangman_word.get_word() and user_input not in self.entered_letters:
                        self.entered_letters.append(user_input)
                        print(f"Nice one! You have guessed {user_input} correctly! "
                              f"Be careful, you have {self.lives_left} lives left!")

                        # If matching letter, checks through each letter in the word and also
                        # checks if the user_input matches the letter
                        for letter in self.hangman_word.get_word():
                            if user_input == letter:

                                # Calls a method to get index of the letter/s
                                indexes = self.hangman_word.get_index_of_letter(letter)

                                # Calls a method from within the class to change letters in self_guess
                                self.reveal_letters(indexes, letter)
                                # self.guess_correct_word()
                                if self.guess == self.hangman_word.get_word():
                                    print("Congratulations you guessed the word!!!")
                                    print(self.hangman_word.get_word())
                                    correct_word = True
                                    user_play_again = letter_check("Would you like to play again? Y/N\n").upper()
                                    if user_play_again == "Y":
                                        self.entered_letters = []
                                        Game()
                                        self.guess = ('_' * self.hangman_word.length)
                                        self.run()
                                    elif user_play_again == "N":
                                        break

                    elif user_input in self.hangman_word.get_word() and user_input in self.entered_letters:
                        print(f"You have already guess {user_input} correctly! Try another letter")
                    elif user_input not in self.hangman_word.get_word() and user_input not in self.entered_letters:
                        self.entered_letters.append(user_input)
                        self.lives_left -= 1
                        print(f"{user_input} is not in the word. You have {self.lives_left} lives left!")
                    elif user_input not in self.hangman_word.get_word() and user_input in self.entered_letters:
                        print(f"You have already tried the letter {user_input.upper()}! Keep up!")
                    else:
                        print("Please enter a letter")

                    print(f"You have currently guessed {sorted(self.entered_letters)}")
                    print(self.guess)