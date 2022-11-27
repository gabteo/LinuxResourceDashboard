from pathlib import Path


class defines():
    home = str(Path.home())
    #CMD_FILES_PATH = "$HOME/LRD"
    CMD_FILES_PATH = home + "/LRD"
    
    def __init__(self) -> None:
        pass
    