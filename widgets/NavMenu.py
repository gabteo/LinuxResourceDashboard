from tkinter import *
import customtkinter

class NavMenu(customtkinter.CTkFrame):   
#classe herdeira (no python chama-se subclasse) de customtkinter.CTkFrame 

    def __init__(self, master) -> None:
        print("Criando NavMenu...")
        super().__init__(master)  # construtor da classe herdada, no caso o Frame
        self.width = 180
        self.master = master
        self.corner_radius = 0

        # self.navMenu = customtkinter.CTkFrame(master=master, width=180, corner_radius=0)
        self.grid(row=0, column=0, sticky="nswe")

        # definindo as linhas do menu de navegação
        self.grid_rowconfigure(0, minsize=10)   # empty row with minsize as spacing
        self.grid_rowconfigure(5, weight=1)  # empty row as spacing
        self.grid_rowconfigure(8, minsize=20)    # empty row with minsize as spacing
        self.grid_rowconfigure(11, minsize=10)  # empty row with minsize as spacing


        # Adicionando Título
        self.appName = customtkinter.CTkLabel(master=self,
                                              text="Linux Resouce Dashboard",
                                              text_font=("Roboto Medium", -16))  # font name and size in px
        self.appName.grid(row=1, column=0, pady=10, padx=10)

        # botões de navegação
        self.homeBtn = customtkinter.CTkButton(master=self,
                                                text="Visão Geral",
                                                command=self.homeBtn_event)
        self.homeBtn.grid(row=2, column=0, pady=10, padx=20)

        self.cpuBtn = customtkinter.CTkButton(master=self,
                                                text="CPU",
                                                command=self.cpuBtn_event)
        self.cpuBtn.grid(row=3, column=0, pady=10, padx=20)

        self.memoryBtn = customtkinter.CTkButton(master=self,
                                                text="Memória",
                                                command=self.memoryBtn_event)
        self.memoryBtn.grid(row=4, column=0, pady=10, padx=20)

        self.sysInfoBtn = customtkinter.CTkButton(master=self,
                                                text="Informações do Sistema",
                                                command=self.sysInfoBtn_event)
        self.sysInfoBtn.grid(row=5, column=0, pady=10, padx=20)

        self.versionLabel = customtkinter.CTkLabel(master=self, text="versão 0.1", text_color=("gray50"))
        self.versionLabel.grid(row=10, column=0, pady=10, padx=20)

        print("NavMenu criado.")

        

    def homeBtn_event(self):
        print("Visão geral")

    def cpuBtn_event(self):
        print("CPU")
    
    def memoryBtn_event(self):
        print("Memória")
    
    def sysInfoBtn_event(self):
        print("Informações do Sistema")