from PyQt5 import QtWidgets, uic
from PyQt5.QtCore import pyqtSignal
import sys
import resource_rc
import mysql.connector
import hashlib

class LoginWindow(QtWidgets.QMainWindow):
    login_successful = pyqtSignal()  

    def __init__(self):
        super().__init__()
        uic.loadUi('login.ui', self)
        self.login_button.clicked.connect(self.attempt_login)

        self.text_password.setEchoMode(QtWidgets.QLineEdit.Password)

    def get_db_connection(self):
        return mysql.connector.connect(
            host="database-1.cpog6osggiv3.ap-northeast-2.rds.amazonaws.com",
        user="arduino_PJT",
        password="1234",
        database="ardumension"
    )
    
    def verify_password(self, stored_hash, stored_salt, provided_password):
        calculated_hash = hashlib.sha256(
            (provided_password + stored_salt).encode()
        ).hexdigest()
        return calculated_hash == stored_hash



    def attempt_login(self):
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
                    self.login_successful.emit()
                    self.close()
                else:
                    QtWidgets.QMessageBox.warning(
                        self,
                        '로그인 실패',
                        '잘못된 비밀번호입니다.'
                    )
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
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    login_window = LoginWindow()
    login_window.show()
    sys.exit(app.exec_())