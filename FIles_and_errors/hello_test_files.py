# file = open("order.txt") # This connects to a file stream
# Syntax is the grammar of python

# ZeroDivision error
# Indentation error
# Name error
# ModuleNotFound error
# Syntax error - UnexpectedEOF - end of file
# Type error
# Key error
# Attribute error - i.e. strings do not have methods
# Index error
# IO error
# Value error
# Recursion error

# try:
#     print("Trying to open file...")
#     file = open("order.txt")
# except FileNotFoundError as err:
#     print("Couldn't open the file! PANIC!")
#     print(err)  # Prints error message
# finally:
#     print("This is the end of the file")


# READ FILE

# r - Read mode (default)
# w - Write mode (if no file, creates one; if file, truncate)
# x - Create mode
# a - append mode (if no file, create one; if file, appends)
# t - text mode
# b - binary mode
# + - reading and writing

# def open_and_print_file(filename):
#     try:
#         opened_file = open(filename, "r")
#         file_line_list = opened_file.readlines()
#
#         for line in file_line_list:
#             print(line.rstrip('\n'))  # Strips a new line in the order.txt
#
#         opened_file.close() # Remember to close it!!!
#
#     except FileNotFoundError:
#         print("File cannot be found, please check filename provided")
#         raise
#
# file = open("order.txt")
#
# order_lines = file.readlines() # This shows the \n lines
# print(order_lines)

# ENSURE YOU ASSIGN THE LINES OR THE DATA WILL DISAPPEAR


# DAVID METHOD

def open_and_print_file(filename):
    try:
        with open("order.txt") as opened_file:
            file_line_list = opened_file.readlines()

            for line in file_line_list:
                print(line.rstrip('\n'))

    except FileNotFoundError:
        print("File cannot be found, please check filename provided")
        raise

with open("order.txt", "w") as opened_file:
    opened_file.write("Cheeseburger")

def append_to_file(filename, order):
    try:
        with open(filename, "a") as opened_file:
            opened_file.write(order + '\n')

    except TypeError:
        print("Order needs to be a string")

append_to_file("order.txt", "Pasta")
append_to_file("order.txt", "Hotdog")
append_to_file("order.txt", "Chow mein")
