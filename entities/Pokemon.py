class Pokemon:

    # Constructeur
    def __init__(self, nom: str, type: str, nature: str, niveau: int):
        self._nom = nom
        self._type = type
        self._nature = nature
        self._niveau = niveau

    def monte_niveau(self):
        self._niveau += 1

    def _get_nom(self):
        return self._nom

    def _set_nom(self, nouveau_nom: str):
        self._nom = nouveau_nom

    nom = property(_get_nom, _set_nom)
