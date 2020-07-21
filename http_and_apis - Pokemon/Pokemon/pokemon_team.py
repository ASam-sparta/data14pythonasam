from Pokemon.pokemon_generator import SinglePokemon
from Pokemon.pokemon_model import Pokemon
from Pokemon.pokemon_moves import PokemonMoves
from pprint import pprint
from random import randint

#This class generates a random team of pokemon with random moves, to be used in a pokemon battle
class PokemonTeam:

    def __init__(self):
        self.pok1()
        self.pok2()
        self.pok3()
        self.pok4()
        self.pok5()
        self.pok6()
        self.pokemon_team = [self.pok1().response_json['name'], self.pok2().response_json['name'], self.pok3().response_json['name'],
                             self.pok4().response_json['name'], self.pok5().response_json['name'], self.pok6().response_json['name']]


    def pok1(self):
        pok1 = SinglePokemon(str(randint(1, 151)))
        return pok1

    def pok2(self):
        pok1 = SinglePokemon(str(randint(1, 151)))
        return pok1

    def pok3(self):
        pok1 = SinglePokemon(str(randint(1, 151)))
        return pok1

    def pok4(self):
        pok1 = SinglePokemon(str(randint(1, 151)))
        return pok1

    def pok5(self):
        pok1 = SinglePokemon(str(randint(1, 151)))
        return pok1

    def pok6(self):
        pok1 = SinglePokemon(str(randint(1, 151)))
        return pok1

pk_team = PokemonTeam()
print(f"Your randomly generated team is {pk_team.pokemon_team} !")