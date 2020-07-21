def valid_num(prompt):
    while True:
        try:
            valid = int(input(prompt))
            return valid
        except ValueError:
            print("This is not a number")


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
    user_prompt = input("Would you like to add another word? (Y/N)\n")
    if user_prompt.upper() == "Y":
        magic_word = input("Please enter your word!\n")
        try:
            magic_number = int(input("Please enter the number for this word!\n"))
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
    word_string = ""
    for key in my_dict.keys():
        if num % key == 0:
            word_string += (my_dict.get(key))  # Strings together the buzzwords
    if word_string != "":  # Ensures no empty strings are printed
        print(word_string)  # Ensures only one string is printed per number in range
    else:
        print(num)
