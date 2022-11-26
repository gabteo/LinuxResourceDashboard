# versão tkinter 
from tkinter import *
import tkinter.messagebox
import customtkinter
from NavMenu import NavMenu


customtkinter.set_appearance_mode("Dark")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

WIDTH = 1280
HEIGHT = 720

""" 
# tkinter usa widgets. primeiro define, depois exibe
helloWorldLabel = Label(root, text="Hello world!")
helloWorldLabel.pack() """

class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        self.title("Linux Resouce Dashboard")
        self.geometry(f"{WIDTH}x{HEIGHT}")
        self.protocol("WM_DELETE_WINDOW", self.on_closing)  # call .on_closing() when app gets closed

        # ============ create two frames ============
        # NavMenu e dashboardFrame
        # configure grid layout (2x1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.navMenu = NavMenu(self)
        #self.dashboardFrame = DashboardFrame(self)

        self.navMenu.grid()
        #self.dashboardFrame.grid()


    def on_closing(self, event=0):
        self.destroy()





""" class DashboardFrame():
    def __init__(self, app: App) -> None:
        self.dashboardFrame = customtkinter.CTkFrame(master=app)
        self.dashboardFrame.grid(row=0, column=0, sticky="nswe")   """ 