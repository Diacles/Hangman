from Mot import Mot

class Progres():
    # Constructeur
    def __init__(self, unMot : Mot):
        self.__mot = unMot
        self.__progres = self.initProgres(self.__mot.getMot())

    # Méthodes get et set
    def getProgres(self):
        return self.__progres
    def setProgres(self, unProgres : list):
        self.__progres = unProgres

    # Autres méthodes
    def initProgres(self, unTexte : str):
        progres = []
        punc = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        for i in unTexte:
            if i == " ":
                progres.append(" ")
            elif i in punc:
                progres.append("i")
            else: 
                progres.append("_")
        return progres
    
    def majProgres(self, desOccurences : list, uneLettre : str):
        for uneOccurence in desOccurences:
            self.__progres[uneOccurence] = uneLettre
