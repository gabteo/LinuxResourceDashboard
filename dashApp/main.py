from log import loggerSetup
from database import database
import logging
from systemData import *


def main():
    loggerSetup()
    log = logging.getLogger()
    log.info("main init")
    db = database.database()
    memStats = systemData(db)
    


if __name__ == '__main__':
    main()