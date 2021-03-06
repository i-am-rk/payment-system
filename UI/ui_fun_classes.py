from os import PRIO_PGRP
from PyQt5 import QtWidgets
from PyQt5.QtCore import(
    QPropertyAnimation,
    Qt
)
from pathlib import Path, WindowsPath
import json
############################################
#region Variables
GLOBAL_SIDE_PANEL_LENTH = 160
#endregion Variables
############################################



########################################################################
#region Toggle Menu
#FUNCTION:Toggle Menu
def toggle_menu(self, status):
    if status:
        self.anim1 = QPropertyAnimation(self.menus, b"maximumWidth")
        self.anim2 = QPropertyAnimation(self.menus, b"minimumWidth")

        self.anim1.setDuration(300)
        self.anim2.setDuration(300)

        self.anim1.setStartValue(46)
        self.anim2.setStartValue(46)
        
        self.anim1.setEndValue(GLOBAL_SIDE_PANEL_LENTH)
        self.anim2.setEndValue(GLOBAL_SIDE_PANEL_LENTH)
        
        self.anim1.start()
        self.anim2.start()
    else:
        self.anim1 = QPropertyAnimation(self.menus, b"maximumWidth")
        self.anim2 = QPropertyAnimation(self.menus, b"minimumWidth")

        self.anim1.setDuration(300)
        self.anim2.setDuration(300)

        self.anim1.setStartValue(GLOBAL_SIDE_PANEL_LENTH)
        self.anim2.setStartValue(GLOBAL_SIDE_PANEL_LENTH)
        
        self.anim1.setEndValue(46)
        self.anim2.setEndValue(46)
        
        self.anim1.start()
        self.anim2.start()
#endregion Toggle Menu
########################################################################

####################################################################
#region Change Page
# FUNCTION:Change Page
def change_page(self, idx, status):
    menus = [
        self.home_btn,
        self.anchor_btn,
        self.sub_btn,
        self.settings_btn,
        self.add_btn
    ]
    for i in range(len(menus)):
        if status == True and i == idx:
            self.Pages.setCurrentIndex(i)
            buttonActive(menus[i])
        else:
            buttonNotActive(menus[i])
    # SUBF:change button state
#endregion Change Page
########################################################################

###########################################################
#region Button Active
def buttonActive(btn):
    btn.setChecked(True)
    btn.setEnabled(False)
#endregion Button Active
###########################################################


###########################################################
#region Button Not Active
def buttonNotActive(btn):
    btn.setChecked(False)
    btn.setEnabled(True)
#endregion Button Not Active
###########################################################



#######################################################
#region Load Style Sheet
def Load_style_sheet():
    '''Returns style sheet after formating it using variables from json file
    '''
    p = Path(__file__).parent
    qss = (p / "Styles/styles.qss").resolve()
    style_vars = (p / "Styles/style_vars.json").resolve()

    if style_vars.is_file(): # load colors
        with open(style_vars, "r") as colors:
            style_vars = json.load(colors)
        if qss.is_file(): # load qss
            with open(qss, "r") as qss:
                qss = qss.read()
            qss = qss.format(**style_vars)
    if len(qss) > 0:
        return qss
    else:
        print("No style in style sheet")
#endregion Load Style Sheet
############################################################



#################### CLASSES ###########################

########################################################
#region Custom Sql TableWidget

class MySqlQTableWidget(QtWidgets.QTableWidget):
    '''This a Custom QTableWidget, which imports QTableWidget.
    It is Used to show queried data from database.
    
    @cols: `Number of columns in query`
    @labels: `list of labels for table`
    @parent: `parent of widget`
    '''
    def __init__(self,cols=None,labels=None,parent=None):
        super().__init__(parent)
        self.setColumnCount(cols)
        self.setHorizontalHeaderLabels(labels)
        
        self.setFrameShadow(QtWidgets.QFrame.Plain)
        self.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.setProperty("showDropIndicator", False)
        self.setDragDropOverwriteMode(False)
        self.setAlternatingRowColors(True)

        self.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.setHorizontalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)

        self.horizontalHeader().setHighlightSections(True)
        self.horizontalHeader().setStretchLastSection(True)
        self.horizontalHeader().setDefaultSectionSize(150)
        self.horizontalHeader().setMinimumSectionSize(80)
        self.verticalHeader().setHighlightSections(True)
        self.verticalHeader().setDefaultSectionSize(30)
        


    def show_data(self, query=None):
        '''This method show queried data in table
        @query: `queried data from database`
        '''
        while query.next():
            row = self.rowCount()
            self.setRowCount(row + 1)
            for i in range(self.columnCount()):
                item = QtWidgets.QTableWidgetItem(str(query.value(i)))
                item.setTextAlignment(Qt.AlignCenter)
                self.setItem(row, i, item)
        self.resizeColumnsToContents()
#endregion Custom Sql TableWidget
######################################################################