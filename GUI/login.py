from PyQt5 import QtWidgets, uic
from PyQt5.QtCore import pyqtSignal
import sys
import resource_rc

class LoginWindow(QtWidgets.QMainWindow):
    login_successful = pyqtSignal()  

    def __init__(self):
        super().__init__()
        
        
        uic.loadUi('login.ui', self)

        
        self.login_button.clicked.connect(self.attempt_login)

    def attempt_login(self):
        
        self.login_successful.emit()
        self.close()

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    login_window = LoginWindow()
    login_window.show()
    sys.exit(app.exec_())