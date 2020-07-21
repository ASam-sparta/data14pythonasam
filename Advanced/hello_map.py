data14 = ["Katie", "Juxhen", "Joe"]

# for name in range(len(data14)):
#     data14[name] = data14[name].upper()
#
# print(data14)

# Map applies a function to an iterable
data14_upper = map(str.upper, data14)

print(list(data14_upper))


# Write a function that squares a number and adds 3


def square_num_add_three(num, add):
    new_num = num ** 2 + add
    return new_num


numbers = [1, 2, 3, 4, 5] # If list is longer then it stops
adds = [10, 100, 1000]

num_map = map(square_num_add_three, numbers, adds)
print(list(num_map))

