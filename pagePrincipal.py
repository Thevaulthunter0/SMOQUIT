import Logic
import tkinter
import customtkinter
from PIL import Image


TITLE = "SMOQUIT"
FRAME_SIZE = "360x640"
BACKGROUND_COLOR = "#171A23"
WHITE = "#FFFFFF"
BLACK = "#000000"
BUTTON = "#FF5722"
BUTTON_HOVER = "#B53D17"
LOGO= 90,90
SMALL_LOGO= 30,30

def initPagePrincipal(data) :
    #Initialiser la base de customtkinter
    customtkinter.set_appearance_mode("System")

    #Frame de l'application
    app = customtkinter.CTk()
    app.geometry(FRAME_SIZE)
    app.title(TITLE)
    app.config(bg= BACKGROUND_COLOR)
    app.resizable(False,False)

    #Debut UI elements
    imageCalendrier = customtkinter.CTkImage(light_image=Image.open('image/calendrier.png'), 
                                        dark_image=Image.open('image/calendrier.png'),
                                        size=(LOGO))
    imageFlamme = customtkinter.CTkImage(light_image=Image.open('image/flamme.png'), 
                                        dark_image=Image.open('image/flamme.png'),
                                        size=(SMALL_LOGO))
    imageArgent = customtkinter.CTkImage(light_image=Image.open('image/argent.png'), 
                                        dark_image=Image.open('image/argent.png'),
                                        size=(SMALL_LOGO))
    imageTemps = customtkinter.CTkImage(light_image=Image.open('image/temps.png'), 
                                        dark_image=Image.open('image/temps.png'),
                                        size=(SMALL_LOGO))


    #Affichage Jours
    labelImageCalendrier = customtkinter.CTkLabel(app, text="", image=imageCalendrier)
    labelImageCalendrier.configure(bg_color=BACKGROUND_COLOR)
    labelImageCalendrier.pack(pady=10)

    labelNbrJour = customtkinter.CTkLabel(app, text=data.jours, font=("Helvetica", 24, "bold"))
    labelNbrJour.configure(bg_color=BACKGROUND_COLOR)
    labelNbrJour.pack()

    labelJour = customtkinter.CTkLabel(app, text="Jours sans cigarette!", font=("Helvetica", 16, "bold"))
    labelJour.configure(bg_color=BACKGROUND_COLOR)
    labelJour.pack()

    #Affichage nombre de cigarette evite
    labelImageFlamme = customtkinter.CTkLabel(app, text="", image=imageFlamme)
    labelImageFlamme.configure(bg_color=BACKGROUND_COLOR)
    labelImageFlamme.pack(pady = 20) 

    labelNbrCig = customtkinter.CTkLabel(app, text=data.cigEvite, font=("Helvetica", 24, "bold"))
    labelNbrCig.configure(bg_color=BACKGROUND_COLOR)
    labelNbrCig.pack()

    labelCig = customtkinter.CTkLabel(app, text="Cigarettes evitées", font=("Helvetica", 16, "bold"))
    labelCig.configure(bg_color=BACKGROUND_COLOR)
    labelCig.pack()

    #Afficahge economie
    labelImageArgent = customtkinter.CTkLabel(app, text="", image=imageArgent)
    labelImageArgent.configure(bg_color=BACKGROUND_COLOR)
    labelImageArgent.pack(pady = 20)

    labelNbrEconomie = customtkinter.CTkLabel(app, text=str(data.economie) + "$", font=("Helvetica", 24, "bold")) 
    labelNbrEconomie.configure(bg_color=BACKGROUND_COLOR)
    labelNbrEconomie.pack()

    labelEconomie = customtkinter.CTkLabel(app, text="Economie", font=("Helvetica", 16, "bold"))
    labelEconomie.configure(bg_color=BACKGROUND_COLOR)
    labelEconomie.pack()

    #Affichage temps recupere
    labelImageTemps = customtkinter.CTkLabel(app, text="", image=imageTemps)
    labelImageTemps.configure(bg_color=BACKGROUND_COLOR)
    labelImageTemps.pack(pady = 20)

    labelNbrTemps = customtkinter.CTkLabel(app, text=str(data.tempsRecupere) + " h", font=("Helvetica", 24, "bold"))
    labelNbrTemps.configure(bg_color=BACKGROUND_COLOR)
    labelNbrTemps.pack()

    labelTemps = customtkinter.CTkLabel(app, text="Temps récupéré", font=("Helvetica", 16, "bold"))
    labelTemps.configure(bg_color=BACKGROUND_COLOR)
    labelTemps.pack()

     #Button reset
    bouttonEnregistrer = customtkinter.CTkButton(app, text="Recommencer",font=("Helvetica", 14, "bold"),
                                                 command=lambda : Logic.restart(app))
    bouttonEnregistrer.configure(fg_color=BUTTON, text_color= WHITE, hover_color=BUTTON_HOVER)
    bouttonEnregistrer.pack(pady = 20)

    return app