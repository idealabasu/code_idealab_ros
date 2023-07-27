# Universal_robot_lite package quick statrt

This a lite UR robot controller built upon ROS and really for test some thing quickly.
Main function:
1. Publish joint angle and end-effector pose through topics when robot is connnected
2. using a main function method, define a ur5 class, so that I can control the robot to move while publising the command 
3. include the cord vector in idealab, ur5-cb is installed with a 45 deg offset in z at our lab. UR5e is aligned with the testbed

# Q and A:
## use them outside ROS
### question
I can find ``universal_robots_lite/joint``, using rosmsg list,but still can not find them. How can I import these msg 
using python directly instead a rosrun?
### answer
When using ROS messages in a Python script, the script should be executed in a ROS environment because the import statements rely on the ROS_PACKAGE_PATH environment variable to locate the message files.

However, if you want to import and use ROS message types in a Python script that's run outside of the ROS environment, you'll need to manually set the PYTHONPATH environment variable to include the directory where the Python modules for your messages are generated.

For instance, if you're using a catkin workspace located at ~/catkin_ws, you could add the following line to your shell profile file (e.g., ~/.bashrc for bash or ~/.zshrc for zsh):

```bash
export PYTHONPATH=$PYTHONPATH:~/catkin_ws/devel/lib/python2.7/dist-packages
```

Then source your shell profile file:

```bash
source ~/.bashrc  # or ~/.zshrc
```

After that, you should be able to import your ROS messages in Python scripts run outside of the ROS environment.

```python
from universal_robots_lite.msg import position
```

This is generally not the recommended approach, because it can lead to conflicts if different versions of packages or Python are used. It's usually best to run your scripts within the ROS environment using rosrun or roslaunch.

Please note that the directory path might change depending on your ROS and Python versions, workspace location, and whether you're using a devel or install workspace.