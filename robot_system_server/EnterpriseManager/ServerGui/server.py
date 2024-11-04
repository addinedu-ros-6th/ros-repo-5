from PyQt5 import QtWidgets, uic
import sys
import os
import resource_rc
from PyQt5.QtWidgets import QHeaderView, QTableWidgetItem,QDialog, QVBoxLayout, QLabel,QMessageBox
from PyQt5.QtCore import Qt, QThread, pyqtSignal, QTimer ,QDate
from PyQt5.QtGui import QPixmap,QImage
import socket
import mysql.connector
import cv2
import os
\

class ImageWindow(QDialog):
    def __init__(self, image, parent=None):
        super(ImageWindow, self).__init__(parent)
        self.setWindowTitle("Image Viewer")

        # 이미지 QLabel 생성
        label = QLabel(self)
        height, width, channel = image.shape
        bytes_per_line = 3 * width
        q_image = QPixmap(QPixmap.fromImage(QImage(image.data, width, height, bytes_per_line, QImage.Format_RGB888).rgbSwapped()))

        # QLabel에 이미지 설정
        label.setPixmap(q_image)

        # 레이아웃 설정
        layout = QVBoxLayout()
        layout.addWidget(label)
        self.setLayout(layout)
        self.resize(width, height)

    def show_image(self):
        self.exec_()


class ClientThread(QThread):
    message_received = pyqtSignal(str) 
    checkboxsync = pyqtSignal(str)
    disconnected = pyqtSignal()
    
    def __init__(self, client_socket):
        super().__init__()
        self.client_socket = client_socket
        self.is_connected = True  # 연결 상태 변수 추가
        
    def run(self):
        try:
            self.checkboxsync.emit("sync")
            while True:
                data = self.client_socket.recv(1024)
                if not data:
                    print("클라이언트가 연결을 종료했습니다.")
                    self.is_connected = False  # 연결 해제 시 상태 업데이트
                    self.disconnected.emit()  # 연결 해제 신호 발송
                    break
                message = data.decode()
                print(f"클라이언트로부터 받은 메시지: {message}")

                self.message_received.emit(message)

        except Exception as e:
            print(f"오류 발생: {e}")
            self.disconnected.emit()  # 오류 발생 시에도 연결 해제 신호 발송
        finally:
            self.client_socket.close()
        
