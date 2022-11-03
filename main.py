# This is a sample Python script.
from entities.Pokemon import Pokemon


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    mon_pokemon: Pokemon = Pokemon('pikachu', 'electrique', 'docile', 10)
    print(mon_pokemon.nom)
