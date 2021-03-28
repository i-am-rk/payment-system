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

def buttonActive(btn):
    style = btn.styleSheet()
    style = style + ("QPushButton{background-color:#00F506;border-left:8px solid #00F506; color:#000000;}")
    btn.setStyleSheet(style)
    btn.setChecked(True)
    btn.setEnabled(False)


def buttonNotActive(btn):
    style = btn.styleSheet()
    style = style.replace("QPushButton{background-color:#00F506;border-left:8px solid #00F506; color:#000000;}","")
    btn.setStyleSheet(style)
    btn.setChecked(False)
    btn.setEnabled(True)

from UI import resource_rc