# 서버 소켓을 관리하는 스레드 클래스
class ServerThread(QThread):
    message_received = pyqtSignal(str)
    checkboxsync = pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self.client_threads = []  # 클라이언트 스레드 목록

    def run(self):
        HOST = '0.0.0.0'  # 로컬호스트 (모든 ip 허용 시 0,0,0,0)
        PORT = 65423      # 포트번호

        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.bind((HOST, PORT))
        server_socket.listen(5)

        print("서버가 시작되었습니다. 클라이언트를 기다리는 중...")

        while True:
            try:
                client_socket, addr = server_socket.accept()
                print(f"클라이언트가 연결되었습니다: {addr}")

                client_thread = ClientThread(client_socket)
                client_thread.message_received.connect(self.on_message_received)
                client_thread.checkboxsync.connect(self.on_checkboxsync)
                client_thread.disconnected.connect(self.on_client_disconnected)
                client_thread.start()

                self.client_threads.append(client_thread)  # 클라이언트 스레드를 목록에 추가

            except Exception as e:
                print(f"오류 발생: {e}")

    def on_message_received(self, message):
        self.message_received.emit(message)

    def on_checkboxsync(self):
        self.checkboxsync.emit("sync")

    def on_client_disconnected(self):
        # 연결 해제된 클라이언트 스레드를 목록에서 제거
        for thread in self.client_threads:
            if not thread.is_connected:
                self.client_threads.remove(thread)
                print("클라이언트 스레드가 목록에서 제거되었습니다.")
                break
            
    def send_message(self, message):
        for thread in self.client_threads:
            if thread.client_socket:  # 클라이언트 소켓이 유효한지 확인
                try:
                    thread.client_socket.sendall(message.encode())
                    print(message)
                except Exception as e:
                    print(f"메시지 전송 오류: {e}")
                    self.client_threads.remove(thread)  # 오류가 발생하면 스레드 목록에서 제거

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, login_window):
        super().__init__()
        self.setWindowTitle("Server")
        self.login_window = login_window
        uic.loadUi('robot_system_server/EnterpriseManager/ServerGui/server.ui', self)
         
        self.checkbox_list = [self.checkbox_basket_1, self.checkbox_basket_2, self.checkbox_basket_3,
                              self.checkbox_basket_4, self.checkbox_basket_5, self.checkbox_basket_6]
        
        """로그테이블의 combobox셋업"""
        self.options = {
            "all" : ["all"],
            "job_status": ["all","pending","allocated","completed","cancled","inprogress","aruco_error"],
            "robot_status": ["all","idle","driving","waiting","charging"],
            "employee_number": ["all","1234","test"]
        }
        
        self.search_type.addItems(self.options.keys())
        self.search_type.currentTextChanged.connect(self.update_item)
        self.update_item(self.search_type.currentText())
        self.search_button.clicked.connect(self.load_log_data)
        current_date = QDate.currentDate()
        self.end_date.setDate(current_date)


        # 서버 스레드 생성 및 시작
        self.server_thread = ServerThread()
        self.server_thread.message_received.connect(self.on_message_received)
        self.server_thread.start()
        self.server_thread.checkboxsync.connect(self.clientcheckboxsync)

        self.log_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        # stack widget 버튼 이동
        self.main_button.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(0))
        self.call_button.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(1))
        self.log_button.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(2))

        self.map_job_widget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

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
    
    def update_item(self, text):
        """첫 번째 콤보박스 선택에 따라 두 번째 콤보박스 항목 업데이트"""
        self.search_item.clear()
        self.search_item.addItems(self.options[text])
    
    def load_log_data(self):
        try:
            connection = mysql.connector.connect(
                host='database-1.cpog6osggiv3.ap-northeast-2.rds.amazonaws.com',
                user='arduino_PJT ',
                password='1234',
                database='ardumension'
            )
            cursor = connection.cursor()
            start_date = self.start_date.date().toString("yyyy-MM-dd")
            end_date = self.end_date.date().toString("yyyy-MM-dd")



            # 기본 쿼리
            base_query = base_query = """
                SELECT * FROM (
                    SELECT 
                        j.create_at AS time,
                        j.job_id,
                        j.job_status,
                        r.name AS robot_name,
                        r.current_status as robot_status,
                        e.image_path,
                        u.employee_number AS user_name,
                        n.name AS navigation_point,
                        e.aruco_id
                    FROM JobLog AS j
                    LEFT JOIN Robot AS r ON j.robot_id = r.id
                    LEFT JOIN JobErrorLog AS e ON j.job_id = e.job_id
                    LEFT JOIN RobotUser AS u ON j.user_id = u.id
                    LEFT JOIN NavigationPoint AS n ON j.navigation_point_id = n.id
                    WHERE DATE(j.create_at) BETWEEN %s AND %s

                    UNION ALL

                    SELECT 
                        rs.create_at AS time,
                        rs.job_id,
                        j.job_status,
                        r.name AS robot_name,
                        rs.robot_status,
                        e.image_path,
                        u.employee_number AS user_name,
                        n.name AS navigation_point,
                        e.aruco_id
                    FROM RobotStatusLog AS rs
                    LEFT JOIN JobLog AS j ON rs.job_id = j.job_id
                    LEFT JOIN Robot AS r ON rs.robot_id = r.id
                    LEFT JOIN JobErrorLog AS e ON rs.job_id = e.job_id
                    LEFT JOIN RobotUser AS u ON j.user_id = u.id
                    LEFT JOIN NavigationPoint AS n ON j.navigation_point_id = n.id
                    WHERE DATE(rs.create_at) BETWEEN %s AND %s
                ) AS combined_logs
            """

            search_type = self.search_type.currentText()
            search_item = self.search_item.currentText()
            params = [start_date, end_date, start_date, end_date]
            #검색 조건
            
            if search_type != "all" and search_item != "all":
                if search_type == "job_status":
                    base_query += " WHERE job_status = %s"
                elif search_type == "robot_status":
                    base_query += " WHERE robot_status = %s"
                elif search_type == "employee_number":
                    base_query += " WHERE user_name = %s"
                params.append(search_item)

            base_query += " ORDER BY time ASC"
            print("Executing query:", base_query) 
            print("Parameters:", params)  
            
            cursor.execute(base_query, params)
            logs = cursor.fetchall()
            
            # 테이블 데이터 설정
            self.log_table.setRowCount(len(logs))
            for row, log in enumerate(logs):
                for col, value in enumerate(log):
                    text = '' if value is None else str(value)
                    item = QTableWidgetItem(text)
                    item.setTextAlignment(Qt.AlignCenter)
                    self.log_table.setItem(row, col, item)
            
            cursor.close()
            connection.close()
            
        except mysql.connector.Error as err:
            print(f"데이터베이스 오류: {err}")
            QMessageBox.warning(self, "오류", f"데이터베이스 오류: {err}")
   
    def table1_dclicked(self, row, col):
        image_path = self.log_table.item(row, 5).text()
        if image_path:
            self.open_new_window(image_path)
        print(image_path)

    def open_new_window(self, image_path):
        try:
            image = cv2.imread(image_path)
            image_window = ImageWindow(image)
            image_window.show_image()
        except AttributeError:
            QMessageBox.warning(self, "오류", "사진이 존재하지 않습니다.")
        

    def clientcheckboxsync(self):
        for i in range(len(self.checkbox_list)):
            checkbox_status = self.checkbox_list[i].isChecked()
            if checkbox_status == True:
                checkbox_status = "1"
            else:
                checkbox_status = "0"
            string_i = str(i+1)
            self.send_message(f"cb,{string_i},{checkbox_status}\n") #새로운 Client 접속 시 checkbox 상태 전송


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
            self.send_message(f"cb,{n},{split_message[2]}\n") #Client에서 수신된 데이터 모든 client에 전송

    def send_message(self, message):
        self.server_thread.send_message(message)

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
    login_window = QtWidgets.QMainWindow()
    main_window = MainWindow(login_window)
    main_window.show()
    sys.exit(app.exec_())
