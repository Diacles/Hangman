import tkinter as tk
from Mot import Mot
from Progres import Progres
from Historique import Historique
from Score import Score
import unidecode

class Pendu():
    # Constructeur
    def __init__(self, unRoot : tk.Tk):
        self.__root = unRoot

        self.__mot = Mot()
        self.__progres = Progres(self.__mot)
        self.__historique = Historique()
        self.__score = Score()

        self.__mainFrm = tk.Frame()
        self.__dessinCnv = tk.Canvas()
        self.__scoreLbl = tk.Label()
        self.__jeuFrm = tk.Frame()
        self.__saisieLbl = tk.Label()
        self.__saisieEnt = tk.Entry()
        self.__progresLbl = tk.Label()
        self.__historiqueLbl = tk.Label()
        self.__validerBtn = tk.Button()
        self.__finFrm = tk.Frame()
        self.__resultatLbl = tk.Label()
        self.__finLbl = tk.Label()
        self.__ouiBtn = tk.Button()
        self.__nonBtn = tk.Button()

        self.ecranPendu()


    # Méthodes get et set
    def getRoot(self):
        return self.__root
    
    def setRoot(self, unRoot : tk.Tk):
        self.__root = unRoot


    # Autres méthodes
    def ecranPendu(self):
        self.__root.title("Le jeu du pendu")

        # Crée une Frame principal
        self.__mainFrm = tk.Frame(self.__root)
        self.__mainFrm.pack(fill=tk.BOTH, expand=True)

        # Crée un Canvas pour le dessin du pendu
        self.__dessinCnv = tk.Canvas(self.__mainFrm, bg="white", width=400, height=400)
        self.__dessinCnv.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # self.__Score
        self.__scoreLbl = tk.Label(self.__mainFrm, text="Score : " + str(self.__score.getScore()))
        self.__scoreLbl.pack()

        # Crée une Frame pour le jeu
        self.__jeuFrm = tk.Frame(self.__mainFrm)
        self.__jeuFrm.pack(side=tk.RIGHT, padx=10, pady=10)

        # Devinez le mot
        self.__saisieLbl = tk.Label(self.__jeuFrm, text="Devinez le mot : ")
        self.__saisieLbl.pack()

        # Crée la zone de saisie
        self.__saisieEnt = tk.Entry(self.__jeuFrm)
        self.__saisieEnt.pack()

        # Progrès
        self.__progresLbl = tk.Label(self.__jeuFrm, text="Votre progrès : " + " ".join(self.__progres.getProgres()))
        self.__progresLbl.pack()

        # Historique des saisies
        self.__historiqueLbl = tk.Label(self.__jeuFrm, text="Historique : " + " ,".join(self.__historique.getHistorique()))
        self.__historiqueLbl.pack()

        # Bouton Valider
        self.__validerBtn = tk.Button(self.__jeuFrm, text="Valider", command=lambda: self.validationSaisie(unidecode.unidecode(self.__saisieEnt.get())))
        self.__validerBtn.pack()
        self.__root.bind('<Return>',lambda e : self.validationSaisie(unidecode.unidecode(self.__saisieEnt.get())))


        # Page Fin
        self.__finFrm = tk.Frame(self.__mainFrm)
        self.__resultatLbl = tk.Label(self.__finFrm)
        self.__resultatLbl.pack()
        self.__finLbl = tk.Label(self.__finFrm, text="Le mot était : "+ self.__mot.getMot() +"\nVoulez-vous rejouer ?")
        self.__finLbl.pack()

        # Boutons Oui et Non
        self.__ouiBtn = tk.Button(self.__finFrm, text="Oui", command=lambda: self.reinitialisationJeu())
        self.__ouiBtn.pack(side=tk.LEFT, padx=10)
        self.__nonBtn = tk.Button(self.__finFrm, text="Non", command=lambda: self.fermerPendu())
        self.__nonBtn.pack(side=tk.RIGHT, padx=10)

    
    def majOccurences(self):
        lesOccurences = self.trouveLesOccurences(self.__saisieEnt.get())
        self.__progres.majProgres(lesOccurences, self.__saisieEnt.get())
        self.__progresLbl.config(text="Votre progrès : " + ' '.join(self.__progres.getProgres()))
        return 0
    
    def trouveLesOccurences(self, uneLettre : str):
        lesOccurences = []
        i = 0
        for ch in unidecode.unidecode(self.__mot.getMot()):
            if ch == uneLettre:
                lesOccurences.append(i)
            i += 1
        return lesOccurences
    
    def validationSaisie(self, unEssai : str):
        if(unEssai == self.__mot.getMot()):
            self.jeuFini(True)
        elif(len(unEssai) == 1 and unEssai in self.__mot.getMot()):
            self.__historique.majHistorique(unEssai)
            self.__historiqueLbl.config(text="Historique : " + " ,".join(self.__historique.getHistorique()))
            self.majOccurences()
            self.__saisieEnt.delete(0, tk.END)
        else:
            self.__historique.majHistorique(unEssai)
            self.__historiqueLbl.config(text="Historique : " + " ,".join(self.__historique.getHistorique()))
            self.__score.diminueVie()
            self.construirePotence()
            self.__saisieEnt.delete(0, tk.END)
            if(self.__score.getVies() == 0):
                self.__score.setScore(0)
                self.jeuFini(False)
    
    def construirePotence(self):
        vies = self.__score.getVies()
        if(vies == 9):
            self.__dessinCnv.create_line(100,300,261,300, fill="brown", width=5)#fondation
        if(vies == 8):
            self.__dessinCnv.create_line(181,300,181,50, fill="brown", width=5)#Poutre
        if(vies == 7):
            self.__dessinCnv.create_line(181,50,270,50, fill="brown", width=5)#Angle
        if(vies == 6):
            self.__dessinCnv.create_line(261,52,261,100, fill="black", width=3)#Corde
        if(vies == 5):
            self.__dessinCnv.create_oval(251,100,271,120, fill="pink", outline="black")#tête
        if(vies == 4):
            self.__dessinCnv.create_line(261,120,261,180, width=3, fill="grey")#corps
        if(vies == 3):
            self.__dessinCnv.create_line(261,120,280,170, width=3, fill="grey")#brasdroit
        if(vies == 2):
            self.__dessinCnv.create_line(261,120,240,170, width=3, fill="grey")#brasgauche
        if(vies == 1):
            self.__dessinCnv.create_line(261,180,280,240, width=3, fill="blue")#jambedroite
        if(vies == 0):
            self.__dessinCnv.create_line(261,180,240,240, width=3, fill="blue")#jambegauche    

    def jeuFini(self, victoire : bool):
        self.__jeuFrm.pack_forget()
        if(victoire):
            self.__score.augmenteScore()
            self.__scoreLbl.config(text="Score : " + str(self.__score.getScore()))
        self.__finFrm.pack()

    def fermerPendu(self):
        self.__root.destroy()

    def reinitialisationJeu(self):
        self.__mot.setMot(self.__mot.choisiMotAleatoire())
        self.__progres.setProgres(self.__progres.initProgres(self.__mot.getMot()))
        self.__historique.setHistorique(unHistorique=[])
        self.__score.setVies(10)

        self.__finFrm.pack_forget()
        self.__saisieEnt.delete(0, tk.END)
        self.__dessinCnv.delete('all')
        self.__progresLbl.config(text="Votre progrès : " + " ".join(self.__progres.getProgres()))
        self.__historiqueLbl.config(text="Historique : " + " ,".join(self.__historique.getHistorique()))
        self.__finLbl.config(text="Le mot était : "+self.__mot.getMot() +"\nVoulez-vous rejouer ?")
        self.afficheJeu()
    
    def afficheJeu(self):
        self.__jeuFrm.pack(side=tk.RIGHT, padx=10, pady=10)