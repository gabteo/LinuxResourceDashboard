from log import loggerSetup
from database import database
import logging
from systemData import *


def main():
    loggerSetup()
    log = logging.getLogger()
    log.info("main init")
db = database()
data = systemData(db)
    
print("numero cores" + data.cpuData.getCores())

if __name__ == '__main__':
    main()


    #df -h --type=ext4  --output