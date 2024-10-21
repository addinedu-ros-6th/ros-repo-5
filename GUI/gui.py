from PyQt5 import QtWidgets, uic
import sys
import resource_rc
from PyQt5.QtWidgets import QHeaderView
from login import LoginWindow 
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        
        
        uic.loadUi('gui.ui', self)

        # stack widget 버튼 이동
        self.main_button.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(0))
        self.call_button.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(1))
        self.log_button.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(2))
        
        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        #로그아웃버튼
        self.logout_button.clicked.connect(self.logout)
        pixmap = QPixmap('virtual_map.png')
        self.virtual_map.setPixmap(pixmap)
        self.virtual_map.setScaledContents(True)

    def logout(self):
        self.hide()
        if self.login_window is None:
            self.login_window = LoginWindow()
        self.login_window.login_successful.connect(self.on_login_success)
        self.login_window.show()

    def on_login_success(self):
        self.show()
        self.login_window.hide()

def main():
    app = QtWidgets.QApplication(sys.argv)
    
    main_window = MainWindow()
    login_window = LoginWindow()
    main_window.login_window = login_window

    login_window.login_successful.connect(main_window.on_login_success)

    login_window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()