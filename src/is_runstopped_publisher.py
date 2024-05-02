#!/usr/bin/env python

import rospy
from std_msgs.msg import Bool

def publish_status():
    # Initialize ROS node
    rospy.init_node('status_publisher', anonymous=True)
    
    # Create publisher for 'is_runstopped' topic
    pub_runstopped = rospy.Publisher('is_runstopped', Bool, queue_size=10)

    # Create publisher for 'is_homed' topic
    pub_homed = rospy.Publisher('is_homed', Bool, queue_size=10)

    # Set the publishing frequency (in Hz)
    rate = rospy.Rate(1)  # 0.1 Hz => every 10 seconds
    
    while not rospy.is_shutdown():
        # Create a new Bool message
        msg_runstopped = Bool()
        msg_runstopped.data = False  # Set the value to False
        
        # Publish the message to 'is_runstopped'
        pub_runstopped.publish(msg_runstopped)
        
        # Log the publishing
        rospy.loginfo("Published to is_runstopped topic: False")
        
        # Create a new Bool message
        msg_homed = Bool()
        msg_homed.data = True  # Set the value to True
        
        # Publish the message to 'is_homed'
        pub_homed.publish(msg_homed)
        
        # Log the publishing
        rospy.loginfo("Published to is_homed topic: True")
        
        # Wait until next publish cycle
        rate.sleep()

if __name__ == '__main__':
    try:
        publish_status()
    except rospy.ROSInterruptException:
        pass
