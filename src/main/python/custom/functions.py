from PyQt5.QtSql import QSqlDatabase
from PyQt5 import QtWidgets

######################################################################
#region Database Connect
def db_connect(driver, databasename):
    '''Connect to database and returns connection object
    @driver : SQL Driver
    @databasename: name of database
    '''
    db = QSqlDatabase.addDatabase(driver)
    db.setDatabaseName(databasename)
    if not db.open():
        QtWidgets.QMessageBox.about(caption="DB Connection", text="Error while connecting to Database")
        return 0
    return db
#endregion Database Connect
######################################################################