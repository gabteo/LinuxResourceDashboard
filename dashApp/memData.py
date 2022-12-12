import subprocess
import logging
import database


class memData():
    def __init__(self, db) -> None:
        self.log = logging.getLogger(__name__)
        self.getMemStats()
        pass

    def getMemStats(self):
        dataToFetch = ["MemFree", "MemTotal", "MemAvailable", "SwapTotal", "SwapFree"]
        self.statsDict = dict.fromkeys(dataToFetch)
        for stat in dataToFetch:
            cmd = "cat /proc/meminfo | grep {0} ".format(stat)
            cmd = cmd + "| awk '{print $2}'"
            
            self.log.info(f"Executando comando: '{cmd}'")
            output = int(self.execCmd(cmd))

            #print(f"{stat}\t\t {output} kB")
            self.statsDict[stat] = output
            
        self.statsList = list(self.statsDict.values())
        
        return self.statsList, self.statsDict

    def saveMemStats(self, db: database, memStatsList: list):
        db.memTableAddRow(memStatsList)

    def execCmd(self, cmd: str):
        proc = subprocess.Popen([cmd], stdout=subprocess.PIPE, shell=True, universal_newlines=True)
        (out, err) = proc.communicate()
        return out.strip()