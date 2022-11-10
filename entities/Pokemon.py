class Pokemon:

    # Constructeur
    def __init__(self, nom: str, type: str, nature: str, niveau: int):
        self._nom = nom
        self._type = type
        self._nature = nature
        self._niveau = niveau

    def __init__(self):
        self._nom = 'pikachu'
        self._type = 'electrique'
        self._nature = 'docile'
        self._niveau = 10


    def monte_niveau(self):
        print("le niveau actuel est de : ", self._niveau)
        self._niveau += 1
        print("le nouveau est de : ", self._niveau)

    def _get_nom(self):
        return self._nom

    def _set_nom(self, nouveau_nom: str):
        self._nom = nouveau_nom

    def _get_niveau(self):
        return self._niveau

    def _set_niveau(self, nouveau_niveau: str):
        self._niveau = nouveau_niveau

    def _get_type(self):
        return self._type

    def _set_type(self, nouveau_type: str):
        self._type = nouveau_type

    def _get_nature(self):
        return self._nature

    def _set_nature(self, nouveau_nature: str):
        self._nature = nouveau_nature

    nom = property(_get_nom, _set_nom)
    niveau = property(_get_niveau, _set_niveau)
    type = property(_get_type, _set_type)
    nature = property(_get_nature, _set_nature)

