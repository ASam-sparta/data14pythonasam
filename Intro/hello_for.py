# FOR LOOPS

# shopping_list = ["eggs", "bacon", "bread"]
# favourite_colours = ["yellow", "purple", "turquoise"]
#
# for item in shopping_list:
#     for colour in favourite_colours:
#         print(colour, item)
#
dict_data = {
    1: {"name": "Alex", "animal": "all dogs"},
    2: {"name": "Ben", "animal": "flamingo"},
    3: {"name": "Evie", "animal": "gorilla"},
    4: {"name": "Charlotte", "animal": "giraffe"}
}

for key in dict_data:
    string = ""
    for inner_key in dict_data[key]:
        string += (dict_data[key][inner_key])
    print(string)
#
for key in dict_data:
    print(f"{dict_data[key]['name']}'s favourite animal is {dict_data[key]['animal']}")

# CHINESE MENU
chinese_menu = {
    101: {'dish': 'egg fried rice', 'price': 1.60, 'rating': 4.5},
    102: {'dish': 'chicken chow mein', 'price': 5.50, 'rating': 3.9},
    103: {'dish': 'beef brisket curry', 'price': 6.50, 'rating': 4.9},
    104: {'dish': 'cantonese roast duck', 'price': 12.50, 'rating': 5.0},
    106: {'dish': 'wonton noodle', 'price': 7.50, 'rating': 3.3},
}

for item in chinese_menu:
    if chinese_menu[item]['price'] < 10:
        print("This is less than £10!! Bargain!!")
    else:
        print("This is too expensive!!")

