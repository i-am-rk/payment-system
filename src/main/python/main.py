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

# import ui files
from UI import mainwindow 

# 1. Instantiate ApplicationContext
appctxt = ApplicationContext()       
version = appctxt.build_settings["version"]

# Main Window
class MainWindow(QMainWindow, mainwindow.Ui_MainWindow):
    def __init__(self, *args, obj=None, **Kwargs):
        super(MainWindow, self).__init__(*args, **Kwargs)
        self.setupUi(self)
        
if __name__ == '__main__':
    window = MainWindow()
    window.show()
    exit_code = appctxt.app.exec_()      # 2. Invoke appctxt.app.exec_()
    sys.exit(exit_code)
