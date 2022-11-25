# versão tkinter 
from tkinter import *
import tkinter.messagebox
import customtkinter

customtkinter.set_appearance_mode("Dark")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

""" 
root = Tk() # cria janela principal

# tkinter usa widgets. primeiro define, depois exibe
helloWorldLabel = Label(root, text="Hello world!")
helloWorldLabel.pack() """

class App(customtkinter.CTk):

    WIDTH = 1280
    HEIGHT = 720

    def __init__(self):
        super().__init__()

        self.title("Linux Resouce Dashboard")
        self.geometry(f"{App.WIDTH}x{App.HEIGHT}")
        self.protocol("WM_DELETE_WINDOW", self.on_closing)  # call .on_closing() when app gets closed

        # ============ create two frames ============
        # NavMenu e dashboardFrame
        # configure grid layout (2x1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        NavMenu(self)
        DashboardFrame(self)


    def on_closing(self, event=0):
        self.destroy()



class NavMenu():
    def __init__(self, app: App) -> None:
        self.navMenu = customtkinter.CTkFrame(master=app, width=180, corner_radius=0)
        self.navMenu.grid(row=0, column=0, sticky="nswe")

        # definindo as linhas do menu de navegação
        self.navMenu.grid_rowconfigure(0, minsize=10)   # empty row with minsize as spacing
        self.navMenu.grid_rowconfigure(5, weight=1)  # empty row as spacing
        self.navMenu.grid_rowconfigure(8, minsize=20)    # empty row with minsize as spacing
        self.navMenu.grid_rowconfigure(11, minsize=10)  # empty row with minsize as spacing
        

class DashboardFrame():
    def __init__(self, app: App) -> None:
        self.dashboardFrame = customtkinter.CTkFrame(master=app)
        self.dashboardFrame.grid(row=0, column=0, sticky="nswe")   