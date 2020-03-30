#include "ros/ros.h"
#include "std_msgs/String.h"
#include "jr3/jr3_force.h"
#include "read_jr3.h"
#include <string.h>

#include <sstream>

/**
 * This tutorial demonstrates simple sending of messages over the ROS system.
 */
int main(int argc, char **argv)
{
//  ASDF
  init();
  /**
   * The ros::init() function needs to see argc and argv so that it can perform
   * any ROS arguments and name remapping that were provided at the command line. For programmatic
   * remappings you can use a different version of init() which takes remappings
   * directly, but for most command-line programs, passing argc and argv is the easiest
   * way to do it.  The third argument to init() is the name of the node.
   *
   * You must call one of the versions of ros::init() before using any other
   * part of the ROS system.
   */
  ros::init(argc, argv, "jr3_node");

  /**
   * NodeHandle is the main access point to communications with the ROS system.
   * The first NodeHandle constructed will fully initialize this node, and the last
   * NodeHandle destructed will close down the node.
   */
  ros::NodeHandle n;

  /**
   * The advertise() function is how you tell ROS that you want to
   * publish on a given topic name. This invokes a call to the ROS
   * master node, which keeps a registry of who is publishing and who
   * is subscribing. After this advertise() call is made, the master
   * node will notify anyone who is trying to subscribe to this topic name,
   * and they will in turn negotiate a peer-to-peer connection with this
   * node.  advertise() returns a Publisher object which allows you to
   * publish messages on that topic through a call to publish().  Once
   * all copies of the returned Publisher object are destroyed, the topic
   * will be automatically unadvertised.
   *
   * The second parameter to advertise() is the size of the message queue
   * used for publishing messages.  If messages are published more quickly
   * than we can send them, the number here specifies how many messages to
   * buffer up before throwing some away.
   */
  ros::Publisher jr3_force_pub = n.advertise<jr3::jr3_force>("jr3_force", 1000);

  ros::Rate loop_rate(10);

  /**
   * A count of how many messages we have sent. This is used to create
   * a unique string for each message.
   */
  int count = 0;
  float values[DATA_LEN];
  while (ros::ok())
  {
    /**
     * This is a message object. You stuff it with data, and then publish it.
     */
    jr3::jr3_force msg;
    read_global(values);

    int ii;
    for (ii=0;ii<NUM_AXES;ii++)
    {
      msg.loadcell1.force[ii]=values[ii+OFFSET_S1+OFFSET_FORCE];
      msg.loadcell1.moment[ii]=values[ii+OFFSET_S1+OFFSET_MOMENT];
      msg.loadcell1.safe[ii]=values[ii+OFFSET_S1+OFFSET_SAFE];
      msg.loadcell2.force[ii]=values[ii+OFFSET_S2+OFFSET_FORCE];
      msg.loadcell2.moment[ii]=values[ii+OFFSET_S2+OFFSET_MOMENT];
      msg.loadcell2.safe[ii]=values[ii+OFFSET_S2+OFFSET_SAFE];
//      printf("%+4.3f ", values[ii]); 
    }
//    printf("\n");
    
    ROS_INFO("%+04.2f %+04.2f %+04.2f %+04.2f %+04.2f %+04.2f %+04.2f %+04.2f %+04.2f", msg.loadcell1.force[0],msg.loadcell1.force[1],msg.loadcell1.force[2],msg.loadcell1.moment[0],msg.loadcell1.moment[1],msg.loadcell1.moment[2],msg.loadcell1.safe[0],msg.loadcell1.safe[1],msg.loadcell1.safe[2]);
    ROS_INFO("%+04.2f %+04.2f %+04.2f %+04.2f %+04.2f %+04.2f %+04.2f %+04.2f %+04.2f", msg.loadcell2.force[0],msg.loadcell2.force[1],msg.loadcell2.force[2],msg.loadcell2.moment[0],msg.loadcell2.moment[1],msg.loadcell2.moment[2],msg.loadcell2.safe[0],msg.loadcell2.safe[1],msg.loadcell2.safe[2]);

    /**
     * The publish() function is how you send messages. The parameter
     * is the message object. The type of this object must agree with the type
     * given as a template parameter to the advertise<>() call, as was done
     * in the constructor above.
     */
    jr3_force_pub.publish(msg);

    ros::spinOnce();

    loop_rate.sleep();
    ++count;
  }


  return 0;
}
