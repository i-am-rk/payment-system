import sys

from fbs_runtime.application_context.PyQt5 import ApplicationContext
from PyQt5.QtCore import QSize, Qt, pyqtSignal, QThreadPool, pyqtSlot
from PyQt5.QtGui import QPixmap, QIcon, QImage
from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QLabel,
    QWidget,
    QPushButton,
    QVBoxLayout,
    QSizePolicy
)
import numpy as np
sys.path.append("/home/liam/Project/payment-system/")

# import ui files
from UI import mainwindow
# from UI.ui_functions import UI_Functions as uif
from UI import ui_functions as uif
import globalvariables as gv 

from UI.Pages import page1
# 1. Instantiate ApplicationContext
appctxt = ApplicationContext()       
version = appctxt.build_settings["version"]

from threads import FeedWorker

# Main Window
class MainWindow(QMainWindow, mainwindow.Ui_MainWindow):
    def __init__(self, *args, obj=None, **Kwargs):
        super(MainWindow, self).__init__(*args, **Kwargs)
        self.setWindowFlags(Qt.WindowCloseButtonHint | Qt.WindowMinimizeButtonHint)
        self.setupUi(self)
        sizePolicy = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding)
        self.setSizePolicy(sizePolicy)
        self.setGeometry(0, 0,gv.WIDTH, gv.HEIGHT)
        self.setMaximumSize(QSize(gv.WIDTH, gv.HEIGHT))
        ###################################################################################
        #region MainWindow SETUP                                                          

        # Toggle function
        self.menu_toggle_btn.clicked.connect(lambda status, self = self:uif.toggle_menu(self, status))
        
        #Page change settings
        self.home_btn.clicked.connect(lambda status,  self = self, idx = 0:uif.change_page(self, idx, status))
        self.anchor_btn.clicked.connect(lambda status, self = self, idx = 1:uif.change_page(self, idx, status ))
        self.sub_btn.clicked.connect(lambda status, self = self, idx = 2:uif.change_page(self, idx, status ))
        self.settings_btn.clicked.connect(lambda status, self = self, idx = 3:uif.change_page(self, idx, status ))
        self.add_btn.clicked.connect(lambda status, self = self, idx = 4:uif.change_page(self, idx, status ))
        
        #endregion MainWindow SETUP                                                           
        ###################################################################################
        
        #######################################################################
        #region PAGE ONE CONFIG

        # define Slot for update image
        @pyqtSlot()
        def update_image(cv_image):
            qt_img = convert_cv_to_qt(cv_image)
            self.page1.feed.setPixmap(qt_img)

        def convert_cv_to_qt(img):
            h, w, ch = img.shape
            bytes_per_line = ch * w
            convert_cv_to_Qt_format = QImage(img.data, w, h, QImage.Format_RGB888)
            p = convert_cv_to_Qt_format.scaled(gv.FeedWidth, gv.FeedHeight, Qt.KeepAspectRatio)
            return QPixmap.fromImage(p)
        
        self.feed_img = None
        self.feedthread = QThreadPool()
        print(self.feedthread.maxThreadCount())
        self.feedWorker = FeedWorker()
        self.feedWorker.signals.cv_image.connect(update_image)
        self.feedthread.start(self.feedWorker)

        # @pyqtSlot()
        # def update_image(cv_image):
        #     qt_img = convert_cv_to_qt(cv_image)
        #     print("update")
        #     self.page1.feed.setPixmap(qt_img)

        # def convert_cv_to_qt(img):
        #     h, w, ch = img.shape
        #     bytes_per_line = ch * w
        #     convert_cv_to_Qt_format = QImage(img.data, w, h, QImage.Format_RGB888)
        #     p = convert_cv_to_Qt_format.scaled(gv.FeedWidth, gv.FeedHeight, Qt.KeepAspectRatio)
        #     return QPixmap.fromImage(p)
        #endregion PAGE ON CONFIG
        ########################################################################

if __name__ == '__main__':
    window = MainWindow()
    window.show()
    exit_code = appctxt.app.exec_()      # 2. Invoke appctxt.app.exec_()
    sys.exit(exit_code)
# self.show()