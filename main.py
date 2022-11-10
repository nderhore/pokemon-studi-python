# This is a sample Python script.
from entities.Salameche import Salameche
from entities.Pokemon import Pokemon
from service.DatabaseService import DatabaseService

# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    #Creation d'un pokemon
    #mon_pokemon: Pokemon = Pokemon()
    #print("J'entraine mon pokemon ...")
    #print("depuis la méthode : ", mon_pokemon.niveau)
    #mon_pokemon.monte_niveau()
    #print("depuis la méthode : ", mon_pokemon.niveau)

    #Creation d'un salameche
    list_capacities : list = ['griffe','rugissement','flammeche','toto']
    mon_salameche : Salameche = Salameche(Salameche.__name__,list_capacities)
    print(mon_salameche.list_capacities)
    mon_salameche.monte_niveau()
    mon_salameche.learn_capacities('lance flamme')
    print(mon_salameche.list_capacities)

    databaseService : DatabaseService = DatabaseService()

    #On sauvegarde un pokemon
    databaseService.create_table()
    databaseService.save_pokemon(mon_salameche)


