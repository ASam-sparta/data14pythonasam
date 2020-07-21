# def valid_num(prompt):
#     # while True:
#         try:
#             valid = int(input(prompt))
#             if valid > 100:
#                 raise Exception
#             return valid
#         except ValueError:
#             print("This is not a number")
#         except Exception:
#             print(f"{valid} is greater than 100! Try again :)")


def valid_int_input(prompt):
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


user_max = valid_int_input("Please enter a number up to 100.\n")
user_min = valid_int_input("Please enter a number to start.\n")
greater_than = False
while not greater_than:
    if user_max > user_min:
        greater_than = True
    elif user_max < user_min:
        print(f"Please enter a starting number less than {user_max}")

user_interval = valid_int_input("Please enter the increment you would like!\n")
user_range = range(user_min, user_max + 1, user_interval)



# This code stores the buzz number as a key and the
# buzz word as a value
my_dict = {3: "Fizz", 5: "Buzz"}

while True:
    user_prompt = input("Would you like to add another word? (Y/N)\n")
    if user_prompt.upper() == "Y":
        magic_word = input("Please enter your word!\n")
        magic_number = valid_int_input(f"Please enter the number for this {magic_word}!\n")
        my_dict[magic_number] = magic_word  # Updates dictionary with new variable
        print(my_dict)
    elif user_prompt.lower() == "n":
        print(my_dict.values())
        break
    else:
        print("Please enter Y for Yes or N for No")

# This code checks if each number is divisible
# by each key and returns the associated word

for num in user_range:
    word_string = ""
    for key in my_dict.keys():
        if num % key == 0:
            word_string += (my_dict.get(key))  # Strings together the buzzwords
    if word_string != "":  # Ensures no empty strings are printed
        print(word_string)  # Ensures only one string is printed per number in range
    else:
        print(num)



