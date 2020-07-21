import requests
from pprint import pprint

# This creates a class of each pokemon moves

class PokemonMoves:

    def __init__(self, moves_json):
        self.accuracy = moves_json['accuracy']
        self.damage_class = moves_json['damage_class']
        self.effect_chance = moves_json['effect_chance']
        self.effect_entries = moves_json['effect_entries']
        # self.short_effect = self.effect_entries['short_effect']
        self.generation = moves_json['generation']
        self.id = moves_json['id']
        self.machines = moves_json['machines']
        self.meta = moves_json['meta']
        self.name = moves_json['name']
        self.power = moves_json['power']
        self.pp = moves_json['pp']
        self.priority = moves_json['priority']
        self.stat_changes = moves_json['stat_changes']
        self.target = moves_json['target']
        self.type = moves_json['type']

# url = "https://pokeapi.co/api/v2/move/144/"
# request = requests.get(url)
# header_details = request.headers
# response_json = request.json()
#
# pprint(response_json)


# url = "https://pokeapi.co/api/v2/stat/2"
# request = requests.get(url)
# header_details = request.headers
# response_json = request.json()
#
# pprint(response_json)