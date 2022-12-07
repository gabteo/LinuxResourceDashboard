""" 
classe que cria um banco de dados e salva dados do sistema nele
https://towardsdatascience.com/an-easy-beginners-guide-to-sqlite-in-python-and-pandas-fbf1f38f6800
"""


import sqlite3 as db
import time
import logging


class database():

    def __init__(self) -> None:
        self.log = logging.getLogger(__name__)
        self.log.info("Criando banco de dados...")
        self.dbPath = "systemStats.db"
        self.conn = None

        try:
            #self.conn = db.connect(':memory:') #cria database na memória
            self.conn = db.connect(self.dbPath) #cria database na memória
        except db.Error as e:
            print(e)
        
        self.c = self.conn.cursor()

        self.createCPUTable()
        self.createMemTable()
        self.createFileSystemTable()        

    def createCPUTable(self):
        self.log.info("Criando tabela da CPU...")
        try:
            self.c.execute("CREATE TABLE IF NOT EXISTS cpu (memid INTEGER PRIMARY KEY, memtotal INT, memfree INT, memavailable INT, swaptotal INT, swapfree INT)")
        except db.Error:
            self.log.exception("Erro ao criar tabela da CPU")

    def createMemTable(self):
        self.log.info("Criando tabela da memória...")
        try:
            self.c.execute("CREATE TABLE IF NOT EXISTS mem (memid INTEGER PRIMARY KEY, memtotal INT, memfree INT, memavailable INT, swaptotal INT, swapfree INT)")
        except db.Error:
            self.log.exception("Erro ao criar tabela da memória")


    def createFileSystemTable(self):
        self.log.info("Criando tabela do sistema de arquivos...")
        try:
            self.c.execute("CREATE TABLE IF NOT EXISTS filesystem (memid INTEGER PRIMARY KEY, memtotal INT, memfree INT, memavailable INT, swaptotal INT, swapfree INT)")
        except db.Error:
            self.log.exception("Erro ao criar tabela do sistema de arquivos")

        self.log.info("Banco de dados criado.")


    def appendMemTable(self, memArray):
        sql = """ INSERT INTO mem(memid, memtotal, memfree, memavailable, swaptotal, swapfree)
                VALUES(?,?,?,?,?,?)"""
        self.c.execute(sql, memArray)
        pass

    def getTimestamp(self):
        return time.time()


    def __del__(self):
        pass

