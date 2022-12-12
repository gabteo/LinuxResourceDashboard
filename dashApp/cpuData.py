import subprocess
import logging
import database

class cpuData():
    # https://man7.org/linux/man-pages/man1/top.1.html
    def __init__(self, db) -> None:
        self.log = logging.getLogger(__name__)
        #self.getCpuStats()
        #self.getNumberOfCores()
        self.getCpuInfo()
        self.cores = self.getCores()
        db.CPUTableAddCores(self.cores)
        pass

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
        #print(self.totalUsage)
        return self.totalUsage

    def execCmd(self, cmd: str) -> str:
        proc = subprocess.Popen([cmd], stdout=subprocess.PIPE, shell=True, universal_newlines=True)
        (out, err) = proc.communicate()
        return out.strip()

    

    def getCpuInfo(self):
        dataToFetch = ['"Architecture"', '"CPU(s):"', '"Thread(s) per core"', '"Core(s) per socket"', '"Model name"', '"CPU MHz"']
        self.cpuInfoDict = dict.fromkeys(dataToFetch)
        for field in dataToFetch:
            cmd = "lscpu | grep {0} ".format(field)
            cmd = cmd + "| awk -F ':' '{print $2}'"
            
            self.log.info(f"Executando comando: '{cmd}'")
            output = self.execCmd(cmd)

            print(f"{field}\t\t {output}")
            self.cpuInfoDict[field] = output
            
        self.cpuInfoList = list(self.cpuInfoDict.values())

        return self.cpuInfoList, self.cpuInfoDict


    def getArchitecture(self):
        #self.getCpuInfo()
        try:
            self.architecture = self.cpuInfoDict['"Architecture"']
        except:
            self.log.error("getCpuInfo() ainda não foi executada!")
        return self.architecture

    def getCores(self):
        #self.getCpuInfo()
        try:
            self.cores = self.cpuInfoDict['"CPU(s):"']
        except:
            self.log.error("getCpuInfo() ainda não foi executada!")
        return self.cores

    def getThreadsPerCore(self):
        #self.getCpuInfo()
        try:
            self.ThreadsPerCore = self.cpuInfoDict['"Thread(s) per core"']
        except:
            self.log.error("getCpuInfo() ainda não foi executada!")
        return self.ThreadsPerCore

    def getCoresPerSocket(self):
        #self.getCpuInfo()
        try:
            self.coresPerSocket = self.cpuInfoDict['"Core(s) per socket"']
        except:
            self.log.error("getCpuInfo() ainda não foi executada!")
        return self.coresPerSocket

    def getModelNamet(self):
        #self.getCpuInfo()
        try:
            self.modelName = self.cpuInfoDict['"Model name"']
        except:
            self.log.error("getCpuInfo() ainda não foi executada!")
        return self.modelName

    def getCpuMhz(self):
        #self.getCpuInfo()
        try:
            self.cpuMhz = self.cpuInfoDict['"CPU MHz"']
        except:
            self.log.error("getCpuInfo() ainda não foi executada!")
        return self.cpuMhz