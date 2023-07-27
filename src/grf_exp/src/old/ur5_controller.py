#!/usr/bin/env python3
import rospy
import time
import roslaunch
from universal_robots.msg import position
from universal_robots.msg import joint
from universal_robots.msg import position_command
from universal_robots.msg import joint_command
from ati_nano.msg import force_torque
import numpy
from numpy import pi
import math

class ur5_command_publisher:
    def __init__(self,timeout=60):
        try:
            rospy.init_node('ur5_node')
        except:
            rospy.loginfo("node already running")
        self.pose_publisher = rospy.Publisher('ur5_control_pose_level', position_command, queue_size=1,latch=True)
        self.joint_publisher = rospy.Publisher('ur5_control_joint_level', joint_command, queue_size=1,latch=True)
        ur5_launch_path = "/home/dongting/Documents/catkin_ws/src/code_idealab_ros/src/universal_robots/launch/ur5_control.launch"
        try:
            uuid = roslaunch.rlutil.get_or_generate_uuid(None, False)
            roslaunch.configure_logging(uuid)
            ur5_launch = roslaunch.parent.ROSLaunchParent(uuid, [ur5_launch_path])
            ur5_launch.start()
            time.sleep(5)
        except:
            rospy.loginfo("cant not start ur5")
        time_a = time.time()
        timeout = 30
        while (self.pose_publisher.get_num_connections()==0) and (self.joint_publisher.get_num_connections()==0):
            rospy.loginfo("waiting for ur5 sub connection")
            time.sleep(1)
            if time.time()-time_a >timeout:
                rospy.loginfo("Connection Timeout")
                break
        rospy.loginfo("connected to ur5 subscriber")
        self.pose_subscriber = rospy.Subscriber('ur5_pose_publisher',position,self.position_callback)
        self.joint_subscriber = rospy.Subscriber('ur5_joint_publisher',joint,self.joint_callback)
        self.ati_subscriber = rospy.Subscriber('/ati_node_chatter',force_torque,self.ati_callback)
        while (self.ati_subscriber.get_num_connections()==0):
            time.sleep(1)
            rospy.loginfo("waiting for ati pub connection")
            if time.time()-time_a >timeout:
                rospy.loginfo("Connection Timeout")
            break
        rospy.loginfo("connected to ati publisher")
        
    def position_callback(self,data):
        self._position = data
    def joint_callback(self,data):
        self._joint = data
    def ati_callback(self,data):
        self._ati_force  = data
    
    def _get_is_moving(self):
        return self._position.is_moving
        
    def dummy_wait_for_move(self,count_timeout):
        count=0
        time.sleep(0.5)
        while count<count_timeout:
            if self._position.is_moving==False:
                count+=1
#        print("done")
    
    def rotate_ur5_ros(self,RPY,vel,acc=1,wait=True):
        pos_to_pub = position_command()
        pos_to_pub.pos = [0,0,0]
        pos_to_pub.RPY = RPY
        pos_to_pub.vel = vel
        pos_to_pub.acc = acc
        pos_to_pub.wait_flag = wait
        self.pose_publisher.publish(pos_to_pub)
        if wait:
#            print(wait)
            self.dummy_wait_for_move(20)
#        print("finished")
#        self.wait_count(10)
#        time.sleep(15)
        
    def movel_ur5_ros(self,pos,vel,acc=1,wait=True):
        pos_to_pub = position_command()
        pos_to_pub.pos = pos
        pos_to_pub.RPY = [0,0,0]
        pos_to_pub.vel = vel
        pos_to_pub.acc = acc
        pos_to_pub.wait_flag = wait
        self.pose_publisher.publish(pos_to_pub)
#        distance = numpy.sqrt(numpy.sum(numpy.square(pos)))
#        wait_time = distance/vel
#        time.sleep(wait_time*1.5)
        if wait:
#            print(wait)
            self.dummy_wait_for_move(20)
#        print("finished")

    def movej_ur5_ros(self,joint_angles,vel,acc=1,wait=True):
        joint_to_pub = joint_command()
        joint_to_pub.joint_angles = joint_angles
        joint_to_pub.vel = vel
        joint_to_pub.acc = acc
        joint_to_pub.wait_flag = wait
        self.joint_publisher.publish(joint_to_pub)
        if wait:
            self.dummy_wait_for_move(20)

    def shake_a_clean(self):
        import time
        clean_wait_time = 0.5
        shake_vel = 0.1
        for item in range(2):
            clean_angle  = numpy.array([pi/4,0,0])
            self.rotate_ur5_ros(clean_angle,shake_vel,1,True)
            time.sleep(clean_wait_time)
            self.rotate_ur5_ros(-2*clean_angle,shake_vel,1,True)
            time.sleep(clean_wait_time)
            self.rotate_ur5_ros(clean_angle,shake_vel,1,True)
            time.sleep(clean_wait_time)
            clean_angle  = numpy.array([0,pi/4,0])
            self.rotate_ur5_ros(clean_angle,shake_vel,1,True)
            time.sleep(clean_wait_time)
            self.rotate_ur5_ros(-2*clean_angle,shake_vel,1,True)
            time.sleep(clean_wait_time)
            self.rotate_ur5_ros(clean_angle,shake_vel,1,True)
            time.sleep(clean_wait_time)
    
    def force_control_intrusion(self,force_threshold):
        rospy.loginfo("Prepare for force intrusion")
        max_read = 100
        z_force = 0
        for ii in range(0,1000):
            z_force+=self._ati_force.fz
        z_force_bias = z_force/1000
        z_force_onestep = 0
        while abs(z_force_onestep)<force_threshold:
            z_force_reading=0
            self.movel_ur5_ros(numpy.array((0,0,-1))*0.001,0.001,0.001,True)
            for ii in range(0,max_read):
                z_force_reading+=(self._ati_force.fz-z_force_bias)
                time.sleep(0.01)
            z_force_onestep = z_force_reading/max_read
        print("Force control intrusion finished, force reading is: {}N".format(z_force_onestep))
            
            
            
