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
# from UI.ui_functions import UI_Functions as uif
from UI import ui_functions as uif

# 1. Instantiate ApplicationContext
appctxt = ApplicationContext()       
version = appctxt.build_settings["version"]

# Main Window
class MainWindow(QMainWindow, mainwindow.Ui_MainWindow):
    def __init__(self, *args, obj=None, **Kwargs):
        super(MainWindow, self).__init__(*args, **Kwargs)
        self.setupUi(self)
        self.home_btn.styleSheet
        # Toggle function
        self.menu_toggle_btn.clicked.connect(lambda status, self = self:uif.toggle_menu(self, status))
        
# ------------Page change settings---------------
        # calling change page function and 
        # pass list of btns and SELF, 
        self.home_btn.clicked.connect(lambda status,  self = self, idx = 0:uif.change_page(self, idx, status))
        self.anchor_btn.clicked.connect(lambda status, self = self, idx = 1:uif.change_page(self, idx, status ))
        self.sub_btn.clicked.connect(lambda status, self = self, idx = 2:uif.change_page(self, idx, status ))
        self.settings_btn.clicked.connect(lambda status, self = self, idx = 3:uif.change_page(self, idx, status ))
        self.add_btn.clicked.connect(lambda status, self = self, idx = 4:uif.change_page(self, idx, status ))
        
    def test(self,obj, x, btn):
        print(x)
        print(obj)
        print(self)
        btn.setEnabled(False)

if __name__ == '__main__':
    window = MainWindow()
    window.show()
    exit_code = appctxt.app.exec_()      # 2. Invoke appctxt.app.exec_()
    sys.exit(exit_code)
