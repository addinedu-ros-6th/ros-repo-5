from datetime import datetime
import math
import mysql.connector

class taskmanager:
    def __init__(self, login_window):
        a = 1

    def get_db_connection(self):
        """데이터베이스 연결"""
        return mysql.connector.connect(
            host="database-1.cpog6osggiv3.ap-northeast-2.rds.amazonaws.com",
            user="arduino_PJT",
            password="1234",
            database="ardumension"
        )
    
    def minibotstatus(self):
        test = "hello_test"
        return test

    def jobstatus(self,newdata):
        test1 = 'asdf'
        test1 = newdata
        return test1
    
    def job_create(self,user_id, navigation_point_id,):
        try:
            connection = self.get_db_connection()
            cursor = connection.cursor()
            create_at = datetime.now()
            robot_id = None
            job_status = "pending"

            sql = '''INSERT INTO Job (job_status, updated_at) values(%s, %s)'''
            value = (job_status, create_at)
            cursor.execute(sql,tuple(value))
            connection.commit()

            sql = '''select max(id) from Job'''
            cursor.execute(sql)
            max_id = cursor.fetchone()[0]
            
            self.JobLog_add(connection, cursor, user_id, robot_id, navigation_point_id, create_at, job_status, max_id)
        except Exception as e:
                    print(f"메시지 전송 오류: {e}")
        finally:
            if 'connection' in locals() and connection.is_connected():
                cursor.close()
                connection.close()
                print("db close")

    def Job_update_notinprogress_to_cancel(self, job_id, navigation_point_id, user_id):
        try:
            connection = self.get_db_connection()
            cursor = connection.cursor()
            job_status = 'cancel'

            self.Job_jobstatus_update(connection, cursor, job_id, job_status)

            robot_id = None
            create_at = datetime.now()
            self.JobLog_add(connection, cursor, user_id, robot_id, navigation_point_id, create_at, job_status, job_id)
            return 'cancel'
        except Exception as e:
                print(f"메시지 전송 오류: {e}")
                cursor.close()
                connection.close()
                print("db close")
        finally:
            cursor.close()
            connection.close()
            print("db close")

    def update_job_allocate(self, minibotname, goalname):
        minibot = [] #
        minibot_status = [] #Minibot_Name, Battery, Status, cur_x, cur_y
        minibot_job_count = []
        minibot_count = 2
        
        for i in range(minibot_count):
            if minibot[i]['battery'] >= 40 :
                if minibot_job_count[i] >= 1:
                    a = 1
                    #self.current_pos_to_destination(self, minibot_status[i]['cur_x'], minibot_status[i]['cur_x'], dest_x, dest_y)

    def current_pos_to_destination(self, cur_x, cur_y, dest_x, dest_y):
        eta = math.sqrt((dest_x - cur_x) ** 2 + (dest_y - cur_y) ** 2) #eta : Estimate Time Arrive
        return eta


    def update_job_inprogress():
        a = 1

    def update_job_complete():
        a = 1
        
    def Job_jobstatus_check(self, navigation_point_id):
        try:
            connection = self.get_db_connection()
            cursor = connection.cursor()

            sql = '''select job_id from JobLog where navigation_point_id = (%s) order by create_at desc limit 1'''
            value = (navigation_point_id,)
            cursor.execute(sql,tuple(value)) 
            job_id = cursor.fetchone()[0] #체크 해제된 순간 해당 navigation_point_id의 최신 job_id 불러오기

            sql = '''select job_status from Job where id = (%s)'''
            value = (job_id,)
            cursor.execute(sql,tuple(value)) 
            job_status = cursor.fetchone()[0] #JobLog에서 불러온 job_id의 job_status 불러오기
            return job_id, job_status
        except Exception as e:
                print(f"메시지 전송 오류: {e}")
                cursor.close()
                connection.close()
                print("db close")
        finally:
            cursor.close()
            connection.close()
            print("db close")

    def JobLog_add(self, connection, cursor, user_id, robot_id, navigation_point_id,create_at, job_status, max_id):
        sql = '''INSERT INTO JobLog (user_id, robot_id, navigation_point_id, create_at, job_status, job_id) values(%s, %s, %s, %s, %s, %s)'''
        value = (user_id, robot_id, navigation_point_id,create_at, job_status, max_id)
        cursor.execute(sql,tuple(value))
        connection.commit()

    def Job_jobstatus_update(self, connection, cursor, job_id, job_status):
        sql = '''update Job set job_status = (%s) where id = (%s)''' #Job status cancel 변경
        value = (job_status, job_id,)
        cursor.execute(sql,tuple(value)) #체크 해제된 순간 해당 navigation_point_id의 최신 job_id 불러오기
        connection.commit()
    