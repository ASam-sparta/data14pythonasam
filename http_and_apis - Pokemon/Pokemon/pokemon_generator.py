import requests
from Pokemon.pokemon_model import Pokemon
from Pokemon.pokemon_moves import PokemonMoves
from random import choice


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

    def stats(self):
# This shows all the stats for a single pokemon
        hp = 110 + 2 * Pokemon(self.response_json).hp
        attack = 5 + 2 * Pokemon(self.response_json).attack
        defense = 5 + 2 * Pokemon(self.response_json).defense
        special_attack = 5 + 2 * Pokemon(self.response_json).special_attack
        special_defense = 5 + 2 * Pokemon(self.response_json).special_defense
        speed = 5 + 2 * Pokemon(self.response_json).speed
        return f"HP: {hp} \nATK: {attack} \nDEF: {defense} \nSP.ATK: {special_attack} " \
               f"\nSP.DEF: {special_defense} \nSPD: {speed}"


    def move_generator_function(self):
# This generates a random move that the pokemon can learn and all its relative attributes needed for a pokemon battle
        while True:
            move1 = choice(Pokemon(self.response_json).moves)['move']
            move1_name = (move1['name']).capitalize()
            move1_address = move1['url']
            request = requests.get(move1_address)
            response_json = request.json()
            testing = PokemonMoves(response_json)
            if testing.power is not None:
                return {'name': move1_name.capitalize(), 'type': testing.type['name'], 'pp': testing.pp, 'power': testing.power,
                        'damage_class': testing.damage_class['name'], 'accuracy': testing.accuracy}

    def moveset(self):
# This returns a list of moves that are unique
        move_list = [self.move_generator_function()]
        name_list = [move_list[0]['name']]
        x = 0
        while x < 3:
            move = self.move_generator_function()
            for i in range(len(move_list)):
                if move['name'] not in name_list:
                    move_list.append(move)
                    name_list.append(move['name'])
            x += 1
        return move_list


# pokemon_ditto = SinglePokemon("dialga")
#
# pprint(pokemon_ditto.moveset())

# Randomly generate moves for the pokemon based on what they can learn - done
# Make a pokemon team class
# Make a battle system
# Import moves api