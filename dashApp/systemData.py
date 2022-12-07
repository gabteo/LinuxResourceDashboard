from abc import abstractmethod
import subprocess
import logging
import threading
import sched, time

class systemData():
    def __init__(self) -> None:
        self.log = logging.getLogger(__name__)
        self.threadIsRunning = True

        self.memoryData = memData()

        # criar thread
        self.threadName = "updateStats"
        updateFrequency = 1 #in hertz
        self.log.info("Criando thread %s", self.threadName)
        self.threadUpdateStats = threading.Thread(target=self.initThread, args=(self.threadName,updateFrequency,))
        self.log.info("Iniciando thread %s", self.threadName)
        self.threadUpdateStats.start()

        return

    def saveData(self):
        pass
    
    def execCmd(self, cmd: str):
        proc = subprocess.Popen([cmd], stdout=subprocess.PIPE, shell=True, universal_newlines=True)
        (out, err) = proc.communicate()
        return out.strip()

    def updateStats(self):
        self.memoryData.getMemStats()
        pass

    
    def initThread(self,  name, frequency):
        self.log.info("Thread %s: starting", name)
        while(self.threadIsRunning):
            s = sched.scheduler(time.time, time.sleep)
            s.enter(frequency, 1, self.updateStats, ())
            s.run()
        
        self.log.info("Thread %s: finishing", name)
        

    def __del__(self):
        self.threadIsRunning = False
        self.threadUpdateStats.join()
        self.log.info("Thread %s encerrada", self.threadName)

        pass

class memData():
    def __init__(self) -> None:
        self.log = logging.getLogger(__name__)
        self.getMemStats()
        pass

    def getMemStats(self):
        dataToFetch = ["MemFree", "MemTotal", "MemAvailable"]
        self.statsDict = dict.fromkeys(dataToFetch)
        for stat in dataToFetch:
            cmd = "cat /proc/meminfo | grep {0} ".format(stat)
            cmd = cmd + "| awk '{print $2}'"
            
            self.log.info(f"Executando comando: '{cmd}'")
            output = self.execCmd(cmd)

            print(f"{stat}\t\t {output} kB")
            self.statsDict[stat] = output
            
        self.statsList = list(self.statsDict.values())

        return self.statsList, self.statsDict


    def execCmd(self, cmd: str):
        proc = subprocess.Popen([cmd], stdout=subprocess.PIPE, shell=True, universal_newlines=True)
        (out, err) = proc.communicate()
        return out.strip()