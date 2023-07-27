from ur_robot_lite_controller import UR5Controller
import rospy
from universal_robots_lite.msg import position
from universal_robots_lite.msg import joint
from universal_robots_lite.msg import position_command
from universal_robots_lite.msg import joint_command


def main():
    rospy.init_node('ur5_user', anonymous=True)

    # Replace '192.168.1.104' with your UR5's IP address
    ur5 = UR5Controller('192.168.1.104')

    # Now you can use ur5 to control your robot
    # For example, let's move the UR5. You will need to replace 'your_command' with an actual command
    # ur5.move_ur5(your_command)
    # rospy.spin()

if __name__ == '__main__':
    main()