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

def initPagePrincipal() :
    #Initialiser la base de customtkinter
    customtkinter.set_appearance_mode("System")

    #Frame de l'application
    app = customtkinter.CTk()
    app.geometry(FRAME_SIZE)
    app.title(TITLE)
    app.config(bg= BACKGROUND_COLOR)
    app.resizable(False,False)

    label = customtkinter.CTkLabel(app,text="YESSSSIR MILLER")
    label.pack()

    return app