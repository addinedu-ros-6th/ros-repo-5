from PyQt5 import QtWidgets, uic
import sys
import os
import resource_rc

class UserWindow(QtWidgets.QMainWindow):
    def __init__(self, login_window):
        super().__init__()
        self.login_window = login_window
        
        uic.loadUi('RobotSystemHub/UserGui/user.ui', self)
        
        # 로그아웃 버튼 연결
        self.logout_button.clicked.connect(self.logout)

    def logout(self):
        self.hide()
        self.login_window.text_id.clear()
        self.login_window.text_password.clear()
        self.login_window.show()