# This is a sample Python script.
from entities.Pokemon import Pokemon

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    mon_pokemon: Pokemon = Pokemon()
    print(" J'entraine mon pokemon ...")
    print("depuis la méthode : ", mon_pokemon.niveau)
    mon_pokemon.monte_niveau()
    print("depuis la méthode : ", mon_pokemon.niveau)
