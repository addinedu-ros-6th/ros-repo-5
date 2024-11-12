from datetime import datetime
import math
import mysql.connector

class taskmanager:
    def __init__(self, login_window):
        a = 1

    def get_db_connection(self):
        """데이터베이스 연결"""
        return mysql.connector.connect(
            host="localhost",
            user="root",
            password="123123",
            database="trashbot"
        )
    
    def minibotstatus(self):
        test = "hello_test"
        return test

    def jobstatus(self,newdata):
        test1 = 'asdf'
        test1 = newdata
        return test1
    
    def job_create(self,user_id, robot_id, navigation_point_id,):
        try:
            connection = self.get_db_connection()
            cursor = connection.cursor()
            create_at = datetime.now()
            job_status = "pending"

            sql = '''INSERT INTO Job (job_status, updated_at) values(%s, %s)'''
            value = (job_status, create_at)
            cursor.execute(sql,tuple(value))
            connection.commit()

            sql = '''select max(id) from Job'''
            cursor.execute(sql)
            max_id = cursor.fetchone()[0]
            
            self.JobLog_add(connection, cursor, user_id, robot_id, navigation_point_id, create_at, job_status, max_id)
            print(f"Job Create : jobid = {max_id}, nav_id = {navigation_point_id}")
            return max_id
        except Exception as e:
            print(f"메시지 전송 오류: {e}")
        finally:
            if 'connection' in locals() and connection.is_connected():
                cursor.close()
                connection.close()
                print("db close")
                
    def Job_cancel(self, job_id, navigation_point_id, user_id):
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

    
    def job_allocate_dump(self,user_id, robot_id, nav_id, job_id, job_status ):
        try:
            connection = self.get_db_connection()
            cursor = connection.cursor()

            create_at = datetime.now()
            self.Job_jobstatus_update(connection, cursor, job_id, job_status)
            self.JobLog_add(connection, cursor, user_id, robot_id, nav_id, create_at, 'allocated', job_id)
        except Exception as e:
            print(f"메시지 전송 오류: {e}")
        finally:
            if 'connection' in locals() and connection.is_connected():
                cursor.close()
                connection.close()
                print("db close")

    def job_allocate(self, robot_status_list, map_pose_list):
        try:
            connection = self.get_db_connection()
            cursor = connection.cursor(dictionary=True)
            
            #로봇 작업중인지 확인필요 ()

            #pending 상태인 Job list 확인
            job_list_sql = '''SELECT jl.job_id, j.job_status, MAX(jl.user_id) AS user_id, MAX(j.updated_at) AS updated_at, jl.navigation_point_id 
                              FROM Job j 
                              LEFT JOIN JobLog jl ON j.id = jl.job_id 
                              WHERE j.job_status = "pending" and jl.user_id is not null
                              GROUP BY j.id, jl.navigation_point_id'''
            cursor.execute(job_list_sql)
            Job_pending_list = cursor.fetchall()
            
            #진행중인 Job, 할당된 Job list 확인
            allocated_job_info_sql = '''SELECT j.job_status AS job_status, j.id AS job_id, jl.navigation_point_id, jl.robot_id, jl.user_id
                                        FROM JobLog jl
                                        JOIN Job j ON jl.job_id = j.id
                                        WHERE (j.job_status = 'inprogress' OR j.job_status = 'allocated')
                                        AND (jl.job_status = 'inprogress' OR jl.job_status = 'allocated')
                                        ORDER BY jl.robot_id ASC, FIELD(j.job_status, 'inprogress', 'allocated')'''
            cursor.execute(allocated_job_info_sql)
            robot_allocated_list = cursor.fetchall()
            
            robot_job_count_info_sql = '''SELECT r.robot_id, COALESCE(COUNT(jl.job_id), 0) AS count
                                          FROM (SELECT DISTINCT robot_id FROM JobLog WHERE robot_id IS NOT NULL
                                            UNION
                                            SELECT 0 UNION SELECT 1) AS r
                                          LEFT JOIN Job j ON j.job_status = 'allocated'
                                          LEFT JOIN JobLog jl ON j.id = jl.job_id AND jl.robot_id = r.robot_id
                                          GROUP BY r.robot_id'''
            cursor.execute(robot_job_count_info_sql)
            robot_job_count_info = cursor.fetchall()
            print(robot_job_count_info)
            # robot_job_count_info.remove(robot_job_count_info[0]) #null값 삭제 (allocated된 Job이 없어도 0으로 찍히게 하기 위함)

            prev_nav_point_id = 0
            battery_limit = 40

            for pending in Job_pending_list:
                pending_nav_point_id=pending['navigation_point_id'] - 1
                if robot_allocated_list:
                    last_line = robot_allocated_list[-1]
                #idle인 로봇 현재 위치부터 pending job까지 거리 구하기
                for job_count_info in robot_job_count_info:
                    robot_id = job_count_info['robot_id']
                    job_count = job_count_info['count']
                    if robot_status_list[robot_id]['status'] == 'idle' and robot_status_list[robot_id]['battery'] >= battery_limit and job_count == 0:
                        cur_x = float(robot_status_list[robot_id]['current_x'])
                        cur_y = float(robot_status_list[robot_id]['current_y'])
                        dest_x = float(map_pose_list[pending_nav_point_id][2])
                        dest_y = float(map_pose_list[pending_nav_point_id][3])
                        globals()[f"robot{robot_id}_eta"] = math.sqrt((cur_x - dest_x) ** 2 + (cur_y - dest_y) ** 2) #eta : Estimate Time Arrive
                        print([f"robot{robot_id}_eta"],globals()[f"robot{robot_id}_eta"] )
                    else:
                        globals()[f"robot{robot_id}_eta"] = 0 #eta : Estimate Time Arrive
                prev_robot_id = None

                #inprogress, allocated 된 job이 있을 경우 총 거리 계산
                if robot_allocated_list: 
                    for row in robot_allocated_list:
                        robot_id = row['robot_id']
                        if robot_status_list[robot_id]['battery'] >= battery_limit and robot_status_list[robot_id]['status'] == 'idle':
                            current_robot_id = robot_id
                            current_nav_point_id = row['navigation_point_id'] - 1
                            print("nav_point_id", current_nav_point_id + 1)
                            if (current_robot_id != prev_robot_id): #처음 Job은 현재 위치에서 목적지까지의 시간 계산
                                cur_x = float(robot_status_list[robot_id]['current_x'])
                                cur_y = float(robot_status_list[robot_id]['current_y'])
                                print("first cur",cur_x,cur_y)
                                dest_x = float(map_pose_list[current_nav_point_id][2])
                                dest_y = float(map_pose_list[current_nav_point_id][3])
                                print("first dest",dest_x,dest_y)
                                globals()[f"robot{robot_id}_eta"] += math.sqrt((cur_x - dest_x) ** 2 + (cur_y - dest_y) ** 2) #eta : Estimate Time Arrive
                                print(f"robot{robot_id}_eta", globals()[f"robot{robot_id}_eta"])
                            elif current_robot_id == prev_robot_id:
                                cur_x = float(map_pose_list[prev_nav_point_id][2])
                                cur_y = float(map_pose_list[prev_nav_point_id][3])
                                print("second cur",cur_x,cur_y)
                                dest_x = float(map_pose_list[current_nav_point_id][2])
                                dest_y = float(map_pose_list[current_nav_point_id][3])
                                print("second dest",dest_x,dest_y)
                                globals()[f"robot{robot_id}_eta"] += math.sqrt((cur_x - dest_x) ** 2 + (cur_y - dest_y) ** 2)
                                print(f"robot{robot_id}_eta", globals()[f"robot{robot_id}_eta"])
                            
                            if (current_robot_id-1 == prev_robot_id):# and prev_nav_point_id != 0): #로봇이 바꼈을 때, 이전 로봇의 total 시간 계산 (last job과 pending job 과의 시간 계산)
                                cur_x = float(map_pose_list[prev_nav_point_id][2])
                                cur_y = float(map_pose_list[prev_nav_point_id][3])
                                print("total",cur_x,cur_y)               
                                dest_x = float(map_pose_list[pending_nav_point_id][2])
                                dest_y = float(map_pose_list[pending_nav_point_id][3])
                                print("total",dest_x,dest_y)               
                                globals()[f"robot{robot_id-1}_eta"] += math.sqrt((cur_x - dest_x) ** 2 + (cur_y - dest_y) ** 2)
                                print("result : ",f"robot{robot_id-1}_eta", globals()[f"robot{robot_id-1}_eta"])
                            elif row == last_line and len(robot_allocated_list) > 1:  #마지막 로봇일 때, 마지막 job과 pending job 거리 계산
                                cur_x = float(map_pose_list[current_nav_point_id][2])
                                cur_y = float(map_pose_list[current_nav_point_id][3])
                                print("total",cur_x,cur_y)               
                                dest_x = float(map_pose_list[pending_nav_point_id][2])
                                dest_y = float(map_pose_list[pending_nav_point_id][3])
                                print("total",dest_x,dest_y)               
                                globals()[f"robot{robot_id}_eta"] += math.sqrt((cur_x - dest_x) ** 2 + (cur_y - dest_y) ** 2)
                                print(f"robot{robot_id}_eta", globals()[f"robot{robot_id}_eta"])

                            prev_robot_id = robot_id
                            prev_nav_point_id = current_nav_point_id

                    #eta 최소값 변수 구하기 (이미 할당된 로봇이 있을 경우)
                    for i in range(len(robot_status_list)-1):
                        if robot_status_list[i]['battery'] > battery_limit and robot_status_list[robot_id]['status'] == 'idle':
                            if globals()[f"robot{i}_eta"] > globals()[f"robot{i+1}_eta"]:
                                eta_min_robot = i+1
                            else:
                                eta_min_robot = i
                    print(f"job allocated robot : {eta_min_robot}, job_id : {pending['job_id']}")
                    create_at = datetime.now()
                    self.Job_jobstatus_update(connection, cursor, pending['job_id'], 'allocated')
                    self.JobLog_add(connection, cursor, row['user_id'], eta_min_robot, pending_nav_point_id+1,create_at, 'allocated', pending['job_id'])
                else:
                    #eta 최소값 변수 구하기 (할당된 로봇이 없을 경우)
                    for i in range(len(robot_status_list)-1):
                        if robot_status_list[i]['battery'] > battery_limit and robot_status_list[robot_id]['status'] == 'idle':
                            if globals()[f"robot{i}_eta"] > globals()[f"robot{i+1}_eta"]:
                                eta_min_robot = i+1
                            else:
                                eta_min_robot = i
                    print(f"job allocated robot : {eta_min_robot}, job_id : {pending['job_id']}")
                    create_at = datetime.now()
                    self.Job_jobstatus_update(connection, cursor, pending['job_id'], 'allocated')
                    self.JobLog_add(connection, cursor, pending['user_id'], eta_min_robot, pending_nav_point_id+1,create_at, 'allocated', pending['job_id'])

                cursor.execute(job_list_sql)
                Job_pending_list = cursor.fetchall()
                cursor.execute(allocated_job_info_sql)
                robot_allocated_list = cursor.fetchall()
                cursor.execute(robot_job_count_info_sql)
                robot_job_count_info = cursor.fetchall()
        except Exception as e:
                    print(f"메시지 전송 오류: {e}")
        finally:
            if 'connection' in locals() and connection.is_connected():
                cursor.close()
                connection.close()
                print("db close")

    def job_inprogress(self, robot_id, nav_id):
        try:#쓰레기장 가야되는 Job이 있는지 확인하고 있으면 우선으로 Job 줘야함.
            connection = self.get_db_connection()
            cursor = connection.cursor(dictionary=True)
            if nav_id == 8 or nav_id == 9 :
                sql = '''SELECT j.id AS job_id, j.job_status AS job_table_status, jl.robot_id, jl.job_status AS joblog_status, jl.create_at, jl.user_id, jl.navigation_point_id
                    FROM Job j
                    JOIN JobLog jl ON j.id = jl.job_id
                    WHERE j.job_status = 'allocated' AND jl.robot_id = (%s) AND jl.job_status = "allocated" AND jl.navigation_point_id = (%s)
                    order by create_at asc'''
                value = (robot_id, nav_id)
            else:
                sql = '''SELECT j.id AS job_id, j.job_status AS job_table_status, jl.robot_id, jl.job_status AS joblog_status, jl.create_at, jl.user_id, jl.navigation_point_id
                        FROM Job j
                        JOIN JobLog jl ON j.id = jl.job_id
                        WHERE j.job_status = 'allocated' AND jl.robot_id = (%s) AND jl.job_status = "allocated"
                        order by create_at asc'''
                value = (robot_id,)

            cursor.execute(sql,tuple(value))
            recently_allocated_job = cursor.fetchall()[0]
            user_id = recently_allocated_job['user_id']
            job_id = recently_allocated_job['job_id']
            navigation_point_id = recently_allocated_job['navigation_point_id']
            job_status = "inprogress"
            create_at = datetime.now()

            self.Job_jobstatus_update(connection, cursor, job_id, job_status)
            self.JobLog_add(connection, cursor, user_id, robot_id, navigation_point_id,create_at, job_status, job_id)
            connection.commit()
            return job_id, navigation_point_id
        except Exception as e:
            print(f"메시지 전송 오류: {e}")
            cursor.close()
            connection.close()
            print("db close")
        finally:
            cursor.close()
            connection.close()
            print("db close")

    def update_job_complete_and_error(self, job_id, job_status):
        try:#쓰레기장 가야되는 Job이 잇는지 확인하고 있으면 우선으로 Job 줘야함.
            connection = self.get_db_connection()
            cursor = connection.cursor(dictionary=True)
            
            sql = '''select * from JobLog where job_id = (%s) and job_status = "inprogress"'''
            value = (job_id,)
            cursor.execute(sql, tuple(value))
            inprogress_job_list = cursor.fetchall()[0]

            navigation_point_id = inprogress_job_list['navigation_point_id']
            user_id = inprogress_job_list['user_id']
            robot_id = inprogress_job_list['robot_id']
            create_at = datetime.now()

            self.Job_jobstatus_update(connection, cursor, job_id, job_status)
            self.JobLog_add(connection, cursor, user_id, robot_id, navigation_point_id, create_at, job_status, job_id)
            return navigation_point_id, user_id, robot_id
        except Exception as e:
            print(f"메시지 전송 오류: {e}")
            cursor.close()
            connection.close()
            print("db close")
        finally:
            cursor.close()
            connection.close()
            print("db close")

    def check_job_allocated(self, robot_id):
        connection = self.get_db_connection()
        cursor = connection.cursor(dictionary=True)

        sql = '''SELECT * 
                FROM JobLog 
                WHERE job_id IN (
                    SELECT id 
                    FROM Job 
                    WHERE job_status = 'allocated'
                ) 
                AND robot_id = (%s) 
                AND job_status = "allocated"'''
        
        value = (robot_id,)
        cursor.execute(sql, tuple(value))
        allocated_job = cursor.fetchall()
        if allocated_job:
            nav_id = allocated_job[0]['navigation_point_id']
            for i in range(len(allocated_job)): #dump 목적지 유무 확인
                if allocated_job[i]['navigation_point_id'] == 8 or allocated_job[i]['navigation_point_id'] == 9:
                    nav_id = allocated_job[i]['navigation_point_id']
        else:
            nav_id = None

        return nav_id
    
    def job_refresh(self):
        try:
            connection = self.get_db_connection()
            cursor = connection.cursor(dictionary = True)

            sql = '''SELECT * 
                FROM JobLog 
                WHERE job_id IN (
                    SELECT id 
                    FROM Job 
                    WHERE job_status = 'allocated'
                ) 
                AND job_status = "allocated"'''
            cursor.execute(sql) 
            allocated_job_info = cursor.fetchall() #체크 해제된 순간 해당 navigation_point_id의 최신 job_id 불러오기

            for job_info in allocated_job_info:
                job_id = job_info['job_id']
                user_id = job_info['user_id']
                nav_id = job_info['navigation_point_id']
                create_at = datetime.now()
                job_status = 'pending'
                robot_id = None
                self.Job_jobstatus_update(connection, cursor, job_id, job_status)
                self.JobLog_add(connection, cursor, user_id, robot_id, nav_id, create_at, job_status, job_id)
                print(f"Job Status Changed {job_info['job_status']} to job_status, Job_ID : {job_id}, robot_id : {robot_id}, nav_id : {nav_id}")
        except Exception as e:
                print(f"메시지 전송 오류: {e}")
                cursor.close()
                connection.close()
                print("db close")
        finally:
            cursor.close()
            connection.close()
            print("db close")

    def update_job_error(self, job_id):
        try:
            connection = self.get_db_connection()
            cursor = connection.cursor(dictionary = True)

            sql = '''select * from JobLog
                     where job_id = (%s)
                     order by create_at desc limit 1'''
            value = (job_id,)
            cursor.execute(sql,tuple(value)) 
            joblog_info = cursor.fetchone() #체크 해제된 순간 해당 navigation_point_id의 최신 job_id 불러오기

            nav_id = joblog_info['navigation_point_id']
            user_id = joblog_info['user_id']
            robot_id = joblog_info['robot_id']
            job_status = "error"
            create_at = datetime.now()

            self.Job_jobstatus_update(self, connection, cursor, job_id, job_status)
            self.JobLog_add(self, connection, cursor, user_id, robot_id, nav_id,create_at, job_status, job_id)
            return nav_id, user_id
        except Exception as e:
                print(f"메시지 전송 오류: {e}")
                cursor.close()
                connection.close()
                print("db close")
        finally:
            cursor.close()
            connection.close()
            print("db close")

    def Job_jobstatus_check(self, navigation_point_id):
        try:
            connection = self.get_db_connection()
            cursor = connection.cursor(dictionary = True)

            sql = '''select job_id, robot_id from JobLog where navigation_point_id = (%s) order by create_at desc limit 1'''
            value = (navigation_point_id,)
            cursor.execute(sql,tuple(value)) 
            job_info = cursor.fetchone() #체크 해제된 순간 해당 navigation_point_id의 최신 job_id 불러오기
            job_id = job_info['job_id']
            robot_id = job_info['robot_id']

            sql = '''select job_status from Job where id = (%s)'''
            value = (job_id,)
            cursor.execute(sql,tuple(value)) 
            job_status = cursor.fetchone()['job_status'] #JobLog에서 불러온 job_id의 job_status 불러오기

            return job_id, job_status, robot_id
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
        print(f"JobLog Update job_id: {max_id}, Job_status: {job_status}, robot_id : {robot_id}, nav_id : {navigation_point_id}")

    def Job_jobstatus_update(self, connection, cursor, job_id, job_status):
        sql = '''update Job set job_status = (%s) where id = (%s)''' #Job status cancel 변경
        value = (job_status, job_id,)
        cursor.execute(sql,tuple(value)) #체크 해제된 순간 해당 navigation_point_id의 최신 job_id 불러오기
        connection.commit()
    
    def map_data(self):
        try:
            connection = self.get_db_connection()
            cursor = connection.cursor()

            sql = '''select * from NavigationPoint'''
            cursor.execute(sql)
            map_pose_list = cursor.fetchall()
            return map_pose_list
        except Exception as e:
            print(f"메시지 전송 오류: {e}")
        finally:
            if 'connection' in locals() and connection.is_connected():
                cursor.close()
                connection.close()
                print("db close")
