import random
from entities.Pokemon import Pokemon


class Salameche(Pokemon):

    def __init__(self, nom: str, type: str, nature: str, niveau: int, capacites: list):
        super().__init__(nom, type, nature, niveau)
        self._list_capacities = capacites

    def __init__(self, capacites: list):
        super().__init__()
        self._list_capacities = capacites

    def __init__(self, name : str,capacites: list):
        super().__init__(name)
        self._list_capacities = capacites

    def _get_list_capacities(self) -> list:
        return self._list_capacities

    def _set_list_capacities(self, capacities: list):
        self._list_capacities = capacities

    def learn_capacities(self, capacitie: str):
        if len(self._list_capacities) >= 4:
            index_capacitie: int = random.randint(0,3)
            self._list_capacities[index_capacitie] = capacitie
        else:
            self._list_capacities.append(capacitie)

    list_capacities = property(_get_list_capacities, _set_list_capacities)
