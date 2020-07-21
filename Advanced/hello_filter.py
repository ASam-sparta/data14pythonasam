students = ["DAVID", "Lee", "HARVEY"]

result = filter(str.isupper, students)

print(list(result))

# Write a function that returns true if a
# number is even and divisible by 3


def even_div(num):
    return num % 3 == 0 and num % 2 == 0


print(even_div(9))

numbers = list(range(1, 100))
result2 = filter(even_div, numbers)

print(list(result2))

# Make a function to return true if the length of the
# is within a range