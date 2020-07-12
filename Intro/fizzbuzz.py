# FIZZBUZZ

# Start at 1
# Print each number in turn
# End at 100

# If divisible by 3, instead of number, "Fizz"
# If divisible by 5, instead of number, "Buzz"
# If divisible by 3 and 5, instead of number, "Fizzbuzz"

# Accept user input for number to count up to? Or change in code?
# Accept user input for number to start from

# Accept user input for custom fizz buzz words
# Change the number we increment by?
# Chang values for fizz buzz

# PEP8 makes python neater


# def valid_num(prompt):
#     while True:
#         try:
#             testing = int(input(prompt))
#             return testing
#         except ValueError:
#             print("This is not a number")


# retrieved_value = valid_num("Enter a number")
# print(retrieved_value)


# This code asks for user input for various numbers
# and tries to catch value errors with a try and except
while True:
    try:
        user_max = int(input("Please enter a number up to 100.\n"))
        if user_max > 100:
            raise Exception
        user_min = int(input("Please enter a number to start.\n"))
        user_interval = int(input("Please enter the increment you would like!\n"))
        user_range = range(user_min, user_max + 1, user_interval)
        break
    except ValueError:
        print("That is not a valid number")
    except Exception:
        print(f"{user_max} is greater than 100!")

# This code stores the buzz number as a key and the
# buzz word as a value
my_dict = {3: "Fizz", 5: "Buzz"}

while True:
    user_prompt = input("Would you like to add another magic word? (Y/N)\n")
    if user_prompt.upper() == "Y":
        magic_word = input("Please enter your magic word!\n")
        try:
            magic_number = int(input("Please enter your magic number!\n"))
        except ValueError:
            print(f"{magic_number} is not a number! Try again :)")
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
    # printed_word = False  # Sets a flag which can be raised
    word_string = ""
    for key in my_dict.keys():
        if num % key == 0:
            word_string += (my_dict.get(key))  # Strings together the buzzwords
            # printed_word = True  # Flag gets raised to prevent double printing
    if word_string != "":  # Ensures no empty strings are printed
        print(word_string)  # Ensures only one string is printed per number in range
    else:
        print(num)
    # elif not printed_word:  # If flag not raised, print number
    #     print(num)

# for num in user_number:
#     printed_word = False
#     string = ""
#     for e, key in enumerate(my_dict.keys()):
#         if num % key == 0:
#             string += (my_dict.get(key))
#             printed_word = True
#         if e == len(my_dict) - 1 and printed_word == True:
#             print(string)
#     # if string != "":
#     #     print(string)
#     if not printed_word:
#         print(num)
