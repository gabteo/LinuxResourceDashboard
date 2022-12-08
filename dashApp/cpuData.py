import subprocess
import logging
import database

class cpuData():
    # https://man7.org/linux/man-pages/man1/top.1.html
    def __init__(self, db) -> None:
        self.log = logging.getLogger(__name__)
        #self.getCpuStats()
        self.getNumberOfCores()
        db.CPUTableAddCores(self.cores)
        pass

    def getCpuStats(self):
        self.cores = self.getNumberOfCores()
        self.totalUsage = self.getTotalUsage()

        dataToFetch = ["MemFree", "MemTotal", "MemAvailable", "SwapTotal", "SwapFree"]
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

    def getNumberOfCores(self):
        # man 2b
        cmd = "top -n 1 -b -1 | grep Cpu | wc | awk '{print $1}'"
        self.log.info(f"Executando comando: '{cmd}'")
        self.cores = int(self.execCmd(cmd))
        return self.cores

    def getTotalUsage(self):
        # man 2b
        cmd = """top -bn1 | grep '%Cpu' |awk -F , '{print $4}' | awk '{print $1}'"""
        self.log.info(f"""Executando comando: '{cmd}'""")
        self.totalUsage = 100 - float(self.execCmd(cmd))
        self.totalUsage = float(f"{self.totalUsage:0.3f}")
        #print(f"{self.totalUsage:0.2f}")
        print(self.totalUsage)
        return self.totalUsage

    def execCmd(self, cmd: str) -> str:
        proc = subprocess.Popen([cmd], stdout=subprocess.PIPE, shell=True, universal_newlines=True)
        (out, err) = proc.communicate()
        return out.strip()