import formulaire
import pagePrincipal
import os
import Logic

if( os.path.exists("data.json")) :  #Donnee deja connu, ouvrir le menu principal
    data = Logic.loadDataStart()
    pagePrincipal = pagePrincipal.initPagePrincipal(data)
    pagePrincipal.mainloop()
else :                              #Donnee inconnu, ouvrir le formulaire
    formulaire = formulaire.initFormulaire()
    formulaire.mainloop()