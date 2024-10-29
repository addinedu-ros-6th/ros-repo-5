from PyQt5 import QtWidgets, uic
import sys
import os
import resource_rc
from PyQt5.QtWidgets import QHeaderView
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, login_window):
        super().__init__()
        self.login_window = login_window
        uic.loadUi('robot_system_server/EnterpriseManager/ServerGui/server.ui', self)
        
        
        # stack widget 버튼 이동
        self.main_button.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(0))
        self.call_button.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(1))
        self.log_button.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(2))
        
        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        
        # 로그아웃 버튼
        self.logout_button.clicked.connect(self.logout)
        
        # 가상 맵 설정
        pixmap = QPixmap('virtual_map.png')
        self.virtual_map.setPixmap(pixmap)
        self.virtual_map.setScaledContents(True)

    def logout(self):
        self.hide()
        self.login_window.text_id.clear()
        self.login_window.text_password.clear()
        self.login_window.show()