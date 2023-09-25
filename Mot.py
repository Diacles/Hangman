import random
import unidecode
class Mot():
    # Constructeur
    def __init__(self):
        self.__mot = self.choisiMotAleatoire()

    # Méthodes get et set
    def getMot(self):
        return self.__mot
    def setMot(self, unMot : str):
        self.__mot = unMot

    # Autres méthodes
    def choisiMotAleatoire(self):
        nomFichier = "mots.txt"
        with open(nomFichier, encoding='utf-8') as contenuFichier:
            lesMots = contenuFichier.readlines()
        return unidecode.unidecode(random.choice(lesMots).strip("\n").lower())

