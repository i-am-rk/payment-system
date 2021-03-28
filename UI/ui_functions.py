from PyQt5.QtCore import(
    QPropertyAnimation
)
# from UI import mainwindow as mw

# class UI_Functions(mw.Ui_MainWindow):
#     """
#     This class holds all ui functions
#     Function:
#         `toggle menu`
#         `change_page`
#     """
#     # FUNCTION:Toggle Menu
#     def toggle_menu(self):
#         print("Toggle menu")
#         print(self.menu_toggle_btn)

#     # FUNCTION:Change Page
#     def change_page(self):
#         pass
#         # SUBF:change button state
############################################
### Variables
GLOBAL_SIDE_PANEL_LENTH = 160
############################################



#FUNCTION:Toggle Menu
def toggle_menu(self, status):
    if status:
        print("inside toggle")
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

# FUNCTION:Change Page
def change_page(self):
    print
    # SUBF:change button state