import subprocess
import logging

class discData():
    def __init__(self, db) -> None:
        self.log = logging.getLogger(__name__)
        self.getDiscUsage()
        pass

    def getDiscUsage(self):
       
        # dataToFetch = ["MemFree", "MemTotal", "MemAvailable", "SwapTotal", "SwapFree"]
        # self.statsDict = dict.fromkeys(dataToFetch)
        # for stat in dataToFetch:
        #     cmd = "cat /proc/meminfo | grep {0} ".format(stat)
        #     cmd = cmd + "| awk '{print $2}'"
            
        #     self.log.info(f"Executando comando: '{cmd}'")
        #     output = int(self.execCmd(cmd))

        #     #print(f"{stat}\t\t {output} kB")
        #     self.statsDict[stat] = output
            
        # self.statsList = list(self.statsDict.values())

        # listaNome, listaTotal, listaAvailable
        cmd = "df -h --type=ext4"
        output = self.execCmd(cmd)
        lines = output.splitlines()
        lines.pop(0)
        count = len(lines)
        self.listaName = []
        self.listaTotal = []
        self.listaLivre = []
        self.listaUsado = []
        for line in lines:
            dados = line.split(" ")
            self.listaName.append(dados[0])
            total = int(dados[8].replace("G",""))
            self.listaTotal.append(total)
            livre = int(dados[11].replace("G",""))
            self.listaLivre.append(livre)
            usado = total - livre
            self.listaUsado.append(usado)

        return self.listaName, self.listaTotal, self.listaLivre, self.listaUsado
        # return self.statsList, self.statsDict

    def execCmd(self, cmd: str) -> str:
        proc = subprocess.Popen([cmd], stdout=subprocess.PIPE, shell=True, universal_newlines=True)
        (out, err) = proc.communicate()
        return out.strip()