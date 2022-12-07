from tkinter import *
import tkinter.messagebox
import customtkinter
import os
from defines import defines

class widgetTopCommand(customtkinter.CTkFrame):

    def __init__(self, master) -> None:
        print("Criando widgetTopCommand...")

        super().__init__(master, width=10, height=10)  # construtor da classe herdada, no caso o Frame
        self.master = master


        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
      
        self.topCmd()

        self.topLabel = customtkinter.CTkLabel(master=self, 
            text=self.topCmdOutput, 
            #height=100, 
            #width = 100, 
            text_font=('Roboto', 12),
            corner_radius=6, 
            fg_color=("white", "gray25"),  # <- custom tuple-color
            justify=tkinter.LEFT, 
            text_color=("gray75"))
        
        """ self.topLabel = customtkinter.CTkTextbox(master=self, 
            text=self.topCmdOutput, 
            #height=100, 
            #width = 100, 
            text_font=('Roboto', 12),
            corner_radius=6, 
            fg_color=("white", "gray25"),  # <- custom tuple-color
            justify=tkinter.LEFT, 
            text_color=("gray75")) """

        self.grid(row=0, column=0, sticky="nswe")
        self.topLabel.grid(row=0, column=0, sticky="nwe", pady=10, padx=10)

        print("widgetTopCommand criado.")

    def topCmd(self):
        self.topPath = defines.CMD_FILES_PATH + '/topOut.txt'

        if(not (os.path.isfile(self.topPath))):
            os.system("touch "+ self.topPath)
        #self.stream = os.popen('top -n 1 -b | ' + defines.CMD_FILES_PATH + '/topOut')
        #self.topCmdOutput = self.stream.read()

        print("Executando top...")
        os.system('top -n 1 -b > ' + self.topPath)
        
        print("lendo arquivo: " + self.topPath)
        with open(self.topPath) as f:
            self.topCmdOutput = f.read()
            print("Arquivo lido")