####################################################
#region COLORS

THEME_COLOR = "#00F506"
HOVER_COLOR = "#FFFFFF"
HOVER_BG_COLOR = "#1FB141"
#endregion COLORS
#######################################################

###########################################################
#region MENU BUTTONS VARS
menu_btn_padding = "45px"
menu_btn_border = "8px"

#endregion MENU BUTTONS VARS
############################################################


######################################################################
#region Menu Buttons Style

menu_btn = """
            QPushButton{{
            background-position: left center;
            background-repeat: no-repeat;
            background-color: none;
            text-align: left;
            padding-left: {padding};
            border:none;
            border-left: {b} solid none;
        }}
        """.format(padding = menu_btn_padding, b = menu_btn_border)

menu_btn_hover = """
                QPushButton:hover{{
                background-color: {color};
                border-left: {bl} solid {color};
                color: {text};
                }}
                """.format(color = HOVER_BG_COLOR, text = HOVER_COLOR, bl = menu_btn_border )


menu_btn_pressed = """
                QPushButton:hover{{
                background-color: {color};
                border-left: {bl} solid {color};
                color: {text};
                }}
                """.format(color = HOVER_BG_COLOR, text = HOVER_COLOR, bl = menu_btn_border )
#endregion Menu Buttons Style
##########################################################################################

########################################################################################
#region TOGGLE BUTTONS

toggle_btn = """
            QPushButton{{
            background-color:{bg};
            border:none;
            background-repeat:no-repeat;
            background-position:center;
            }}
            """.format(bg = THEME_COLOR)
#endregion TOGGLE BUTTONS
######################################################################################
