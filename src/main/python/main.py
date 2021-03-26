import sys

from fbs_runtime.application_context.PyQt5 import ApplicationContext
from PyQt5.QtCore import QSize
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QLabel,
    QWidget,
    QPushButton,
    QVBoxLayout
)


appctxt = ApplicationContext()       # 1. Instantiate ApplicationContext
version = appctxt.build_settings["version"]

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Hellow World v" + version)
        w = QWidget()
        layout = QVBoxLayout()
        btn = QPushButton("press")
        btn.setIconSize(QSize(20, 20))
        btn.setIcon(QIcon("../resources/256.png"))
        layout.addWidget(btn)
        w.setLayout(layout)

        self.setCentralWidget(w)


if __name__ == '__main__':
    window = MainWindow()
    window.show()
    exit_code = appctxt.app.exec_()      # 2. Invoke appctxt.app.exec_()
    sys.exit(exit_code)
