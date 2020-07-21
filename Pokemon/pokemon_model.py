# import requests
# from pprint import pprint

# This creates a pokemon

class Pokemon:

    def __init__(self, pokemon_json):
        self.abilities = pokemon_json['abilities']
        self.base_experience = pokemon_json["base_experience"]
        self.forms = pokemon_json['forms']
        self.game_indices = pokemon_json['game_indices']
        self.height = pokemon_json['height']
        self.held_items = pokemon_json['held_items']
        self.id = pokemon_json['id']
        self.is_default = pokemon_json['is_default']
        self.location_area_encounters = pokemon_json['location_area_encounters']
        self.moves = pokemon_json['moves']
        self.name = pokemon_json['name']
        self.order = pokemon_json['order']
        self.species = pokemon_json['species']
        self.sprites = pokemon_json['sprites']
        self.stats = pokemon_json['stats']
        self.hp = self.stats[0]['base_stat']
        self.attack = self.stats[1]['base_stat']
        self.defense = self.stats[2]['base_stat']
        self.special_attack = self.stats[3]['base_stat']
        self.special_defense = self.stats[4]['base_stat']
        self.speed = self.stats[5]['base_stat']
        self.types = pokemon_json['types']
        self.weight = pokemon_json['weight']

#
# url = "https://pokeapi.co/api/v2/pokemon/ditto"
# request = requests.get(url)
# header_details = request.headers
# response_json = request.json()
#
# pprint(response_json)


