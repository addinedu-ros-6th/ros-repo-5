from PyQt5 import QtWidgets, uic
from PyQt5.QtCore import pyqtSignal
import sys
import os
import mysql.connector
import hashlib

# Python 경로에 필요한 디렉토리 추가
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

# Robot_System_Server 폴더부터 시작하는 import
from robot_system_server.EnterpriseManager.ServerGui.server import MainWindow
from RobotSystemHub.UserGui.user import UserWindow

class LoginWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        # UI 파일은 같은 디렉토리에 있으므로 직접 파일명만 사용
        uic.loadUi('login.ui', self)

        # 초기화
        self.setup_ui()
        self.setup_connections()
        
        # 서버와 유저 윈도우 생성
        self.main_window = MainWindow(self)
        self.user_window = UserWindow(self)

    def setup_ui(self):
        """UI 초기 설정"""
        self.text_password.setEchoMode(QtWidgets.QLineEdit.Password)

    def setup_connections(self):
        """시그널-슬롯 연결"""
        self.login_button.clicked.connect(self.attempt_login)

    def get_db_connection(self):
        """데이터베이스 연결"""
        return mysql.connector.connect(
            host="database-1.cpog6osggiv3.ap-northeast-2.rds.amazonaws.com",
            user="arduino_PJT",
            password="1234",
            database="ardumension"
        )
    
    def verify_password(self, stored_hash, stored_salt, provided_password):
        """비밀번호 검증"""
        calculated_hash = hashlib.sha256(
            (provided_password + stored_salt).encode()
        ).hexdigest()
        return calculated_hash == stored_hash

    def attempt_login(self):
        """로그인 시도"""
        employee_number = self.text_id.text()
        password = self.text_password.text()
        
        if not employee_number or not password:
            QtWidgets.QMessageBox.warning(
                self,
                '입력 오류',
                '사원번호와 비밀번호를 모두 입력해주세요.'
            )
            return
        
        try:
            connection = self.get_db_connection()
            cursor = connection.cursor()
            sql = """
            SELECT password_hash, password_salt, role 
            FROM RobotUser 
            WHERE employee_number = %s
            """
            cursor.execute(sql, (employee_number,))
            result = cursor.fetchone()
            
            if result:
                stored_hash, stored_salt, role = result
                
                success_message = QtWidgets.QMessageBox()
                success_message.setIcon(QtWidgets.QMessageBox.Information)
                success_message.setWindowTitle('로그인 성공')
                success_message.setText(f'로그인 성공!\n역할: {role}')
                success_message.setStandardButtons(QtWidgets.QMessageBox.Ok)
                
                if success_message.exec_() == QtWidgets.QMessageBox.Ok:
                    self.hide()
                    if role.lower() == 'admin':
                        self.main_window.show()
                    else:
                        self.user_window.show()
            else:
                QtWidgets.QMessageBox.warning(
                    self,
                    '로그인 실패',
                    '존재하지 않는 사용자입니다.'
                )
        except mysql.connector.Error as err:
            QtWidgets.QMessageBox.critical(
                self,
                '데이터베이스 오류',
                f'데이터베이스 오류가 발생했습니다: {err}'
            )
        finally:
            if 'connection' in locals() and connection.is_connected():
                cursor.close()
                connection.close()

def main():
    app = QtWidgets.QApplication(sys.argv)
    login_window = LoginWindow()
    login_window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()