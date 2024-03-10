import arrow

class data :
    #Initialisation
    date = None
    temps = None
    nbrCigJour = None
    nbrCigPaquet = None
    prixPaquet = None
    #Besoin d'etre calcule
    jours = None
    heure = None
    minute = None
    economie = None
    tempsRecupere = None

    #Constructeur
    def __init__(self,date,temps,nbrCigJour,nbrCigPaquet,prixPaquet):
        self.date = date
        self.temps = temps
        self.nbrCigJour = nbrCigJour
        self.nbrCigPaquet = nbrCigPaquet
        self.prixPaquet = prixPaquet
        self.calculer()

    #Methodes
    def calculer(self) :
        auj = arrow.now()   #Get date au moment du calcul
        dateArret = arrow.get(self.date + " " + self.temps, 'YYYY-MM-DD HH:mm') #Get date d'arret
        
        #Calcul le nombre de jour, heure, minute
        self.jours = auj.day - dateArret.day
        self.heure = auj.hour - dateArret.hour
        self.minute = auj.minute - dateArret.minute

        #Calcul de l'economie
        nbrJourPaquet = self.nbrCigPaquet / self.nbrCigJour
        economieParJour = self.prixPaquet / nbrJourPaquet
        self.economie = self.jours * economieParJour

        #Calcul de tempsRecupere
        tempsFumer = 5
        self.tempsRecupere = int(tempsFumer *  self.nbrCigJour * self.jours / 60)

    def toString(self) :
        print("Vous avez arreter de fumer le " + str(arrow.get(self.date + " " + self.temps, 'YYYY-MM-DD HH:mm')))
