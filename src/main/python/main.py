import sys

from fbs_runtime.application_context.PyQt5 import ApplicationContext
from PyQt5.QtCore import QSize, Qt
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QLabel,
    QWidget,
    QPushButton,
    QVBoxLayout
)
sys.path.append("/home/liam/Project/payment-system/")

import UI

appctxt = ApplicationContext()       # 1. Instantiate ApplicationContext
version = appctxt.build_settings["version"]
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        UI.ui_1.test_function()
if __name__ == '__main__':
    window = MainWindow()
    window.show()
    exit_code = appctxt.app.exec_()      # 2. Invoke appctxt.app.exec_()
    sys.exit(exit_code)
