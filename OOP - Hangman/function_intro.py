# Don't
# Repeat
# Yourself


# def print_something():
#     print("Something!")
#
#
# print_something()
#
# # Functions require arguments, and these are dynamic
# # aka string/int based on the input
#
#
# def print_something_multiple(some_string, number_of_times):
#     string_to_print = some_string * number_of_times
#     print(string_to_print)
#
#
# print_something_multiple("Woohoo!", 3)
#
# PUT DEFAULT/DEFINED VALUES AT THE END OR IT WONT KNOW
# WHICH VARIABLE IT IS and specify which parameter is changing
#
# CAN ALSO SET THE ARGUMENTS TO SPECIFIC DATA TYPES
# BUT THIS IS NOT HARD CODED
# This clutters the screen but makes reading code easier
def repeat_string(string_to_repeat: str, number_of_repeats: int = 3) -> str:
    string_to_return = string_to_repeat * number_of_repeats
    return string_to_return


print(repeat_string("Boohoowoo!").capitalize())


# def addition(num1, num2):
#     return num1 + num2
#
#
# add_num = addition(3, 5)
# print(add_num)

#MULTIPLE ARGUMENTS
# def find_product(*multiargs):
#     numbers = [*multiargs]
#     result = numbers[0]
#     length = len(numbers)
#     for index in range(1, length):
#         result *= numbers[index]
#     return result



# def find_product(*multiargs):
#     # Return the product (all numbers multiplied together)
#     if len(multiargs) < 1:
#         return None
#     else:
#         product = 1
#         for number in multiargs:
#             product = product * number
#         return product

# print(find_product(1, 2, 3, 4, 5, 6))

# Look at fizz buzz code, fizz buzz function that will run the main fizz buzz game
# Look at what else you can fucntionise