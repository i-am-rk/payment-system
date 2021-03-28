# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI/main_ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
        def __init__(self):
                pass
        def setupUi(self, MainWindow):
                MainWindow.setObjectName("MainWindow")
                MainWindow.resize(800, 602)
                self.centralwidget = QtWidgets.QWidget(MainWindow)
                self.centralwidget.setStyleSheet("QWidget{\n"
        "background-color: rgb(255, 255, 255);\n"
        "}")
                self.centralwidget.setObjectName("centralwidget")
                self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
                self.verticalLayout.setContentsMargins(0, 0, 0, 0)
                self.verticalLayout.setSpacing(0)
                self.verticalLayout.setObjectName("verticalLayout")
#------------------top-bar------------------
                self.top_bar = QtWidgets.QFrame(self.centralwidget)
                self.top_bar.setMinimumSize(QtCore.QSize(0, 50))
                self.top_bar.setMaximumSize(QtCore.QSize(16777215, 50))
                self.top_bar.setStyleSheet("")
                self.top_bar.setFrameShape(QtWidgets.QFrame.NoFrame)
                self.top_bar.setFrameShadow(QtWidgets.QFrame.Plain)
                self.top_bar.setLineWidth(0)
                self.top_bar.setObjectName("top_bar")
# ------------------shadow settings start------------------------
                shadow = QtWidgets.QGraphicsDropShadowEffect()
                shadow.setColor(QtGui.QColor(50, 50, 50))
                shadow.setBlurRadius(10)
                shadow.setXOffset(0)
                shadow.setYOffset(2)
