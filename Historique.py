from Mot import Mot
import unidecode

class Historique():
    # Constructeur
    def __init__(self, unHistorique : list = []):
        self.__historique = unHistorique

    # Méthodes get et set
    def getHistorique(self):
        return self.__historique
    def setHistorique(self, unHistorique : list):
        self.__historique = unHistorique
        
    # Autres méthodes
    def majHistorique(self, uneEntree : str):
        if(uneEntree not in self.__historique):
            self.__historique.append(uneEntree)
        
    def trouveLesOccurences(self, uneLettre : str , unMot : Mot):
        lesOccurences = []
        i = 0
        for ch in unidecode.unidecode(unMot.getTexte()):
            if ch == uneLettre:
                lesOccurences.append(i)
            i += 1
        return lesOccurences