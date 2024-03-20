#! /usr/bin/env python3

import rospy
import cv2 as cv
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
from rover_camera.srv import RoverCamera, RoverCameraResponse

def processInputData(request):
    bridge = CvBridge()
    try:
        cvImage = cv.imread(f"../images/{request.angle}.png")
        image = bridge.cv2_to_imgmsg(cvImage, encoding="bgr8")
    except CvBridgeError as e:
        rospy.logerr(e)
        return None
    
    return RoverCameraResponse(image)

def initRoverCameraService():
    rospy.init_node("rover_camera_service_node")
    print("Rover service server node is running...")
    rospy.Service("rover_camera", RoverCamera, processInputData)
    rospy.spin()

if __name__ == "__main__":
    try:
        initRoverCameraService()
        pass
    except: 
        pass