self.r0_publisher = self.create_publisher(RobotStatus, '', 10)
self.r1_publisher = self.create_publisher(RobotStatus, 'robot1/RobotStatus', 10)
# 로봇 amcl_pose 구독
self.robot0_subscription = self.create_subscription(PoseWithCovarianceStamped,'/robot0/amcl_pose', self.robot0_pose_callback, 10)
self.robot0_subscription = self.create_subscription(PoseWithCovarianceStamped,'/robot1/amcl_pose', self.robot_pose_callback, 10)
timer_period = 0.5
self.timer = self.create_timer(timer_period, self.status_callback)
def robot0_pose_callback(self, msg):
    self.robot0_pose = msg.pose.pose  # Pose 정보 저장
    self.get_logger().info(f"Robot 0 Pose: {self.robot0_pose}")
def robot1_pose_callback(self, msg):
    self.robot1_pose = msg.pose.pose  # Pose 정보 저장
    self.get_logger().info(f"Robot 1 Pose: {self.robot1_pose}")
def status_callback(self):
    # 로봇 0 상태 업데이트 및 메시지 발행
    msg_r0 = RobotStatus()
    self.robot0_battery_time += 0.5
    if self.robot0_battery_time > 100:
        if self.robot0_battery_status > 0:  # 배터리 값이 음수가 되지 않도록
            self.robot0_battery_status -= 1
        self.robot0_battery_time = 0
    robot0_state = self.shared_state.get_state("robot0")
    msg_r0.battery_status = self.robot0_battery_status
    msg_r0.robot_status = robot0_state["status"]
    msg_r0.x = self.robot0_pose_x
    msg_r0.y = self.robot0_pose_y
    self.r0_publisher.publish(msg_r0)
    # 로봇 1 상태 업데이트 및 메시지 발행
    msg_r1 = RobotStatus()
    self.robot1_battery_time += 0.5
    if self.robot1_battery_time > 100:
        if self.robot1_battery_status > 0:
            self.robot1_battery_status -= 1
        self.robot1_battery_time = 0
    robot1_state = self.shared_state.get_state("robot1")
    msg_r1.battery_status = self.robot1_battery_status
    msg_r1.robot_status = robot1_state["status"]
    msg_r1.x = self.robot1_pose_x
    msg_r1.y = self.robot1_pose_y
    self.r1_publisher.publish(msg_r1)







