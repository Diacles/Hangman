class Score():
    # Constructeur
    def __init__(self, unScore : int = 0, desVies : int = 10):
        self.__score = unScore
        self.__vie = desVies

    # Méthodes get et set
    def getScore(self):
        return self.__score
    def setScore(self, unScore):
        self.__score = unScore

    def getVies(self):
        return self.__vie
    def setVies(self, desVies):
        self.__vie = desVies

    # Autres méthodes
    def augmenteScore(self):
        self.__score += self.__vie
        return self.__score
    
    def diminueVie(self):
        self.__vie -= 1
        return self.__vie