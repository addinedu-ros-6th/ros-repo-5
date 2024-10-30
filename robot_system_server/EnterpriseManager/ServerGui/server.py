from PyQt5 import QtWidgets, uic
import sys
import os
import resource_rc
from PyQt5.QtWidgets import QHeaderView
from PyQt5.QtCore import Qt, QThread, pyqtSignal
from PyQt5.QtGui import QPixmap
import socket

# 서버 소켓을 관리하는 스레드 클래스
class ServerThread(QThread):
    message_received = pyqtSignal(str)  # 메시지 수신 신호
    checkboxsync = pyqtSignal(str)  # 메시지 수신 신호

    def __init__(self):
        super().__init__()
        self.client_socket = None  # 클라이언트 소켓 저장

    def run(self):
        HOST = '127.0.0.1'  # 로컬호스트
        PORT = 65420        # 포트번호

        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.bind((HOST, PORT))
        server_socket.listen()

        print("서버가 시작되었습니다. 클라이언트를 기다리는 중...")

        while True:
            try:
                self.client_socket, addr = server_socket.accept()  # 클라이언트 연결 수락
                print(f"클라이언트가 연결되었습니다: {addr}")
                self.checkboxsync.emit("Client Connected")

                while True:
                    data = self.client_socket.recv(1024)  # 클라이언트로부터 데이터 수신
                    if not data:
                        print("클라이언트가 연결을 종료했습니다.")
                        break
                    message = data.decode()
                    print(f"클라이언트로부터 받은 메시지: {message}")

                    # 메시지를 메인 윈도우로 전송
                    self.message_received.emit(message)

            except Exception as e:
                print(f"오류 발생: {e}")

            finally:
                if self.client_socket:
                    self.client_socket.close()

    def send_message(self, message):
        if self.client_socket:  # 클라이언트가 연결되어 있는지 확인
            self.client_socket.sendall(message.encode())  # 클라이언트에게 메시지 전송

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, login_window):
        super().__init__()
        self.login_window = login_window
        uic.loadUi('robot_system_server/EnterpriseManager/ServerGui/server.ui', self)

        self.checkbox_list = [self.checkbox_basket_1, self.checkbox_basket_2, self.checkbox_basket_3,
                              self.checkbox_basket_4, self.checkbox_basket_5, self.checkbox_basket_6]

        # 서버 스레드 생성 및 시작
        self.server_thread = ServerThread()
        self.server_thread.message_received.connect(self.on_message_received)
        self.server_thread.start()
        self.server_thread.checkboxsync.connect(self.clientcheckboxsync)
        # stack widget 버튼 이동
        self.main_button.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(0))
        self.call_button.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(1))
        self.log_button.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(2))

        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        # 로그아웃 버튼
        self.logout_button.clicked.connect(self.logout)

        # 가상 맵 설정
        pixmap = QPixmap('robot_system_server/EnterpriseManager/ServerGui/virtual_map.png')
        self.virtual_map.setPixmap(pixmap)
        self.virtual_map.setScaledContents(True)
        self.checkbox_basket_1.clicked.connect(self.checkbox_basket_1_changed)
        self.checkbox_basket_2.clicked.connect(self.checkbox_basket_2_changed)
        self.checkbox_basket_3.clicked.connect(self.checkbox_basket_3_changed)
        self.checkbox_basket_4.clicked.connect(self.checkbox_basket_4_changed)
        self.checkbox_basket_5.clicked.connect(self.checkbox_basket_5_changed)
        self.checkbox_basket_6.clicked.connect(self.checkbox_basket_6_changed)

    def clientcheckboxsync(self):
        for i in range(len(self.checkbox_list)):
            checkbox_status = self.checkbox_list[i].isChecked()
            if checkbox_status == True:
                checkbox_status = "1"
            else:
                checkbox_status = "0"
            string_i = str(i+1)
            # 각 체크박스 상태를 개별 메시지로 보냄
            self.send_message(f"cb,{string_i},{checkbox_status}\n")  # 여전히 루프 내부에 위치


    def on_message_received(self, message):
        # 수신된 메시지를 처리하는 함수
        split_message = message.split(",")
        print(split_message)
        if split_message[0] == "cb" :
            n = int(split_message[1])
            if split_message[2] == "1":
                self.checkbox_list[n-1].setChecked(True)
            elif split_message[2] == "0":
                self.checkbox_list[n-1].setChecked(False)

        

    def send_message(self, message):
        # 메시지 전송
        self.server_thread.send_message(message)  # 서버 스레드에 메시지 전송

    def logout(self):
        self.hide()
        self.login_window.text_id.clear()
        self.login_window.text_password.clear()
        self.login_window.show()

    def checkbox_basket_1_changed(self):
        print("basket_1 clicked")
        if self.checkbox_basket_1.isChecked() == True :
            print("basket_1_checked")
            self.send_message("cb,1,1\r\n")
        else:
            print("basket_1_unchecked")
            self.send_message("cb,1,0\r\n")

    def checkbox_basket_2_changed(self):
        print("basket_2 clicked")
        if self.checkbox_basket_2.isChecked() == True :
            print("basket_2_checked")
            self.send_message("cb,2,1\r\n")
        else:
            print("basket_2_unchecked")
            self.send_message("cb,2,0\r\n")

    def checkbox_basket_3_changed(self):
        print("basket_3 clicked")
        if self.checkbox_basket_3.isChecked() == True :
            print("basket_3_checked")
            self.send_message("cb,3,1\r\n")
        else:
            print("basket_3_unchecked")
            self.send_message("cb,3,0\r\n")

    def checkbox_basket_4_changed(self):
        print("basket_4 clicked")
        if self.checkbox_basket_4.isChecked() == True :
            print("basket_4_checked")
            self.send_message("cb,4,1\r\n")
        else:
            print("basket_4_unchecked")
            self.send_message("cb,4,0\r\n")

    def checkbox_basket_5_changed(self):
        print("basket_5 clicked")
        if self.checkbox_basket_5.isChecked() == True :
            print("basket_5_checked")
            self.send_message("cb,5,1\r\n")
        else:
            print("basket_5_unchecked")
            self.send_message("cb,5,0\r\n")

    def checkbox_basket_6_changed(self):
        print("basket_6 clicked")
        if self.checkbox_basket_6.isChecked() == True :
            print("basket_6_checked")
            self.send_message("cb,6,1\r\n")
        else:
            print("basket_6_unchecked")
            self.send_message("cb,6,0\r\n")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    login_window = QtWidgets.QMainWindow()  # 로그인 윈도우 초기화 (예시로 빈 윈도우 생성)
    main_window = MainWindow(login_window)
    main_window.show()
    sys.exit(app.exec_())
