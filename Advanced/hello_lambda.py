# Lambda

# A way to do anonymous functions


def add(n1, n2):
    return n1 + n2


print(add(2, 2))

add_lambda = lambda n1, n2: n1 + n2

print(add_lambda(2, 2))

numbers = [101, 2034, 2, 282, 3]

result = map(lambda x: x ** 2 + 3, numbers)
print(list(result))

# Use lambda is map AND filter

savings = [234.00, 555.00, 674.00, 78.00]

# In a new list called bonus,
# savings with 10% added

bonus = list(map(lambda x: round(x*1.1, 2), savings))

print(bonus)

# In a new list called even savings
# keep only savings amounts that are even

even_savings = list(filter(lambda x: x % 2 == 0, savings))

print(even_savings)