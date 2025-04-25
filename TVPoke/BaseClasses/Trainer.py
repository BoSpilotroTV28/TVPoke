import importlib

class Trainer:
    def __init__(self, pokemon, i):
        self.pokemon = []
        self.name = "Player " + str(i)
        for poke in pokemon:
            pokeFile = importlib.import_module("TVPoke.Pokemon." + poke)
            PokeClass = getattr(pokeFile, poke)
            self.pokemon.append(PokeClass())

    def removeFaintedPokemon(self):
        for poke in self.pokemon:
            if poke.hp <= 0:
                self.pokemon.remove(poke)