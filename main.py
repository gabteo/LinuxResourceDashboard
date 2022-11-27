from dashboard import *
import os
from defines import defines

if __name__ == '__main__':
    #root.mainloop()     # event loop
    print("Home dir: " + defines.home)
    if(not (os.path.isdir(defines.CMD_FILES_PATH))):
        os.system("mkdir "+ defines.CMD_FILES_PATH)
    app = App()
    app.mainloop()

