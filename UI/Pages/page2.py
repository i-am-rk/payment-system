# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI/Pages/page1.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from pathlib import Path
import json

# class Ui_Page(object):
class Ui_Page(QtWidgets.QWidget):
    def setupUi(self, Page):
        Page.setObjectName("Page")
        Page.resize(1000, 550)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Page.sizePolicy().hasHeightForWidth())
        Page.setSizePolicy(sizePolicy)

        self.vertical_layout = QtWidgets.QVBoxLayout(Page)
        self.vertical_layout.setContentsMargins(0, 0, 0, 0)
        self.vertical_layout.setSpacing(0)
        self.setObjectName("verticalLayout")

        #####################################################################
        #region TOP BAR
        self.top_bar = QtWidgets.QFrame(Page)
        self.top_bar.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.top_bar.setFrameShadow(QtWidgets.QFrame.Plain)
        self.top_bar.setLineWidth(0)

        self.search_bar = QtWidgets.QTextEdit()
        self.search_btn = QtWidgets.QPushButton("Search")

        hlayout = QtWidgets.QHBoxLayout()
        hlayout.addWidget(self.search_bar)
        hlayout.addWidget(self.search_btn)

        self.top_bar.setLayout(hlayout)
        #endregion TOP BAR
        ####################################################################
        self.vertical_layout.addWidget(self.top_bar)
        
        #####################################################################
        #region DATA TABLE
        # start
        #endregion DATA TABLE
        ####################################################################

        
   
# import resource_rc 
from UI import resource_rc
