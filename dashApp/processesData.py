import subprocess
import logging
import database
import re # regex lib
from enum import Enum


class processesData():

    def __init__(self, db) -> None:
        self.log = logging.getLogger(__name__)
        
        self.topColumnsNames = ['PID', 'USER', 'PRIORITY', 'NICE', 'VIRTUALMEM', 'RESIDENTMEM', 'SHAREDMEM', 'STATUS', 'CPU', 'MEM', 'TIME', 'COMMAND']
        
        self.topColumns = Enum('topColumns', ['PID', 'USER', 'PRIORITY', 'NICE', 'VIRTUALMEM', 'RESIDENTMEM', 'SHAREDMEM', 'STATUS', 'CPU', 'MEM', 'TIME', 'COMMAND'], start=0)
        
        self.getProcesses()
        self.order = self.topColumns.RESIDENTMEM.name
        self.sortProcesses(self.order)

        return

    def getProcesses(self):
        cmd = "top -n 1 -b | awk 'FNR > 7 { print }'"
        self.log.info(f"Executando comando: '{cmd}'")
        self.processes = self.execCmd(cmd)

        self.procList = self.processes.split('\n')
        # Neste ponto, procList é uma lista de processos, e cada processo é string

        #print(*self.procList, sep = "\n")
        self.procDicts = []

        for process, value in enumerate(self.procList):
            self.procList[process] = self.procList[process].split()
            
            intPID = int(self.procList[process][self.topColumns.PID.value].strip())
            self.procList[process][self.topColumns.PID.value] = intPID

            intPri = int(self.procList[process][self.topColumns.PRIORITY.value].strip())
            self.procList[process][self.topColumns.PRIORITY.value] = intPri

            intPri = int(self.procList[process][self.topColumns.NICE.value].strip())
            self.procList[process][self.topColumns.NICE.value] = intPri

            intPri = int(self.procList[process][self.topColumns.VIRTUALMEM.value].strip())
            self.procList[process][self.topColumns.VIRTUALMEM.value] = intPri

            intPri = int(self.procList[process][self.topColumns.RESIDENTMEM.value].strip())
            self.procList[process][self.topColumns.RESIDENTMEM.value] = intPri

            intPri = int(self.procList[process][self.topColumns.SHAREDMEM.value].strip())
            self.procList[process][self.topColumns.SHAREDMEM.value] = intPri

            intPri = float(self.procList[process][self.topColumns.CPU.value].strip())
            self.procList[process][self.topColumns.CPU.value] = intPri

            intPri = float(self.procList[process][self.topColumns.MEM.value].strip())
            self.procList[process][self.topColumns.MEM.value] = intPri


            self.procDicts.append(dict(zip(self.topColumnsNames, self.procList[process]))) 


            #print(self.procList[process])
        
        # Neste ponto, procList é uma lista de processos, e cada processo é uma lista de valores iterável
        # Neste ponto, procDicts é uma lista de dicionários, em que cada dict representa um processo, cujas chaves são topColumnsNames. 
        # A conversão para dict ocorre para facilitar a ordenação dos processos

        #print(*self.procDicts, sep = "\n")
        #print(*self.procList, sep = "\n")
        #print(repr(self.procList[5]))
        #print(topColumnsNames[topColumns.PID.value])
        return self.procList, self.procDicts

    def sortProcesses(self, keyProc = "PID"):
        self.procDicts.sort(key=lambda x: x[keyProc])
        print(*self.procDicts, sep = "\n")

        return

    def execCmd(self, cmd: str):
        proc = subprocess.Popen([cmd], stdout=subprocess.PIPE, shell=True, universal_newlines=True)
        (out, err) = proc.communicate()
        return out.strip()