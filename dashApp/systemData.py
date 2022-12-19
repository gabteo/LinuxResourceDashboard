import subprocess
import logging
import threading
import sched, time
from killSig import killSig
from memData import memData
from cpuData import cpuData
from discData import discData
from processesData import processesData


class systemData():
    def __init__(self, db) -> None:
        self.log = logging.getLogger(__name__)
        self.threadIsRunning = True
        self.killer = killSig()

        self.memoryData = memData(db)
        self.cpuData = cpuData(db)
        self.processesData = processesData(db)
        self.discData = discData(db)

        # criar thread
        self.threadName = "updateStats"
        updateFrequency = 1 #in hertz
        self.log.info("Criando thread %s", self.threadName)
        self.threadUpdateStats = threading.Thread(target=self.initThread, args=(self.threadName,updateFrequency,db,))
        self.log.info("Iniciando thread %s", self.threadName)
        self.threadUpdateStats.start()

        return

    
    
    def execCmd(self, cmd: str):
        proc = subprocess.Popen([cmd], stdout=subprocess.PIPE, shell=True, universal_newlines=True)
        (out, err) = proc.communicate()
        return out.strip()

    def updateStats(self, db):
        memStatsList, _ = self.memoryData.getMemStats()
        self.memoryData.saveMemStats(db, memStatsList)
        self.cpuData.getTotalUsage()
        self.processesData.getProcesses()
        self.processesData.sortProcesses("PID")
        pass

    
    def initThread(self, name, frequency, db):
        self.log.info("Thread %s: starting", name)
        while not (self.killer.kill_now):
            s = sched.scheduler(time.time, time.sleep)
            s.enter(frequency, 1, self.updateStats, (db,))
            s.run()
        self.log.info("Thread %s encerrada", self.threadName)
        

    def __del__(self):        
        pass



