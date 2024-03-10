import Logic
import tkinter
import customtkinter

TITLE = "SMOQUIT"
FRAME_SIZE = "360x640"
BACKGROUND_COLOR = "#171A23"
WHITE = "#FFFFFF"
BLACK = "#000000"
BUTTON = "#FF5722"
BUTTON_HOVER = "#B53D17"

app = None

def getApp() :
    return app

def initFormulaire() :
    #Initialiser la base de customtkinter
    customtkinter.set_appearance_mode("System")

    #Frame de l'application
    app = customtkinter.CTk()
    app.geometry(FRAME_SIZE)
    app.title(TITLE)
    app.config(bg= BACKGROUND_COLOR)
    app.resizable(False,False)
    

    #Debut UI elements
    messageLabel = customtkinter.CTkLabel(app, text="Bienvenue!",font=("Helvetica", 24, "bold"))
    messageLabel.configure(bg_color=BACKGROUND_COLOR)
    messageLabel.pack(pady=10)
    expLabel = customtkinter.CTkLabel(app,text="Remplir les informations suivantes",font=("Helvetica", 16, "bold") )
    expLabel.configure(bg_color=BACKGROUND_COLOR)
    expLabel.pack(pady = 20)

    #Label and input pour la date
    date = tkinter.StringVar(value="2024-02-10")
    labelDate = customtkinter.CTkLabel(app, text="Date d'arret YY-MM-DD", font=("Helvetica", 14, "bold"))
    labelDate.configure(bg_color=BACKGROUND_COLOR)
    labelDate.pack()
    inputDate = customtkinter.CTkEntry(app, width=250, height=25, textvariable=date)
    inputDate.configure(fg_color=WHITE, text_color=BLACK, border_color= BLACK , bg_color=BACKGROUND_COLOR)
    inputDate.pack(pady=5)

    #Label and input pour nombre de cigarette par jour
    NbrCigJour = tkinter.IntVar(value=3)
    labelNbrCigJour = customtkinter.CTkLabel(app, text="Nombre de cigarette par jour", font=("Helvetica", 14, "bold"))
    labelNbrCigJour.configure(bg_color=BACKGROUND_COLOR)
    labelNbrCigJour.pack()
    inputNbrCigJour = customtkinter.CTkEntry(app, width=250, height=25, textvariable=NbrCigJour)
    inputNbrCigJour.configure(fg_color=WHITE, text_color=BLACK, border_color= BLACK , bg_color=BACKGROUND_COLOR)
    inputNbrCigJour.pack(pady=5)

    #Label and input pour nombre de cigarette par paquet
    nbrCigPaquet = tkinter.IntVar(value=8)
    labelNbrCigPaquet = customtkinter.CTkLabel(app, text="Nombre de cigarette par paquet", font=("Helvetica", 14, "bold"))
    labelNbrCigPaquet.configure(bg_color=BACKGROUND_COLOR)
    labelNbrCigPaquet.pack()
    inputNbrCigPaquet = customtkinter.CTkEntry(app, width=250, height=25, textvariable = nbrCigPaquet)
    inputNbrCigPaquet.configure(fg_color=WHITE, text_color=BLACK, border_color= BLACK , bg_color=BACKGROUND_COLOR)
    inputNbrCigPaquet.pack(pady=5)

    #Label and input pour le prix du paquet
    prixPaquet = tkinter.IntVar(value=19)
    labelPrixPaquet = customtkinter.CTkLabel(app, text="Prix du paquet", font=("Helvetica", 14, "bold"))
    labelPrixPaquet.configure(bg_color=BACKGROUND_COLOR)
    labelPrixPaquet.pack()
    inputPrixPaquet = customtkinter.CTkEntry(app, width=250, height=25, textvariable=prixPaquet)
    inputPrixPaquet.configure(fg_color=WHITE, text_color=BLACK, border_color= BLACK , bg_color=BACKGROUND_COLOR)
    inputPrixPaquet.pack(pady=5)

    #Button enregistrer
    bouttonEnregistrer = customtkinter.CTkButton(app, text="Enregistrer",font=("Helvetica", 14, "bold"),
                                                 command=lambda : Logic.loadData(date.get(),
                                                        NbrCigJour.get(),nbrCigPaquet.get(),prixPaquet.get(), labelErreur, app))
    bouttonEnregistrer.configure(fg_color=BUTTON, text_color= WHITE, hover_color=BUTTON_HOVER)
    bouttonEnregistrer.pack(pady = 20)

    #Label erreur
    labelErreur = customtkinter.CTkLabel(app, text="", text_color="red")
    labelErreur.configure(bg_color=BACKGROUND_COLOR)
    labelErreur.pack(pady=20)

    return app