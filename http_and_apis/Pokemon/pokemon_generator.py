import requests
from Pokemon.pokemon_model import Pokemon
# from config_manager import base_url


# This model processes the data, i.e. retrieves all the information from API
class SinglePokemon:

    def __init__(self, pokemon_name):
        self.url = "https://pokeapi.co/api/v2/pokemon/" + pokemon_name
        self.request = requests.get(self.url)
        self.header_details = self.request.headers
        self.response_json = self.request.json()
        self.level = 100
        self.hp = 110 + 2 * Pokemon(self.response_json).hp
        self.attack = 5 + 2 * Pokemon(self.response_json).attack
        self.defense = 5 + 2 * Pokemon(self.response_json).defense
        self.special_attack = 5 + 2 * Pokemon(self.response_json).special_attack
        self.special_defense = 5 + 2 * Pokemon(self.response_json).special_defense
        self.speed = 5 + 2 * Pokemon(self.response_json).speed

    def response(self):
        return Pokemon(self.response_json)

    def stats(self):
        return f"HP: {self.hp} \nATK: {self.attack} \nDEF: {self.defense} \nSP.ATK: {self.special_attack} " \
               f"\nSP.DEF: {self.special_defense} \nSPD: {self.speed}"

pokemon_ditto = SinglePokemon("rayquaza")

print(pokemon_ditto.stats())

# Randomly generate moves for the pokemon based on what they can learn
# Make a pokemon team class
# Make a battle system