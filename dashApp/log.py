import logging
import sys

def loggerSetup():
        formatter = logging.Formatter('%(asctime)s [%(levelname)s] %(message)s (in module %(name)s).')
        
        logging.basicConfig(level=logging.WARNING, format="%(asctime)s [%(levelname)s] %(message)s (in module %(name)s).", datefmt="%H:%M:%S")
        

        log = logging.getLogger()

        """ consoleHandler = logging.StreamHandler(sys.stdout)
        consoleHandler.setFormatter(formatter)
        consoleHandler.setLevel(logging.DEBUG)
        log.addHandler(consoleHandler) """

        fileHandler = logging.FileHandler(filename="log.log", mode='w', encoding=None, delay=False)
        fileHandler.setFormatter(formatter)
        fileHandler.setLevel(logging.WARNING)
        log.addHandler(fileHandler)


