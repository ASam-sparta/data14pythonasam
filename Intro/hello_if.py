# CONTROL FLOW
# age = 18
# x= 4
# if age > 18:
#     print("You can see the scary film")
#     x = x+1
#     print(x)
# elif age == 18:
#     print("You are just about old enough")
# else:
#     print("You are not old enough")
#
# # U, PG, 12A, 15, 18
#
# U = "suitable for all age groups"
# PG = "Requires parental guidance"

# x = input("What is the film rating?\n")
# x = x.upper()
#
# if x == "U":
#     print("Suitable for all age groups")
# elif x == "PG":
#     print("Requires parental guidance")
# elif x == "12A" or x == "12":
#     print("Suitable for viewers over 12")
# elif x == "15":
#     print("Suitable for viewers over 15")
# elif x == "18":
#     print("Suitable for viewers over 18")
# else:
#     print("Please enter a valid rating")

ratings = {
    "PG": "Parental Guidance advised",
    "12A": "Under 12s must be accompanied by adult",
    "15": "Suitable for viewers over 15",
    "18": "Suitable for viewers over 18",
    "U": "Suitable for all ages"
}

x = "U"
if x == ratings.keys():
    print(ratings[value])