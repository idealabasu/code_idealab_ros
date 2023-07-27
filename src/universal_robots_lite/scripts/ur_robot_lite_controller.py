import threading
import rospy
from universal_robots_lite.msg import position
from universal_robots_lite.msg import joint
from universal_robots_lite.msg import position_command
from universal_robots_lite.msg import joint_command

import math3d as m3d
import urx
import time
import numpy
import math
from numpy import pi

class UR5Controller:
    def __init__(self, ur5_port="192.168.1.104", tcp=(0, 0, 0.1476, 0, 0, 0), payload_m=0.61, payload_location=(0, 0, 0)):
        # Initialize ROS node
        rospy.init_node('ur5_controller_node', anonymous=True)
        self.ur5_port = ur5_port
        self.tcp = tcp
        self.payload_m = payload_m
        self.payload_location = payload_location
        # Initialize urx Robot
        self.ur5 = urx.Robot(self.ur5_port)
        time.sleep(3)

        if self.ur5.host != ur5_port:
            raise Exception("Failed to connect to UR5 robot.")
        print("Connected to UR5 robot.")
        print(self.ur5)


        self.ur5.set_tcp(self.tcp)
        self.ur5.set_payload(self.payload_m, self.payload_location)

        # Initialize publishers and subscribers
        self.pose_publisher = rospy.Publisher('ur5_pose_publisher', position, queue_size=10)
        self.joint_publisher = rospy.Publisher('ur5_joint_publisher', joint, queue_size=10)
        self.publisher_thread = threading.Thread(target=self.pose_publisher_function)
        self.publisher_thread.start()
    def set_idealab_cord(self):
        # this is just an handy fucntion of setting the robot cord sys.
        # the ur5-cb is installed 45 deg tilted
        # the ur5-e is installed aligned with the test bed
        if self.ur5_port == "192.168.1.104":
            self.moving_vector_left = numpy.array((1, 1, 0)) * math.sqrt(2) / 2
            self.moving_vector_right = -numpy.array((1, 1, 0)) * math.sqrt(2) / 2
            self.moving_vector_forward = numpy.array((1, -1, 0)) * math.sqrt(2) / 2
            self.moving_vector_backward = numpy.array((-1, 1, 0)) * math.sqrt(2) / 2
            self.moving_vector_up = numpy.array((0, 0, 1))
            self.moving_vector_down = numpy.array((0, 0, -1))

        if self.ur5_port == "192.168.1.103":
            self.moving_vector_left = numpy.array((1, 0, 0))
            self.moving_vector_right = numpy.array((-1, 0, 0))
            self.moving_vector_forward = numpy.array((0, -1, 0))
            self.moving_vector_backward = numpy.array((0, 1, 0))
            self.moving_vector_up = numpy.array((0, 0, 1))
            self.moving_vector_down = numpy.array((0, 0, -1))

    def pose_publisher_function(self):
        # These pose and joint angles is according to "Base" frame on the teachpad
        # pose is in m/rad
        # joint angle is in rad
        rate = rospy.Rate(1000)
        while not rospy.is_shutdown():
            pose = self.ur5.get_pose()
            orient = pose.get_orient()
            q = orient.unit_quaternion
            pose_data = position()
            pose_data.q[0] = q[0]
            pose_data.q[1] = q[1]
            pose_data.q[2] = q[2]
            pose_data.q[3] = q[3]
            pose_data.p[0] = pose.pos[0]
            pose_data.p[1] = pose.pos[1]
            pose_data.p[2] = pose.pos[2]
            pose_data.is_moving = self.ur5.is_program_running()
            self.pose_publisher.publish(pose_data)

            joint_angles = self.ur5.getj()
            joint_data = joint()
            joint_data.joint_angles[:] = joint_angles[:]
            self.joint_publisher.publish(joint_data)
            rate.sleep()

    # here is some handy functions I used to move the robot, it's all based on
    def move_ur5(self, v, a, wait=False):
        current_pose = self.ur5.get_pose()
        current_pose.pos[:] += self.moving_vector
        self.ur5.movel(current_pose, vel=v, acc=a, wait=wait)


    def rotate_around_h(self,angle_r, v, a, w):
        # this code is designed so that rotate the x axis of the TCP make sure tcp is correctly configureed
        # if rotate around the base flange, set tcp as zeros
        # rotate around x axis
        # Tct.orient = m3d.Orientation.new_euler((pi/2,0,0), encoding='XYZ')
        # rotate around y-axis
        # Tct.orient = m3d.Orientation.new_euler((0,pi/2,0), encoding='XYZ')
        # rotate around z-axis
        # Tct.orient = m3d.Orientation.new_euler((0,0,pi/2), encoding='XYZ')
        pose = self.ur5.get_pose()
        Tct = m3d.Transform()
        Tct.pos = m3d.Vector(0, 0, 0)
        Tct.orient = m3d.Orientation.new_euler(angle_r, encoding='XYZ')
        new_pos = pose * Tct
        self.ur5.movel(new_pos, vel=v, acc=1, wait=w)


    def shake_a_clean(self):
        print("Warning! Check if robot configuration allows these set range of motion before proceeed! YOU WILL BE RESPONSIBLE FOR USING THIS FUNSTION!")
        input()
        shake_vel = 0.1
        for item in range(2):
            clean_angle = numpy.array([pi / 4, 0, 0])
            self.rotate_around_h(clean_angle, shake_vel, 1, True)
            time.sleep(1)
            self.rotate_around_h(-2 * clean_angle, shake_vel, 1, True)
            time.sleep(1)
            self.rotate_around_h(clean_angle, shake_vel, 1, True)
            time.sleep(1)
            clean_angle = numpy.array([0, pi / 4, 0])
            self.rotate_around_h(clean_angle, shake_vel, 1, True)
            time.sleep(1)
            self.rotate_around_h(-2 * clean_angle, shake_vel, 1, True)
            time.sleep(1)
            self.rotate_around_h(clean_angle, shake_vel, 1, True)
            time.sleep(1)


if __name__ == "__main__":
    ur5 = UR5Controller()

    ## if uring ur5.xxx you will be access the function I defined
    ## if using ur5.ur5.xxx, it's original urx object
    ## basilly this code add a poublisher function to the urx method so that it can be easily used in ros
    ur5.shake_a_clean()