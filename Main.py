import formulaire
import pagePrincipal
import os

if( os.path.exists("data.json")) :  #Donnee deja connu, ouvrir le menu principal
    pagePrincipal = pagePrincipal.initPagePrincipal()
    pagePrincipal.mainloop()
else :                              #Donnee inconnu, ouvrir le formulaire
    formulaire = formulaire.initFormulaire()
    formulaire.mainloop()