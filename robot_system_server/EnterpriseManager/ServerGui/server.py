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
from PyQt5.QtWidgets import QHeaderView, QTableWidgetItem,QDialog, QVBoxLayout, QLabel,QMessageBox
from PyQt5.QtCore import Qt, QThread, pyqtSignal, QTimer ,QDate
from PyQt5.QtGui import QPixmap,QImage
import rclpy as rp
from rclpy.node import Node
from geometry_msgs.msg import Pose  # X, Y, TH 데이터를 담을 수 있는 메시지
from PyQt5.QtCore import QThread, pyqtSignal
import mysql.connector
import cv2
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../..")))
import robot_system_server.EnterpriseManager.ServerGui.taskmanager as taskmanager
from taskmanager_msgs.srv import JobCompleteReq, JobAllocated
from taskmanager_msgs.msg import RobotStatus


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


class RosSubscriberNode(Node):
    def __init__(self):
        super().__init__('pose_subscriber')
        self.subscription = self.create_subscription(RobotStatus, 'RobotStatus', self.robot0_status, 10)
        self.server = self.create_service(JobCompleteReq, 'JobCompleteReq', self.jobcompletereq)
        self.client = self.create_client(JobAllocated, 'JobAllocatedRes')

        self.req_complete_job_id = None

    def robot0_status(self, msg): # receive data
        self.status = msg.robot_status
        self.pose_x = msg.x
        self.pose_y = msg.y
        self.battery = msg.battery_status

        #robot0 status print
        # self.get_logger().info(f'robot_status : {self.status}, Received - X: {self.pose_x}, Y: {self.pose_y}, battery : {self.battery}')

    def jobcompletereq(self, request, response):
        self.req_complete_job_id = request.job_id
        self.job_complete_status = request.job_complete # 0 : basket 없음, 1 : Job 완료
        self.detected_sensor = request.detected_sensor
        print(f"recv req_complete_job_id : {self.req_complete_job_id}, job_complete_status : {self.job_complete_status} detected sensor : {self.detected_sensor}")
        
        response.receive_complete = 1
        return response

    def send_job_inprogress_and_cancel(self, robot_num, x, y, z, w, job_id, nav_id):
        request = JobAllocated.Request()
        request.robot_num = robot_num
        request.x = x
        request.y = y
        request.z = z
        request.w = w
        request.job_id = job_id
        request.nav_id = nav_id
        
        # 비동기 호출
        future = self.client.call_async(request)
        future.add_done_callback(self.response_check)

        self.get_logger().info(f'Sent JobAllocated request for robot {robot_num} to ({x}, {y}, {z}, {w}) with job ID {job_id}, nav id : {nav_id}')

    def response_check(self, future):
        response = future.result()
        self.get_logger().info(f"Response received: {response}")

