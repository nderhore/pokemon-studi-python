import sqlite3

from entities import Pokemon


class DatabaseService:

    def __init__(self):
        self._file_database = './bdd/pokemondb.db'

    def create_table(self):
        connection = sqlite3.connect(self._file_database)
        curseur = connection.cursor()
        curseur.execute("""
        CREATE TABLE IF NOT EXISTS Pokemon(
        id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
        nom TEXT,
        type TEXT,
        nature TEXT,
        niveau INTEGER)
        """)
        connection.commit()
        connection.close()

    def save_pokemon(self, mon_pokemon: Pokemon):
        connection = sqlite3.connect(self._file_database)
        curseur = connection.cursor()
        curseur.execute("""
        INSERT INTO Pokemon(nom,type,nature,niveau) VALUES (?,?,?,?)""",
                        (mon_pokemon.nom, mon_pokemon.type, mon_pokemon.nature, mon_pokemon.niveau))
        connection.commit()
        connection.close()
