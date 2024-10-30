from PyQt5 import QtWidgets, uic
import sys
import socket
from PyQt5.QtCore import Qt, QThread, pyqtSignal
import mysql.connector

class ClientThread(QThread):
    message_received = pyqtSignal(str)  # 메시지 수신 신호

    def __init__(self, host, port):
        super().__init__()
        self.host = host
        self.port = 65420
        self.client_socket = None

    def run(self):
        try:
            # 서버에 연결
            self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.client_socket.connect((self.host, self.port))
            print("서버에 연결되었습니다.")

            while True:
                data = self.client_socket.recv(1024)  # 서버로부터 데이터 수신
                if not data:
                    print("서버와의 연결이 종료되었습니다.")
                    break
                message = data.decode()
                self.message_received.emit(message)  # 수신된 메시지를 메인 윈도우로 전송

        except Exception as e:
            print(f"오류 발생: {e}")

        finally:
            if self.client_socket:
                self.client_socket.close()

    def send_message(self, message):
        if self.client_socket:  # 서버가 연결되어 있는지 확인
            self.client_socket.sendall(message.encode())  # 서버에게 메시지 전송


class UserWindow(QtWidgets.QMainWindow):
    def __init__(self, login_window):
        super().__init__()
        self.login_window = login_window
        
        uic.loadUi('RobotSystemHub/UserGui/user.ui', self)
        self.employee_number = self.login_window.text_id.text() 
        
        self.checkbox_list = [self.checkbox_basket_1, self.checkbox_basket_2, self.checkbox_basket_3,
                              self.checkbox_basket_4, self.checkbox_basket_5, self.checkbox_basket_6]
        
        # 로그아웃 버튼 연결
        self.logout_button.clicked.connect(self.logout)

        # 클라이언트 스레드 초기화
        self.client_thread = ClientThread('127.0.0.1', 65432)  # 서버 주소와 포트
        self.client_thread.message_received.connect(self.on_message_received)
        self.client_thread.start()

        self.checkbox_basket_1.clicked.connect(self.checkbox_basket_1_changed)
        self.checkbox_basket_2.stateChanged.connect(self.checkbox_basket_2_changed)
        self.checkbox_basket_3.stateChanged.connect(self.checkbox_basket_3_changed)
        self.checkbox_basket_4.stateChanged.connect(self.checkbox_basket_4_changed)
        self.checkbox_basket_5.stateChanged.connect(self.checkbox_basket_5_changed)
        self.checkbox_basket_6.stateChanged.connect(self.checkbox_basket_6_changed)

        # db연동 
        self.db_config = {
            'host': "database-1.cpog6osggiv3.ap-northeast-2.rds.amazonaws.com",
            'user': "arduino_PJT",
            'password': "1234",
            'database': "ardumension"
        }
        self.db_connection = None
        self.connect_to_database()
        if self.db_connection:
            self.initialize_checkboxes()
    def connect_to_database(self):
        try:
            self.db_connection = mysql.connector.connect(**self.db_config)
            print("데이터베이스에 연결되었습니다.")
            return True
        except mysql.connector.Error as e:
            print(f"데이터베이스 연결 오류: {e}")
            self.db_connection = None
            return False
        
    def initialize_checkboxes(self):
        try:
            cursor = self.db_connection.cursor(dictionary=True)
            
            # 현재 사용자의 id 조회
            user_query = """
                SELECT id FROM RobotUser
                WHERE employee_number = %s
            """
            cursor.execute(user_query, (self.employee_number,))
            user_result = cursor.fetchone()
            
            if user_result:
                # 모든 체크박스를 먼저 disable
                for checkbox in self.checkbox_list:
                    checkbox.setEnabled(False)

                # 사용자의 할당된 basket 조회
                basket_query = """
                    SELECT np.name, np.id
                    FROM Userbasket ub
                    JOIN NavigationPoint np ON ub.navigation_point_id = np.id
                    WHERE ub.user_id = %s
                """
                cursor.execute(basket_query, (user_result['id'],))
                assigned_baskets = cursor.fetchall()
        
                # 할당된 basket만 enable
                for basket in assigned_baskets:
                    try:
                        basket_num = int(''.join(filter(str.isdigit, basket['name'])))
                        if 1 <= basket_num <= len(self.checkbox_list):
                            self.checkbox_list[basket_num-1].setEnabled(True)
                    except ValueError:
                        continue

            cursor.close()

        except mysql.connector.Error as e:
            error_msg = f"체크박스 초기화 오류: {e}"
            print(error_msg)
            QtWidgets.QMessageBox.warning(self, "데이터베이스 오류", error_msg)

    def send_message(self, message):
        # 메세지 전송
        self.client_thread.send_message(message)  # 클라이언트 스레드에 메시지 전송

    def on_message_received(self, message):
        # 수신된 메시지를 처리하는 함수
                # 수신된 메시지를 처리하는 함수
        messages = message.splitlines()  # 각 줄로 분리
        
        for msg in messages:
            split_message = msg.split(",")  # 개별 메시지를 ','로 나눔
            print(split_message)
            
            if split_message[0] == "cb":
                n = int(split_message[1])
                if split_message[2] == "1":
                    self.checkbox_list[n-1].setChecked(True)
                elif split_message[2] == "0":
                    self.checkbox_list[n-1].setChecked(False)

    def logout(self):
        self.hide()
        self.login_window.text_id.clear()
        self.login_window.text_password.clear()
        self.login_window.show()
        self.db_connection.close()
        
    def checkbox_basket_1_changed(self):
        print("basket_1 clicked")
        if self.checkbox_basket_1.isChecked() == True :
            print("basket_1_checked")
            self.send_message("cb,1,1")
        else:
            print("basket_1_unchecked")
            self.send_message("cb,1,0")

    def checkbox_basket_2_changed(self):
        print("basket_2 clicked")
        if self.checkbox_basket_2.isChecked() == True :
            print("basket_2_checked")
            self.send_message("cb,2,1")
        else:
            print("basket_2_unchecked")
            self.send_message("cb,2,0")

    def checkbox_basket_3_changed(self):
        print("basket_3 clicked")
        if self.checkbox_basket_3.isChecked() == True :
            print("basket_3_checked")
            self.send_message("cb,3,1")
        else:
            print("basket_3_unchecked")
            self.send_message("cb,3,0")

    def checkbox_basket_4_changed(self):
        print("basket_4 clicked")
        if self.checkbox_basket_4.isChecked() == True :
            print("basket_4_checked")
            self.send_message("cb,4,1")
        else:
            print("basket_4_unchecked")
            self.send_message("cb,4,0")

    def checkbox_basket_5_changed(self):
        print("basket_5 clicked")
        if self.checkbox_basket_5.isChecked() == True :
            print("basket_5_checked")
            self.send_message("cb,5,1")
        else:
            print("basket_5_unchecked")
            self.send_message("cb,5,0")

    def checkbox_basket_6_changed(self):
        print("basket_6 clicked")
        if self.checkbox_basket_6.isChecked() == True :
            print("basket_6_checked")
            self.send_message("cb,6,1")
        else:
            print("basket_6_unchecked")
            self.send_message("cb,6,0")



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    login_window = QtWidgets.QMainWindow()  # 로그인 윈도우 초기화 (예시로 빈 윈도우 생성)
    user_window = UserWindow(login_window)
    user_window.show()
    sys.exit(app.exec_())
