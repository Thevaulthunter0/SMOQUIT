import Data

def loadData(date, temp, NbrCigJour,nbrCigPaquet, prixPaquet) :
    data = Data.data(date,temp,NbrCigJour,nbrCigPaquet,prixPaquet)
    data.toString()