import cv2
from geometry_msgs.msg import Twist
from rclpy.node import Node
from rclpy.qos import QoSProfile
from rclpy.qos import qos_profile_sensor_data
from sensor_msgs.msg import LaserScan


class LaneTracking(Node):

    def __init__(self):
        super().__init__('lane_tracking')
        self.cap = cv2.VideoCapture(0)
        self.linear_velocity = [0.1, 0.0, 0.0, 0.0, 0.0]  # unit: m/s
        self.angular_velocity = [0.0, 0.2, 0.15, -0.15, 0.0]  # unit: m/s
        self.obstacle = [True, True, True, True] # Values for Front, Back, Right, Left. True if obstacle present False if obstacle is not available.

        qos = QoSProfile(depth=10)
        self.cmd_vel_pub = self.create_publisher(Twist, 'cmd_vel', qos)
        self.cmd_vel_raw_sub = self.create_subscription(Twist, 'cmd_vel_raw', self.cmd_vel_raw_callback, qos)
        self.update_timer = self.create_timer(0.010, self.update_callback)
        self.get_logger().info("Lane Tracker Node is Initialized!.")


    def cmd_vel_raw_callback(self, msg):
        self.linear_velocity = msg.linear.x
        self.angular_velocity = msg.angular.z

    def update_callback(self):
        self.track_road()

    def get_direction(self, img):
        (H, W, C) = img.shape
        turn = [0, 0, 0, 0, 0]
        Y = int((H/3)*2)
        X = int((W/4))
        X_E = (X*3)
        im = img.copy()
        img = img[Y:H, X:X_E]

        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        ret, img = cv2.threshold(img, 128, 255, cv2.THRESH_BINARY)

        (H, W) = img.shape
        X = int((W/5))
        X_E = (X*4)
        left = img[:,0:X]
        mid = img[:,X:X_E]
        right = img[:,X_E:]

        if(255 in left):
            turn[2] = 1
            print("Left")
        elif(255 in right):
            turn[3] = 1
            print("Right")
        elif(255 in mid):
            turn[0] = 1
            print("Forward")
        else:
            turn[4] = 1
            print("stopped")
        
        return turn


    def track_road(self):
        twist = Twist()
        ret, img = self.cap.read()
        self.obstacle = self.get_direction(img)
        indx = 4
        if self.obstacle[0] == 1:
            indx = 0
        elif self.obstacle[1] == 1:
            indx = 1
        elif self.obstacle[2] == 1:
            indx = 2
        elif self.obstacle[3] == 1:
            indx = 3
        else:
            self.get_logger().info("Not able to locate the road. Robot stopped.")

        twist.linear.x = self.linear_velocity[indx]
        twist.angular.z = self.angular_velocity[indx]
        
        self.cmd_vel_pub.publish(twist)
