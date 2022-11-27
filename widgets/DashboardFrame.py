from tkinter import *
import customtkinter
from defines import defines
from .widgetTopCommand import widgetTopCommand


class DashboardFrame(customtkinter.CTkFrame):

    def __init__(self, master) -> None:
        print("Criando DashboardFrame...")

        super().__init__(master)  # construtor da classe herdada, no caso o Frame
        self.master = master

        self.grid(row=0, column=0, sticky="nswe")

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        self.grid_rowconfigure(0, weight=2, minsize=50)
        self.grid_rowconfigure(1, weight=2, minsize=50)
        self.grid_rowconfigure(2, weight=2, minsize=50)
        self.grid_rowconfigure(3, weight=1, minsize=50)

        """ self.helloLabel = customtkinter.CTkLabel(master=self, 
            text="hello", 
            height=100, 
            width = 100, 
            corner_radius=6, 
            fg_color=("white", "gray38"),  # <- custom tuple-color
            justify=tkinter.LEFT, 
            text_color=("gray75")) """
        
        #self.helloLabel.grid(row=0, column=0, sticky="nwe", pady=10, padx=10)
        
        self.widgetTopCommand = widgetTopCommand(self)
        self.widgetTopCommand.grid(row=2, column=0, sticky="nwe", pady=10, padx=10, columnspan=2)

        print("DashboardFrame criado.")



