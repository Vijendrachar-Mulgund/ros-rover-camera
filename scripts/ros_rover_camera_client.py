#! /usr/bin/env python3

import rospy
import cv2 as cv
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
from rover_camera.srv import RoverCamera

ACCEPTABLE_ANGLES = [-30, -15, 0, 15, 30]

def initRoverCameraClient():

    rospy.init_node("rover_camera_client_node")
    serviceProxy = rospy.ServiceProxy("rover_camera", RoverCamera)

    userInput = input(f"\nPlease enter an angle value from the options {str(ACCEPTABLE_ANGLES)}: ")

    if(int(userInput) not in ACCEPTABLE_ANGLES):
        print("Invalid input")
        return None
    
    res = serviceProxy(int(userInput))

    bridge = CvBridge()
    try:
        responseImage = bridge.imgmsg_to_cv2(res.image, desired_encoding="bgr8")
        cv.imshow("Received Image", responseImage)
        cv.waitKey(0)
        cv.destroyAllWindows()
    except CvBridgeError as e:
        rospy.logerr(e)
        return None

if __name__ == "__main__":
    try:
        initRoverCameraClient()
    except: 
        pass