if __name__ == "__main__":
    rospy.init_node('ur5_control_node', anonymous=False)
    ur5 = ur5_command_publisher()
    
    print("Test readings")
    print(ur5._position)
    time.sleep(1)
    print(ur5._joint.joint_angles)
    print(numpy.rad2deg(ur5._joint.joint_angles))
    time.sleep(1)
    print(ur5._ati_force)
    print("Test readings finished")
    a
#    prepare_pose_0319 = [0.0815650150179863, -1.5978644529925745, 1.9941048622131348, -1.9665778318988245, -1.571324650441305, 0.8671167492866516]
#    exp_pose_0319 = [0.081541046500206, -1.5899680296527308, 2.0079269409179688, -1.9884231726275843, -1.5713723341571253, 0.8671886324882507]
#    clean_pose_0319 = [0.08128900080919266, -1.6698091665851038, 1.6587028503417969, -1.5593016783343714, -1.5711091200457972, 0.866301417350769]

    prepare_pose_0319 = [0.07304871827363968, -1.5784171263324183, 1.9971623420715332, -1.9821565786944788, -1.5836175123797815, 0.8728137612342834]
    exp_pose_0319 = [0.07313298434019089, -1.5455978552447718, 2.050570011138916, -2.072040859852926, -1.5837252775775355, 0.8732691407203674]
    clean_pose_0319 = [0.07308504730463028, -1.651834789906637, 1.7938828468322754, -1.70927602449526, -1.5834015051471155, 0.8724178671836853]
 

    ur5.movej_ur5_ros(prepare_pose_0319,0.05,1,True)  
#    ur5.shake_a_clean()
    
    x_deg = 15
    y_deg = 10
    z_deg = 10
    slip_dist = 0.05
    
    moving_vector_left = numpy.array((1,1,0))*math.sqrt(2)/2
    moving_vector_right = -numpy.array((1,1,0))*math.sqrt(2)/2
    moving_vector_forward = numpy.array((1,-1,0))*math.sqrt(2)/2
    moving_vector_backward = numpy.array((-1,1,0))*math.sqrt(2)/2
    moving_vector_up = numpy.array((0,0,1))
    moving_vector_down = numpy.array((0,0,-1))


    exp_x_angle  = numpy.array([pi/180*x_deg,0,0])
    exp_y_angle  = numpy.array([0,pi/180*y_deg,0])
    exp_z_angle  = numpy.array([0,0,pi/180*z_deg])

#    prepare_pos_0 = [-1.3850138823138636, -1.2373269240008753, 1.4040675163269043, -1.7126200834857386, -1.5615842978106897, 5.763495445251465]
#    clean_pos = [-1.3849895636187952, -1.2105634848224085, 1.4980859756469727, -1.8333409468280237, -1.561728302632467, 5.7637715339660645]
    
#    clean_pose_0120  = [-1.4038532415973108, -1.3078416029559534, 1.34041166305542, -1.56696063676943, -1.5534375349627894, 5.745469570159912]
#    prepare_pos_0120 = [-1.4036372343646448, -1.2501691023456019, 1.5993051528930664, -1.883542839680807, -1.5535810629474085, 5.7462968826293945]
#    exp_pose_0120    = [-1.4013569990741175, -1.276153866444723, 1.3395256996154785, -1.576130215321676, -1.5624707380877894, 5.747891902923584]
#    ur5.movej_ur5_ros(prepare_pos_0120,0.05,1,True)  
#   
##    ur5.movej_ur5_ros(prepare_pos_0120,0.05,1,True)  
##    ur5.movej_ur5_ros(prepare_pos_0,0.05,1,True)    
##    ur5.movej_ur5_ros(clean_pos,0.05,1,True)
##    ur5.movel_ur5_ros(moving_vector_down*0.04,0.01,1,True)
##
##    ur5.force_control_intrusion(1)
#    ur5.rotate_ur5_ros(-exp_x_angle,0.03,acc=1,wait=True)
#    ur5.rotate_ur5_ros(exp_y_angle,0.03,acc=1,wait=True)
#    ur5.rotate_ur5_ros(exp_z_angle,0.03,acc=1,wait=True)
#    
#    ur5.movel_ur5_ros(moving_vector_backward*slip_dist,0.01,1,True)
#    time.sleep(10)
#    ur5.movel_ur5_ros(moving_vector_forward*slip_dist,0.01,1,True)
##    
#    ur5.rotate_ur5_ros(exp_z_angle*-1,0.03,acc=1,wait=True)
#    ur5.rotate_ur5_ros(exp_y_angle*-1,0.03,acc=1,wait=True)
#    ur5.rotate_ur5_ros(exp_x_angle*-1,0.03,acc=1,wait=True)
#    
#    ur5.movel_ur5_ros(moving_vector_up*0.03,0.01,1,True)
#    ur5.movej_ur5_ros(clean_pos,0.05,1,True)
#    ur5.shake_a_clean()
#    ur5.movej_ur5_ros(prepare_pos_0,0.05,1,True)    
    
#
#    ur5.shake_a_clean()