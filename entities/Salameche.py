from entities.Pokemon import Pokemon


class Salameche(Pokemon):

    def __init__(self, nom: str, type: str, nature: str, niveau: int, capacites: list):
        super().__init__(nom, type, nature, niveau)
        self._list_capacities = capacites
