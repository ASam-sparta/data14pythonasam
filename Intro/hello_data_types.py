# # NUMBERS
#
# #   Float, integer, complex
#
# # a = complex(2, 3)
# # a = 3+2j
#
#
# # # STRINGS
# # single_inside = "I'm using double quotes for single quotes"
# # print(single_inside)
# #
# # slash = 'I\'m using single quotes'
# # print(slash)
#
# # Python starts counting at 0 for indices
# # print(hw[3:7]) up to and not including 7
# # Python treats strings as list
# # print(len(hw))
#
# #STRING METHODS AND FUNCTIONS
#
# white_space = "        white space       "
# print(white_space.strip())
# print(white_space.lstrip())
# print(white_space.rstrip())
#
# print(white_space.count(" "))
# print(white_space.count("e"))
#
# print(white_space.lower())
# print(white_space.upper())
# print(white_space.capitalize())
# print(white_space.replace("e", "eeeeeeee"))
#
# print(white_space.strip().capitalize())
#
# # FORMATTED STRING ala SUBSTITUTION
# a = "hello"
# b = "there"
# c = "alex"
# d = 4
# print(f"{a}, {b}, {c}, {d}")

# Name, age, number of sibling, favourite decimal number, favourite animal
name = str(input("What is your name?\n"))
age = int(input("How old are you?\n"))
num_sib = input("How many siblings do you have?\n")
fav_dec = float(input("What is your favourite decimal number?\n"))
fav_ani = input("What is your favourite animal?\n")
print(f"Hello, your name is {name} and you are {age} years old. "
      f"You have {num_sib} siblings and you favourite decimal is {fav_dec}. Finally, your favourite animal is a {fav_ani}!")