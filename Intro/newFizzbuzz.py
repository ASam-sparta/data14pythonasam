def valid_input(prompt):
    valid = False
    while not valid:
        user_input = input(prompt)
        if user_input.isnumeric():
            user_input = int(user_input)
            valid = True
            return user_input
        else:
            print("This is not a number. Please try again!")

# This code asks for user input for various numbers
# and tries to catch value errors with a try and except


user_max = valid_input("Please enter a number up to 100.\n")
user_min = valid_input("Please enter a number to start.\n")
user_interval = valid_input("Please enter the increment you would like!\n")
user_range = range(user_min, user_max + 1, user_interval)

first_word = input("Please enter a word for fizz!")
first_num = valid_input(f"Please enter a number for {first_word}!")
second_word = input("Please enter a word for buzz!")
second_num = valid_input(f"Please enter a number for {second_word}!")

# def fizz_buzz(first_combo):
#     first_word, first_num = first_combo.split()
#     first_num = int(first_num)
#     return first_word, first_num
#
#
# print(fizz_buzz("fizz 3"))

def fizz_buzz(userrange, word1, num1, word2, num2):
    for num in userrange:
        if num % num1*num2 == 0:
            return word1 + word2
        if num % num1 == 0:
            return word1
        elif num % num2 == 0:
            return word2


print(fizz_buzz(user_range, first_word, first_num, second_word, second_num))