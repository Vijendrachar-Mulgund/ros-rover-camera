#! /usr/bin/env python3

import rospy
from sensor_msgs.msg import Image
import cv2 as cv
from cv_bridge import CvBridge, CvBridgeError
from rover_camera.srv import RoverCamera

def initRoverCameraClient():

    rospy.init_node("rover_camera_client_node")
    srvProxy = rospy.ServiceProxy("rover_camera", RoverCamera)

    userInput = input("\nPlease Enter a value: ")

    res = srvProxy(int(userInput))

    print("The output is : ", res.image)
    
    bridge = CvBridge()
    try:
        imageRes = bridge.imgmsg_to_cv2(res.image, desired_encoding="bgr8")
        cv.imshow("Received Image", imageRes)
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