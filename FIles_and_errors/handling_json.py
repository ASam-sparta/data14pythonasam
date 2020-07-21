import json
# from pprint import pprint
#
# with open("film.json", "r") as jsonfile:
#     film = json.load(jsonfile)
#
# pprint(film) # This prints this in alphabetical order

film = {
    "Title": "The Godfather",
    "length_in_min": 178,
    "Release Date": 1972,
    "Cast": {
        "Marlon Brando": "Vito Corleone",
        "Al Pacino": "Michael Corleone"}
}

# print(film)
# print(json.dumps(film))  # dumps outputs a string
#
# with open("godfather.json", "w") as jsonfile:
#     json.dump(film, jsonfile)  # dump writes it to a file

# Define a class
# Store same attributes as defined in json
# Read your jason file
# Create an instance of the film class
# for your film

class Film:
    def __init__(self, title, length, year):
        self.title = title
        self.length_in_min = length
        self.release_year = year
        self.cast = {
                        "Marlon Brando": "Vito Corleone",
                        "Al Pacino": "Michael Corleone",
                        "Robert Duvall": "Tom Hagen"
                    },
        self.genre = ["Crime film", "Mafia"]
        self.screenplay = ["Mario Puzo", "Francis Ford Coppola"]
        self.music_by = "Nino Rota"

with open("film.json", "r") as jsonfile:
    film = json.load(jsonfile)  # There is also loads (loads as string) and load
    print(film)

new_film = Film()
print(new_film.title)