# LISTS (Arrays)

# shopping_list = ["eggs", "sausages", "cheese", "bread"]
# print(shopping_list)
# print(type(shopping_list))
# print(shopping_list[-1])
#
# shopping_list.append("mushrooms")
# print(shopping_list)
#
# shopping_list.remove("cheese")
# print(shopping_list)
# # TWO KINDS OF METHODS, SOME CHANGE THE VALUE, SOME RETURN THE VALUE
#
# pop_return = shopping_list.pop()
# print(shopping_list)
# print(pop_return)

# TUPLES
#
# colours = ("blue", "purple", "turquoise")
# print(colours)
#
# # IMMUTABLE
#
# colours[1] = "red"
# print(colours.count("blue"))
# print(colours.index("purple"))

# DICTIONARIES

my_dict = {"key": "value", "key2": 2} #Keys can be strings and need to be unique, values can be anything
print(my_dict)
print(type(my_dict))

bigger_dictionary = {
    "key1": "value1",
    "key2": "value2",
    "key3": [1, 2, 3, 4]

}

alex_dict = {
    "first_name": "Alex",
    "last_name": "Sam",
    "age": 22,
    "siblings": 3,
    "favourite_food": ["Bacon", "Chicken"]
}

print(alex_dict)

print(my_dict["key"])
my_dict["key"] = "new value"

print(my_dict["key"])
del my_dict["key"]
print(my_dict)

#ORDER DOES NOT MATTER
# KEYS MUST BE UNIQUE, SO CANNOT REFER TO VALUE TO FIND THE KEY
    # CAN REVERSE THE DICTIONARY FOR THIS

print(my_dict.keys())
print(my_dict.values())

data_14 = {"course": "Data 14",
           "trainer": "David Harvey",
           "num_students": 11,
           "location": "Birmingham",
           "start_date_month": "June",
           "trainees": [["Alex", "Sam"], "Anthony McHugh", "Benjamin Seifert", "Charles Weston", "Charlotte Kings", "Danvir Sehmi", "Evie Demetriou"]
           }

print(data_14)
print(data_14["trainees"][0][0][0:1])

for value in data_14:
    if value == "course":
        print(data_14["course"])
    else:
        print("Hello world")
# SET

# car_parts = {"wheels", "doors"}
# print(car_parts)
# print(type(car_parts))
#
# car_parts.add("pedals")
# print(car_parts)
# car_parts.discard("doors")
# print(car_parts)
# SIMILAR TO LISTS, BUT UNORDERED AND CANNOT FIND VALUES FOR THE INDEXES

#FROZEN SET

# fs = frozenset([1, 2, 3, 4])
# print(fs)

#FROZEN SET ARE IMMUTABLE