class RosThread(QThread):
    robot0_status_received = pyqtSignal(str, float, float, int)
    jobcompletereq_received = pyqtSignal(int, int, int)
    
    def __init__(self):
        super().__init__()
        rp.init()
        self.node = RosSubscriberNode()

    def run(self):
        while rp.ok():
            rp.spin_once(self.node)
            if self.node.req_complete_job_id is not None:
                self.jobcompletereq_received.emit(self.node.req_complete_job_id, self.node.job_complete_status, self.node.detected_sensor)
                self.node.req_complete_job_id = None

            # 받은 데이터를 PyQt로 전달
            self.robot0_status_received.emit(self.node.status, self.node.pose_x, self.node.pose_y, self.node.battery)

    def stop(self):
        rp.shutdown()
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
                    print(f"send to client msg : {message}")
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
        self.robot_status_list = [{"status" : "idle", "current_x" : 0, "current_y" : 0, "battery" : 50},  #minibot1
                                  {"status" : "idle", "current_x" : 0, "current_y" : 0, "battery" : 50}]  #minibot2
        self.checkbox_list = [self.checkbox_basket_1, self.checkbox_basket_2, self.checkbox_basket_3,
                              self.checkbox_basket_4, self.checkbox_basket_5, self.checkbox_basket_6]
        
        # ROS 스레드 시작
        self.ros_thread = RosThread()
        self.ros_thread.robot0_status_received.connect(self.robot0_status)
        self.ros_thread.jobcompletereq_received.connect(self.job_complete)
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

        self.map_job_widget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        # 로그아웃 버튼
        # self.logout_button.clicked.connect(self.logout)
        self.logout_button.clicked.connect(self.test_status)

        # 가상 맵 설정
        pixmap = QPixmap('robot_system_server/EnterpriseManager/ServerGui/virtual_map.png')

        self.virtual_map.setPixmap(pixmap)
        self.virtual_map.setScaledContents(True)

        #map 데이터 불러오기
        self.map_pose_list = self.tm.map_data()
        
        for i in range(len(self.checkbox_list)):
            self.checkbox_list[i].clicked.connect(lambda checked, index=i: self.checkbox_basket_changed(checked, index))

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
        self.log_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.map_job_widget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

    def update_item(self, text):
        """첫 번째 콤보박스 선택에 따라 두 번째 콤보박스 항목 업데이트"""
        self.search_item.clear()
        self.search_item.addItems(self.options[text])
    
    def load_log_data(self):
        try:
            connection = mysql.connector.connect(
                host="localhost",
                user="root",
                password="123123",
                database="trashbot"
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

    def robot0_status(self, status, x, y, battery):
        # ROS에서 받은 데이터를 UI로 업데이트
        self.robot_status_list[0] = {"status" : status, "current_x" : x, "current_y" : y, "battery" : 50}
        # print(self.robot_status_list) #robot status

    def test_status(self):
        self.robot_status_list = [{"status" : "idle", "current_x" : 0, "current_y" : 0, "battery" : 50},  #minibot1
                                  {"status" : "driving", "current_x" : 0, "current_y" : 0, "battery" : 50}]  #minibot2
        for i in range(len(self.robot_status_list)):
            if ((self.robot_status_list[i]['status'] == 'idle' or self.robot_status_list[i]['status'] == 'charging')  and self.robot_status_list[i]['battery'] > 40):
                robot_id = i

                #Job 유무 확인
                nav_id = self.tm.check_job_allocated(robot_id)#job 유무 확인 및 dump job 확인
                if nav_id != None:
                    job_id, nav_id = self.tm.job_inprogress(robot_id,nav_id)
                    
                    x = float(self.map_pose_list[nav_id-1][2])
                    y = float(self.map_pose_list[nav_id-1][3])
                    z = float(self.map_pose_list[nav_id-1][4])
                    w = float(self.map_pose_list[nav_id-1][5])

                    print(f"inprogress request,{robot_id}, {x}, {y}, {z}, {w}, {job_id}")
                    self.send_request_job_inprogress(robot_id, x, y, z, w, job_id)
            elif self.robot_status_list[i]['status'] == 'driving':
                if self.robot_status_list[i]['battery'] > 40:
                    pass
                else:
                    self.tm.job_refresh()
                    self.tm.job_allocate(self.robot_status_list, self.map_pose_list)
                    print("Rescheduling complete!!")
                    
    def job_complete(self, job_id, complete_status, detected_sensor):
        if complete_status == 0: #basket 없으면 error
            job_status = "error"
        elif complete_status == 1: # basket 있으면 complete
            job_status = "complete"

        nav_id, user_id, robot_id = self.tm.update_job_complete_and_error(job_id, job_status)
        print(f"Job {job_status}, Job_ID : {job_id}, robot_id : {robot_id}, nav_id : {nav_id}, user_id : {user_id}")

        print(f"test : {nav_id}")
        # self.checkbox_list[nav_id-1].setChecked(False)
        bt_status = "0" #False

        self.send_message(f"cb,{nav_id},{bt_status},{user_id}\n") #Client에서 수신된 데이터 모든 client에 전송

        if detected_sensor == 1:
            if robot_id == 0:
                nav_id = 8 # 0번 로봇 쓰레기 장소 id
            elif robot_id == 1:
                nav_id = 9 # 1번 로봇 쓰레기 장소 id

            job_id = self.tm.job_create(1, robot_id, nav_id) #관리자 모드 Job 생성
            job_status = "allocated"
            self.tm.job_allocate_dump(1, robot_id, nav_id, job_id, job_status)

    def send_request_job_inprogress(self, robot_id, x, y, z, w, job_id):
        # ROS 노드의 send_request 호출
        print(f"send_request_job_inprogress,{robot_id}, {x}, {y}, {z}, {w}, {job_id}")
        self.ros_thread.node.send_job_inprogress_and_cancel(robot_id, x, y, z, w, job_id)

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
        print(f"received client msg : {split_message}")
        if split_message[0] == "cb" : # client에서 받은 데이터로 checkbox 상태 변경
            index = int(split_message[1])
            self.userid = int(split_message[3]) #client user id
            if split_message[2] == "1": #Checkbox True
                self.checkbox_list[index-1].setChecked(True)
                robot_id = None
                job_id = self.tm.job_create(self.userid, robot_id, navigation_point_id = index) # 유저 모드 Job 생성
                if job_id != None:
                    self.tm.job_allocate(self.robot_status_list, self.map_pose_list) # Job 할당 및 Job table 업데이트, JobLog 추가
                else:
                    print("Job Create Fail")

            elif split_message[2] == "0": #Checkbox False
                self.checkbox_list[index-1].setChecked(False)
                job_id, job_status, robot_id = self.tm.Job_jobstatus_check(navigation_point_id = index) #Job ID, Job staus 불러오기

                if job_status == 'inprogress':
                    print(f"job status is {job_status}, user = client, cancel msg : {robot_id}, 0.0, 0.0, 0.0, 0.0, {job_id}")
                    self.ros_thread.node.send_job_inprogress_and_cancel(robot_id, 0.0, 0.0, 0.0, 0.0, job_id)
                    self.tm.Job_cancel(job_id, navigation_point_id = index, user_id = self.userid) #유저 모드 Job 취소
                    
                if job_status == 'pending' or job_status == 'allocated':
                    print(f"job status is {job_status}, user = client, Job Cancel")
                    self.tm.Job_cancel(job_id, navigation_point_id = index, user_id = self.userid) #유저 모드 Job 취소

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
        print(f"basket_{index+1} clicked")
        if checked:
            if self.checkbox_list[index].isChecked() == True :
                robot_id = None
                print(f"basket_{index+1}_checked")
                self.send_message(f"cb,{index+1},1\r\n")
                job_id = self.tm.job_create(server_id, robot_id, navigation_point_id = index+1) #관리자 모드 Job 생성
                if job_id != None:
                    self.tm.job_allocate(self.robot_status_list, self.map_pose_list) # Job 할당 및 Job table 업데이트, JobLog 추가
                else:
                    print("Job Create Fail")
        elif checked==False:
            if self.checkbox_list[index].isChecked() == False :
                print(f"basket_{index+1}_unchecked")
                self.send_message(f"cb,{index+1},0\r\n")
                job_id, job_status, robot_id = self.tm.Job_jobstatus_check(navigation_point_id = index+1) #Job ID, Job staus 불러오
                
                if job_status == 'inprogress':
                    print(f"cancel job id {job_id}, user = server, cancel msg : {robot_id}, 0.0, 0.0, 0.0, 0.0, {job_id}")
                    self.ros_thread.node.send_job_inprogress_and_cancel(robot_id, 0.0, 0.0, 0.0, 0.0, job_id)
                    self.tm.Job_cancel(job_id, navigation_point_id = index+1, user_id = server_id) #관리자보드  모드 Job 취소

                if job_status == 'pending' or job_status == 'allocated':
                    print(f"cancel job id : {job_id}, user = server, Job Cancel")
                    self.tm.Job_cancel(job_id, navigation_point_id = index+1, user_id = server_id) #관리자보드  모드 Job 취소

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    login_window = QtWidgets.QMainWindow()
    main_window = MainWindow(login_window)
    main_window.show()
    sys.exit(app.exec_())