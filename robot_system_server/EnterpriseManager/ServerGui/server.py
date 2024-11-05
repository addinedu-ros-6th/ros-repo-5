from PyQt5 import QtWidgets, uic
import sys
import os
import resource_rc
from PyQt5.QtWidgets import QHeaderView
from PyQt5.QtCore import Qt, QThread, pyqtSignal
from PyQt5.QtGui import QPixmap
import socket
import sys
import os

import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Pose  # X, Y, TH 데이터를 담을 수 있는 메시지
from PyQt5.QtCore import QThread, pyqtSignal

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../..")))
import robot_system_server.EnterpriseManager.ServerGui.taskmanager as taskmanager

class RosSubscriberNode(Node):
    def __init__(self):
        super().__init__('pose_subscriber')
        self.subscription = self.create_subscription(Pose, '/trashbot/Pose', self.listener_callback, 10)
        self.pose_x = 0.0
        self.pose_y = 0.0
        self.pose_th = 0.0

    def listener_callback(self, msg):
        self.pose_x = msg.position.x
        self.pose_y = msg.position.y
        self.pose_th = msg.orientation.z
        self.get_logger().info(f'Received - X: {self.pose_x}, Y: {self.pose_y}, TH: {self.pose_th}')

class RosThread(QThread):
    pose_received = pyqtSignal(float, float, float)

    def __init__(self):
        super().__init__()
        rclpy.init()
        self.node = RosSubscriberNode()

    def run(self):
        while rclpy.ok():
            rclpy.spin_once(self.node)
            # 받은 데이터를 PyQt로 전달
            self.pose_received.emit(self.node.pose_x, self.node.pose_y, self.node.pose_th)

    def stop(self):
        rclpy.shutdown()
        self.node.destroy_node()

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
        PORT = 65413      # 포트번호

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
        self.login_window = login_window
        uic.loadUi('robot_system_server/EnterpriseManager/ServerGui/server.ui', self)

        # taskmanager 클래스 인스턴스 생성
        self.tm = taskmanager.taskmanager(self.login_window)

        self.checkbox_list = [self.checkbox_basket_1, self.checkbox_basket_2, self.checkbox_basket_3,
                              self.checkbox_basket_4, self.checkbox_basket_5, self.checkbox_basket_6]
        # ROS 스레드 시작
        self.ros_thread = RosThread()
        self.ros_thread.pose_received.connect(self.update_pose)
        self.ros_thread.start()
        
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
        

        for i in range(len(self.checkbox_list)):
            self.checkbox_list[i].clicked.connect(lambda checked, index=i: self.checkbox_basket_changed(checked, index))

    def update_pose(self, x, y, th):
        # ROS에서 받은 데이터를 UI로 업데이트
        print(f"Received Pose - X: {x}, Y: {y}, TH: {th}")

    def closeEvent(self, event):
        # 프로그램 종료 시 ROS 노드를 종료
        self.ros_thread.stop()
        super().closeEvent(event)
        
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
        if split_message[0] == "cb" : # client에서 받은 데이터로 checkbox 상태 변경
            index = int(split_message[1])
            self.userid = int(split_message[3]) #client user id
            if split_message[2] == "1": #Checkbox True
                self.checkbox_list[index-1].setChecked(True)
                self.tm.job_create(self.userid ,navigation_point_id = index) # 유저 모드 Job 생성

            elif split_message[2] == "0": #Checkbox False
                self.checkbox_list[index-1].setChecked(False)
                job_id, job_status = self.tm.Job_jobstatus_check(navigation_point_id = index) #Job ID, Job staus 불러오기

                if job_status == 'pending' or job_status == 'allocated':
                    self.tm.Job_update_notinprogress_to_cancel(job_id, navigation_point_id = index, user_id = self.userid) #유저 모드 Job 취소

            self.send_message(f"cb,{index},{split_message[2]},{self.userid}\n") #Client에서 수신된 데이터 모든 client에 전송

    def send_message(self, message):
        self.server_thread.send_message(message)

    def logout(self):
        self.hide()
        self.login_window.text_id.clear()
        self.login_window.text_password.clear()
        self.login_window.show()

# self,user_id, job_id, navigation_point_id, pos_x, pos_y, proximity_status):
    def checkbox_basket_changed(self, checked, index):
        server_id = 1
        print(f"basket_{index} clicked")
        if checked:
            if self.checkbox_list[index].isChecked() == True :
                print(f"basket_{index+1}_checked")
                self.send_message(f"cb,{index+1},1\r\n")
                self.tm.job_create(server_id, navigation_point_id = index+1) #관리자 모드 Job 생성
        elif checked==False:
            if self.checkbox_list[index].isChecked() == False :
                print(f"basket_{index+1}_unchecked")
                self.send_message(f"cb,{index+1},0\r\n")
                job_id, job_status = self.tm.Job_jobstatus_check(navigation_point_id = index+1) #Job ID, Job staus 불러오기

                if job_status == 'pending' or job_status == 'allocated':
                    self.tm.Job_update_notinprogress_to_cancel(job_id, navigation_point_id = index+1, user_id = server_id) #관리자보드  모드 Job 취소

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    login_window = QtWidgets.QMainWindow()
    main_window = MainWindow(login_window)
    main_window.show()
    sys.exit(app.exec_())