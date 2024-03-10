import arrow

class data :
    #Initialisation
    date = None
    nbrCigJour = None
    nbrCigPaquet = None
    prixPaquet = None
    #Besoin d'etre calcule
    jours = None
    cigEvite = None
    economie = None
    tempsRecupere = None

    #Constructeur
    def __init__(self,date,nbrCigJour,nbrCigPaquet,prixPaquet):
        self.date = date
        self.nbrCigJour = nbrCigJour
        self.nbrCigPaquet = nbrCigPaquet
        self.prixPaquet = prixPaquet
        self.calculer()

    #Methodes
    def calculer(self) :
        auj = arrow.now()   #Get date au moment du calcul
        dateArret = arrow.get(self.date, 'YYYY-MM-DD') #Get date d'arret
        
        #Calcul le nombre de jour
        annee = (auj - dateArret).days // 365
        self.jours = (auj - dateArret).days  + (annee * 365)

        #Calcul du nombre de cigarette evite
        self.cigEvite = self.nbrCigJour * self.jours

        #Calcul de l'economie
        nbrJourPaquet = self.nbrCigPaquet / self.nbrCigJour
        economieParJour = self.prixPaquet / nbrJourPaquet
        self.economie = self.jours * economieParJour

        #Calcul de tempsRecupere
        tempsFumer = 5
        self.tempsRecupere = int(tempsFumer *  self.nbrCigJour * self.jours / 60)

    def toString(self) :
        print("Vous avez arreter de fumer le " + str(arrow.get(self.date, 'YYYY-MM-DD')) 
              + " et vous avez eviter " + str(self.cigEvite) + " cigarettes!\n"
              + " cela fait " + str(self.jours) + " jours que vous n'avez pas fumer!")
