from PyQt5 import QtWidgets, uic
import sys
import socket
from PyQt5.QtCore import Qt, QThread, pyqtSignal
import mysql.connector

server_ip = "192.168.0.37" #Server IP 기입
server_port = 65423

class ClientThread(QThread):
    message_received = pyqtSignal(str)

    def __init__(self, host, port):
        super().__init__()

        self.client_socket = None

    def run(self):
        try:
            # 서버에 연결
            self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.client_socket.connect((server_ip, server_port))
            print("서버에 연결되었습니다.")

            while True:
                data = self.client_socket.recv(1024)
                if not data:
                    print("서버와의 연결이 종료되었습니다.")
                    break
                message = data.decode()
                self.message_received.emit(message)

        except Exception as e:
            print(f"오류 발생: {e}")

        finally:
            if self.client_socket:
                self.client_socket.close()

    def send_message(self, message):
        if self.client_socket:  
            self.client_socket.sendall(message.encode())  


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

        self.client_thread = ClientThread(server_ip, server_port)

        self.client_thread.message_received.connect(self.on_message_received)
        self.client_thread.start()

        self.checkbox_basket_1.clicked.connect(self.checkbox_basket_1_changed)
        self.checkbox_basket_2.clicked.connect(self.checkbox_basket_2_changed)
        self.checkbox_basket_3.clicked.connect(self.checkbox_basket_3_changed)
        self.checkbox_basket_4.clicked.connect(self.checkbox_basket_4_changed)
        self.checkbox_basket_5.clicked.connect(self.checkbox_basket_5_changed)
        self.checkbox_basket_6.clicked.connect(self.checkbox_basket_6_changed)

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
        self.client_thread.send_message(message)

    def on_message_received(self, message):
        messages = message.splitlines()
        
        for msg in messages:
            split_message = msg.split(",")
            print(split_message)
            
            if split_message[0] == "cb": #message[0] : cb(Checkbox) message[1] : cb 번호, message[2] : True/False
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
