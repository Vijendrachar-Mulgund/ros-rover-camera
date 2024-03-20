#! /usr/bin/env python3

import rospy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
import cv2 as cv
from rover_camera.srv import RoverCamera, RoverCameraResponse

def encode_image(image):
    # Convert image to JPEG format
    _, encoded_image = cv.imencode('.png', image)
    return encoded_image.tostring()

def processInputData(request):
     # Process the request
    bridge = CvBridge()
    try:
        cvImage = cv.imread("../images/0.png")
        image = bridge.cv2_to_imgmsg(cvImage, encoding="bgr8")
    except CvBridgeError as e:
        rospy.logerr(e)
        return None
    # Perform some operations on the image if needed
    # Then encode the image
    # encoded_image = encode_image(image)
    
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