# ----------------shadows settings end----------------------
                self.top_bar.setGraphicsEffect(shadow)
                self.horizontalLayout = QtWidgets.QHBoxLayout(self.top_bar)
                self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
                self.horizontalLayout.setSpacing(0)
                self.horizontalLayout.setObjectName("horizontalLayout")
                self.menu_toggle_btn = QtWidgets.QPushButton(self.top_bar)
                self.menu_toggle_btn.setMaximumSize(QtCore.QSize(50, 50))
                self.menu_toggle_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
                self.menu_toggle_btn.setStyleSheet("QPushButton{\n"
        "background-color: #00F506;\n"
        "border:none;\n"
        "background-image: url(:/Icons/Icons/menu.png);\n"
        "background-repeat:no-repeat;\n"
        "background-position:center;\n"
        "}")
                self.menu_toggle_btn.setText("")
                self.menu_toggle_btn.setCheckable(True)
                self.menu_toggle_btn.setObjectName("menu_toggle_btn")
                self.horizontalLayout.addWidget(self.menu_toggle_btn)
                self.available_label = QtWidgets.QLabel(self.top_bar)
                font = QtGui.QFont()
                font.setBold(True)
                font.setWeight(75)

                menu_font = QtGui.QFont()
                menu_font.setBold(True)
                menu_font.setWeight(65)
                menu_font.setPointSize(11)

                self.available_label.setFont(font)
                self.available_label.setAlignment(QtCore.Qt.AlignCenter)
                self.available_label.setObjectName("available_label")
                self.horizontalLayout.addWidget(self.available_label)
                self.time_label = QtWidgets.QLabel(self.top_bar)
                font = QtGui.QFont()
                font.setBold(True)
                font.setWeight(75)
                self.time_label.setFont(font)
                self.time_label.setAlignment(QtCore.Qt.AlignCenter)
                self.time_label.setObjectName("date_label")
                self.horizontalLayout.addWidget(self.time_label)
                self.date_label = QtWidgets.QLabel(self.top_bar)
                font = QtGui.QFont()
                font.setBold(True)
                font.setWeight(75)
                self.date_label.setFont(font)
                self.date_label.setAlignment(QtCore.Qt.AlignCenter)
                self.date_label.setObjectName("time_label")
                self.horizontalLayout.addWidget(self.date_label)
                self.frame = QtWidgets.QFrame(self.top_bar)
                self.frame.setMaximumSize(QtCore.QSize(50, 16777215))
                self.frame.setFrameShape(QtWidgets.QFrame.NoFrame)
                self.frame.setFrameShadow(QtWidgets.QFrame.Plain)
                self.frame.setLineWidth(0)
                self.frame.setObjectName("frame")
                self.horizontalLayout.addWidget(self.frame)
                self.verticalLayout.addWidget(self.top_bar)
                self.main_container = QtWidgets.QFrame(self.centralwidget)
                self.main_container.setFrameShape(QtWidgets.QFrame.NoFrame)
                self.main_container.setFrameShadow(QtWidgets.QFrame.Plain)
                self.main_container.setLineWidth(0)
                self.main_container.setObjectName("main_container")
                self.main_container.lower()
                self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.main_container)
                self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
                self.horizontalLayout_2.setSpacing(0)
                self.horizontalLayout_2.setObjectName("horizontalLayout_2")
                self.menus = QtWidgets.QFrame(self.main_container)
                self.menus.setMinimumSize(QtCore.QSize(0, 0))
                self.menus.setMaximumSize(QtCore.QSize(46, 16777215))
                self.menus.setStyleSheet("QFrame{\n"
        "background-color:#F5F5F5;\n"
        "}")
                self.menus.setFrameShape(QtWidgets.QFrame.NoFrame)
                self.menus.setFrameShadow(QtWidgets.QFrame.Plain)
                self.menus.setLineWidth(0)
                self.menus.setObjectName("menus")
                self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.menus)
                self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
                self.verticalLayout_2.setSpacing(0)
                self.verticalLayout_2.setObjectName("verticalLayout_2")
                self.home_btn = QtWidgets.QPushButton(self.menus)
                self.home_btn.setMinimumSize(QtCore.QSize(0, 50))
                self.home_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
                self.home_btn.setStyleSheet("QPushButton{\n"
        "    background-image: url(:/Icons/Icons/home.png);\n"
        "    background-position: left center;\n"
        "    background-repeat: no-repeat;\n"
        "    background-color: none;\n"
        "    text-align: left;\n"
        "    padding-left: 45px;\n"
        "    border:none;\n"
        "    border-left: 8px solid none;\n"
        "}\n"
        "QPushButton:hover{\n"
        "    background-color:#1FB141;\n"
        "    border-left:8px solid #1FB141;\n"
        "    color:#FFFFFF;\n"
        "}\n"
        "QPushButton:pressed{\n"
        "    background-color:#1FB141;\n"
        "    border-left:8px solid #1FB141;\n"
        "}")
                self.home_btn.setCheckable(True)
                self.home_btn.setFont(menu_font)
                self.home_btn.setObjectName("home_btn")
                self.verticalLayout_2.addWidget(self.home_btn)
                self.anchor_btn = QtWidgets.QPushButton(self.menus)
                self.anchor_btn.setMinimumSize(QtCore.QSize(0, 50))
                self.anchor_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
                self.anchor_btn.setStyleSheet("QPushButton{\n"
        "    background-image: url(:/Icons/Icons/anchor.png);\n"
        "    background-position: left center;\n"
        "    background-repeat: no-repeat;\n"
        "    background-color: none;\n"
        "    text-align: left;\n"
        "    padding-left: 45px;\n"
        "    border:none;\n"
        "    border-left: 8px solid none;\n"
        "}\n"
        "QPushButton:hover{\n"
        "    background-color:#1FB141;\n"
        "    border-left:8px solid #1FB141;\n"
        "    color:#FFFFFF;\n"
        "}\n"
        "QPushButton:pressed{\n"
        "    background-color:#1FB141;\n"
        "    border-left:8px solid #1FB141;\n"
        "}")

                self.anchor_btn.setCheckable(True)
                self.anchor_btn.setFont(menu_font)
                self.anchor_btn.setObjectName("anchor_btn")
                self.verticalLayout_2.addWidget(self.anchor_btn)
                self.sub_btn = QtWidgets.QPushButton(self.menus)
                self.sub_btn.setMinimumSize(QtCore.QSize(0, 50))
                self.sub_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
                self.sub_btn.setStyleSheet("QPushButton{\n"
        "    background-image: url(:/Icons/Icons/sub.png);\n"
        "    background-position: left center;\n"
        "    background-repeat: no-repeat;\n"
        "    background-color: none;\n"
        "    text-align: left;\n"
        "    padding-left: 45px;\n"
        "    border:none;\n"
        "    border-left: 8px solid none;\n"
        "}\n"
        "QPushButton:hover{\n"
        "    background-color:#1FB141;\n"
        "    border-left:8px solid #1FB141;\n"
        "    color:#FFFFFF;\n"
        "}\n"
        "QPushButton:pressed{\n"
        "    background-color:#1FB141;\n"
        "    border-left:8px solid #1FB141;\n"
        "}")
                self.sub_btn.setCheckable(True)
                self.sub_btn.setFont(menu_font)
                self.sub_btn.setObjectName("sub_btn")
                self.verticalLayout_2.addWidget(self.sub_btn)
                self.settings_btn = QtWidgets.QPushButton(self.menus)
                self.settings_btn.setMinimumSize(QtCore.QSize(0, 50))
                self.settings_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
                self.settings_btn.setStyleSheet("QPushButton{\n"
        "    background-image: url(:/Icons/Icons/settings.png);\n"
        "    background-position: left center;\n"
        "    background-repeat: no-repeat;\n"
        "    background-color: none;\n"
        "    text-align: left;\n"
        "    padding-left: 45px;\n"
        "    border:none;\n"
        "    border-left: 8px solid none;\n"
        "}\n"
        "QPushButton:hover{\n"
        "    background-color:#1FB141;\n"
        "    border-left:8px solid #1FB141;\n"
        "    color:#FFFFFF;\n"
        "}\n"
        "QPushButton:pressed{\n"
        "    background-color:#1FB141;\n"
        "    border-left:8px solid #1FB141;\n"
        "}")
                self.settings_btn.setCheckable(True)
                self.settings_btn.setFont(menu_font)
                self.settings_btn.setObjectName("settings_btn")
                self.verticalLayout_2.addWidget(self.settings_btn)
                self.add_btn = QtWidgets.QPushButton(self.menus)
                self.add_btn.setMinimumSize(QtCore.QSize(0, 50))
                self.add_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
                self.add_btn.setStyleSheet("QPushButton{\n"
        "    background-image: url(:/Icons/Icons/add.png);\n"
        "    background-position: left center;\n"
        "    background-repeat: no-repeat;\n"
        "    background-color: none;\n"
        "    text-align: left;\n"
        "    padding-left: 45px;\n"
        "    border:none;\n"
        "    border-left: 8px solid none;\n"
        "}\n"
        "QPushButton:hover{\n"
        # "    background-color:#00F506;\n"
        "    background-color:#1FB141;\n"
        "    border-left:8px solid #1FB141;\n"
        "    color:#FFFFFF;\n"
        "}\n"
        "QPushButton:pressed{\n"
        "    background-color:#1FB141;\n"
        "    border-left:8px solid #1FB141;\n"
        "}")
                self.add_btn.setCheckable(True)
                self.add_btn.setFont(menu_font)
                self.add_btn.setObjectName("add_btn")
                self.verticalLayout_2.addWidget(self.add_btn)
                spacerItem = QtWidgets.QSpacerItem(20, 299, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
                self.verticalLayout_2.addItem(spacerItem)
                self.horizontalLayout_2.addWidget(self.menus)
                self.divider = QtWidgets.QFrame(self.main_container)
                self.divider.setMinimumSize(QtCore.QSize(4, 0))
                self.divider.setMaximumSize(QtCore.QSize(4, 16777215))
                self.divider.setStyleSheet("QFrame{\n"
        "background-color: #00F506;\n"
        "}")
                self.divider.setFrameShape(QtWidgets.QFrame.NoFrame)
                self.divider.setFrameShadow(QtWidgets.QFrame.Plain)
                self.divider.setLineWidth(0)
                self.divider.setObjectName("divider")
                self.horizontalLayout_2.addWidget(self.divider)
# -----------------Pages setup-------------------
                self.Pages = QtWidgets.QStackedWidget(self.main_container)
                self.Pages.setObjectName("Pages")

                # Page One
                self.page1 = QtWidgets.QWidget()
                self.page1.setObjectName("page1")
                self.page1.setStyleSheet("QWidget{background-color:red;}")
                self.label_5 = QtWidgets.QLabel(self.page1)
                self.label_5.setGeometry(QtCore.QRect(320, 210, 141, 51))
                self.label_5.setAlignment(QtCore.Qt.AlignCenter)
                self.label_5.setObjectName("label_5")
                self.Pages.addWidget(self.page1)

                # Page Two
                self.page2 = QtWidgets.QWidget()
                self.page2.setObjectName("page_2")
                self.label_4 = QtWidgets.QLabel(self.page2)
                self.label_4.setGeometry(QtCore.QRect(360, 220, 141, 51))
                self.label_4.setAlignment(QtCore.Qt.AlignCenter)
                self.label_4.setObjectName("label_4")
                self.Pages.addWidget(self.page2)

                # Page Three
                self.page3 = QtWidgets.QWidget()
                self.page3.setObjectName("page_3")
                self.label_6 = QtWidgets.QLabel(self.page3)
                self.label_6.setGeometry(QtCore.QRect(360, 220, 141, 51))
                self.label_6.setAlignment(QtCore.Qt.AlignCenter)
                self.label_6.setObjectName("label_6")
                self.Pages.addWidget(self.page3)

                # Page Four
                self.page4 = QtWidgets.QWidget()
                self.page4.setObjectName("page_4")
                self.label_7 = QtWidgets.QLabel(self.page4)
                self.label_7.setGeometry(QtCore.QRect(360, 220, 141, 51))
                self.label_7.setAlignment(QtCore.Qt.AlignCenter)
                self.label_7.setObjectName("label_4")
                self.Pages.addWidget(self.page4)

                # Page Five
                self.page5 = QtWidgets.QWidget()
                self.page5.setObjectName("page_5")
                self.label_8 = QtWidgets.QLabel(self.page5)
                self.label_8.setGeometry(QtCore.QRect(360, 220, 141, 51))
                self.label_8.setAlignment(QtCore.Qt.AlignCenter)
                self.label_8.setObjectName("label_6")
                self.Pages.addWidget(self.page5)
                
                self.horizontalLayout_2.addWidget(self.Pages)
                self.verticalLayout.addWidget(self.main_container)
                MainWindow.setCentralWidget(self.centralwidget)

                self.retranslateUi(MainWindow)
                self.Pages.setCurrentIndex(3)
                QtCore.QMetaObject.connectSlotsByName(MainWindow)

        def retranslateUi(self, MainWindow):
                _translate = QtCore.QCoreApplication.translate
                MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))

                self.available_label.setText(_translate("MainWindow", "Available"))
                self.time_label.setText(_translate("MainWindow", "Time"))
                self.date_label.setText(_translate("MainWindow", "Date"))

                self.home_btn.setToolTip(_translate("MainWindow", "Home"))
                self.home_btn.setText(_translate("MainWindow", "Home"))
                self.anchor_btn.setToolTip(_translate("MainWindow", "Parked"))
                self.anchor_btn.setText(_translate("MainWindow", "Parked"))
                self.sub_btn.setToolTip(_translate("MainWindow", "Customers"))
                self.sub_btn.setText(_translate("MainWindow", "Customers"))
                self.settings_btn.setToolTip(_translate("MainWindow", "Settings"))
                self.settings_btn.setText(_translate("MainWindow", "Settings"))
                self.add_btn.setToolTip(_translate("MainWindow", "Add Customer"))
                self.add_btn.setText(_translate("MainWindow", "Add Customer"))

                self.label_5.setText(_translate("MainWindow", "Page one"))
                self.label_4.setText(_translate("MainWindow", "Page Two"))
                self.label_6.setText(_translate("MainWindow", "Page Three"))
                self.label_7.setText(_translate("MainWindow", "Page Four"))
                self.label_8.setText(_translate("MainWindow", "Page Five"))
# import resource_rc 
from UI import resource_rc
