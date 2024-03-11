import Data
import pagePrincipal
import re #regex
import json
import os
import formulaire

#Appele par le formulaire pour creer un objet Data
#Verifie les inputs
def loadData(date, nbrCigJour,nbrCigPaquet, prixPaquet, label, app) :
    paternDate = r'^\d{4}\-(0?[1-9]|1[012])\-(0?[1-9]|[12][0-9]|3[01])$'

    #Verification qu'il n'est pas d'empty string
    if(date == "") :
        print("La date ne peut pas etre vide.")
        label.configure(text="La date ne peut pas etre vide.")
        return
    
    #Verification des inputs
    date = validerStringRegex(paternDate,date)
    nbrCigJour = validerInt(nbrCigJour)
    nbrCigPaquet = validerInt(nbrCigPaquet)
    prixPaquet = validerInt(prixPaquet)

    #Si erreur quoi faire
    if(date == None) :
        print("Mauvais format pour la date.")
        label.configure(text="Mauvais format pour la date")
        return
    elif(nbrCigJour == None) :
        print("Le nombre de cigarette par jour doit etre plus grand que 0.")
        label.configure(text="Le nombre de cigarette par jour doit etre plus grand que 0.")
        return
    elif(nbrCigPaquet == None) :
        print("Le nombre de cigarette par paquet doit etre plus grand que 0.")
        label.configure(text="Le nombre de cigarette par paquet doit etre plus grand que 0.")
        return
    elif(prixPaquet == None) :
        print("Le prix d'un paquet doit etre plus grand que 0$.")
        label.configure(text="Le prix d'un paquet doit etre plus grand que 0$.")
        return
    #Si aucun erreur creer l'objet data et allez chercher la page principal
    else :    
        data = Data.data(date,nbrCigJour,nbrCigPaquet,prixPaquet)
        data.toString()
        label.configure(text="")
        creerFichier(data)
        app.destroy()
        page = pagePrincipal.initPagePrincipal(data)
        page.mainloop()

#Appele par pagePrinciap pour detruire le fichier data.json et ouvrir la page formulaire
def restart(app) :
    if(os.path.exists("data.json")) :
        os.remove("data.json")
        app.destroy()
        page = formulaire.initFormulaire()
        page.mainloop()
    else :
        print("Erreur, fichier non existant")
    
#Permet de valider des String grace a un patern Regex
def validerStringRegex(patern, string) :
    string = string.strip()
    if(re.match(patern, string)) :
        return string
    else :
        return None

#Permet de valider des Int pour qu'il soit plus grand que 0.
def validerInt(int) :
    if(int > 0) :
        return int
    else :
        return None

#Creer un fichier ou ajoute sur le fichier data.json les informations necessaire pour la prochaine utilisation
def creerFichier(data) :
    dict = {
        'date' : data.date,
        'nbrCigJour' : data.nbrCigJour,
        'nbrCigPaquet' : data.nbrCigPaquet,
        'prixPaquet' : data.prixPaquet,
    }
    with open('data.json', 'w') as f :
        json.dump(dict,f)

#Retourne un objet data creer a partir des informations dans le fichier data.json
def loadDataStart() :
    with open('data.json', 'r') as fichier :
        dict = json.load(fichier)
    return Data.data(dict['date'],dict['nbrCigJour'],dict['nbrCigPaquet'],dict['prixPaquet'])