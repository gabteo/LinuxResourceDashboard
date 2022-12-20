""" 
classe que cria um banco de dados e salva dados do sistema nele
https://towardsdatascience.com/an-easy-beginners-guide-to-sqlite-in-python-and-pandas-fbf1f38f6800
"""


import sqlite3 as db
import time
import logging
import os


class database():

    def __init__(self) -> None:
        self.log = logging.getLogger(__name__)
        self.log.info("Criando banco de dados...")
        self.dbPath = "systemStats.db"
        self.conn = None

        try:
            #self.conn = db.connect(':memory:') #cria database na memória
            self.conn = db.connect(self.dbPath, check_same_thread = False) #cria database na memória
        except db.Error as e:
            self.log.exception("Erro ao abrir a conexão com o db.")
            print(e)
            return
        
        self.c = self.conn.cursor()

        self.createCPUTable()
        self.createMemTable()

    def createCPUTable(self):
        self.log.info("Criando tabela da CPU...")
        try:
            query = "CREATE TABLE IF NOT EXISTS cpu (cpuid INTEGER PRIMARY KEY, cpu_usage REAL)"
            self.c.execute(query)
        except db.Error:
            self.log.exception("Erro ao criar tabela da CPU")
    
    def CPUTableAddCores(self, cores: str):
        for core in range(int(cores.strip())):
            try:
                query = f"ALTER TABLE cpu ADD cpu{core} REAL"
                self.c.execute(query)
            except db.Error:
                self.log.exception("Erro ao adicionar core na tabela da CPU. Tabela já tem core")
                #self.log.exception(db.Error)

    def createMemTable(self):
        self.log.info("Criando tabela da memória...")
        try:
            self.c.execute("CREATE TABLE IF NOT EXISTS mem (memid INTEGER PRIMARY KEY, memtotal INT, memfree INT, memavailable INT, swaptotal INT, swapfree INT)")
        except db.Error:
            self.log.exception("Erro ao criar tabela da memória")





    def memTableAddRow(self, memArray: list):
        sql = """ INSERT OR IGNORE INTO mem(memid, memtotal, memfree, memavailable, swaptotal, swapfree)
                VALUES(?,?,?,?,?,?)"""
        memArray.insert(0, self.getTimestamp())
        try:
            self.c.execute(sql, memArray)
            self.conn.commit()
        except db.Error:
            self.log.exception("Erro ao adicionar row na tabela mem")
        return

    def getTimestamp(self):
        timestamp = int(time.time())
        #print (timestamp)
        return timestamp


    def __del__(self):
        #os.remove('systemStats.db')
        try:
            #self.conn = db.connect(':memory:') #cria database na memória
            self.conn.close
        except db.Error as e:
            self.log.exception("Erro ao fechar a conexão com o db.")

        return

