# -*- coding: utf-8 -*-
# Form implementation generated from reading ui file 'UI/Pages/page1.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtWidgets
from PyQt5.QtSql import QSqlDatabase, QSqlQuery

from UI import ui_fun_classes as uif
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
        self.top_bar.setMaximumHeight(60)

        self.search_bar = QtWidgets.QLineEdit()
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
        self.frame_b = QtWidgets.QFrame()
        self.frame_b.setContentsMargins(0, 0, 0, 0)
        self.frame_b.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_b.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_b.setLineWidth(0)

        self.frame_b_layout = QtWidgets.QHBoxLayout()
        self.frame_b_layout.setContentsMargins(0, 0, 0, 0)
        self.frame_b_layout.setSpacing(0)

        # Set Tabel
        db_labels = ["Id", "First Name", "Last Name", "Gender", "DOB", "Email", "Mob. Number", "Balance" ]
        self.db_table = uif.MySqlQTableWidget(cols=8, labels=db_labels)
        self.frame_b_layout.addWidget(self.db_table)

        # table options buttons
        self.vl1 = QtWidgets.QVBoxLayout()
        self.vl1.setContentsMargins(5, 20, 5, 5)
        self.vl1.setSpacing(5)
        self.edit_btn = QtWidgets.QPushButton("Edit")
        self.delete_btn = QtWidgets.QPushButton("Delete")
        self.reload_btn = QtWidgets.QPushButton("Reload")
        spacer = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)

        self.vl1.addWidget(self.reload_btn) # reload button
        self.vl1.addWidget(self.edit_btn) # edit button
        self.vl1.addWidget(self.delete_btn) # delete button
        self.vl1.addItem(spacer)
        self.frame_b_layout.addLayout(self.vl1)
        self.frame_b.setLayout(self.frame_b_layout)
        #endregion DATA TABLE
        ####################################################################
        self.vertical_layout.addWidget(self.frame_b)

# import resource_rc 
from UI import resource_rc
