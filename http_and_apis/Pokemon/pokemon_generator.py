import requests
from Pokemon.pokemon_model import Pokemon
from Pokemon.pokemon_moves import PokemonMoves
from random import choice
from pprint import pprint
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
        self.move1 = choice(Pokemon(self.response_json).moves)['move']['name']
        self.move2 = choice(Pokemon(self.response_json).moves)['move']['name']
        self.move3 = choice(Pokemon(self.response_json).moves)['move']['name']
        self.move4 = choice(Pokemon(self.response_json).moves)['move']['name']

    def pokemon_response(self):
        return Pokemon(self.response_json)

    def pokemon_move_response(self):
        return PokemonMoves()

    def stats(self):
        return f"HP: {self.hp} \nATK: {self.attack} \nDEF: {self.defense} \nSP.ATK: {self.special_attack} " \
               f"\nSP.DEF: {self.special_defense} \nSPD: {self.speed}"

    def moveset(self):
        return

pokemon_ditto = SinglePokemon("rayquaza")

pprint(pokemon_ditto.move1.move2.move3.move4)

# Randomly generate moves for the pokemon based on what they can learn - done
# Make a pokemon team class
# Make a battle system
# Import moves api