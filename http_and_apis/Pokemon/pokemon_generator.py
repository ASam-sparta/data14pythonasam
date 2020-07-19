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
        self.moveset()
        self.stats()

    def pokemon_response(self):
        return Pokemon(self.response_json)

    # def pokemon_move_response(self):
    #     return PokemonMoves(https://pokeapi.co/api/v2/move/144/)

    def stats(self):
        hp = 110 + 2 * Pokemon(self.response_json).hp
        attack = 5 + 2 * Pokemon(self.response_json).attack
        defense = 5 + 2 * Pokemon(self.response_json).defense
        special_attack = 5 + 2 * Pokemon(self.response_json).special_attack
        special_defense = 5 + 2 * Pokemon(self.response_json).special_defense
        speed = 5 + 2 * Pokemon(self.response_json).speed
        return f"HP: {hp} \nATK: {attack} \nDEF: {defense} \nSP.ATK: {special_attack} " \
               f"\nSP.DEF: {special_defense} \nSPD: {speed}"

    def moveset(self):
        move1 = (choice(Pokemon(self.response_json).moves)['move']['name']).capitalize()
        move2 = (choice(Pokemon(self.response_json).moves)['move']['name']).capitalize()
        move3 = (choice(Pokemon(self.response_json).moves)['move']['name']).capitalize()
        move4 = (choice(Pokemon(self.response_json).moves)['move']['name']).capitalize()
        return f"{move1} \n{move2} \n{move3} \n{move4}"

    def move1(self):
        address =
pokemon_ditto = SinglePokemon("rayquaza")

pprint(pokemon_ditto.response_json)

# Randomly generate moves for the pokemon based on what they can learn - done
# Make a pokemon team class
# Make a battle system
# Import moves api