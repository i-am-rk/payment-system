import sys

from fbs_runtime.application_context.PyQt5 import ApplicationContext
from PyQt5.QtWidgets import QMainWindow


appctxt = ApplicationContext()       # 1. Instantiate ApplicationContext
version = appctxt.build_settings["version"]

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Hellow World v" + version)

        self.resize(250, 120)

    

if __name__ == '__main__':
    window = MainWindow()
    window.show()
    exit_code = appctxt.app.exec_()      # 2. Invoke appctxt.app.exec_()
    sys.exit(exit_code)