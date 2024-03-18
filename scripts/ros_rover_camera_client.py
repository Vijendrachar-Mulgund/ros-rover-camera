#! /usr/bin/env python3

import rospy

from rover_camera.srv import RoverCamera

def initRoverCameraClient():

    rospy.init_node("rover_camera_client_node")
    srvProxy = rospy.ServiceProxy("rover_camera", RoverCamera)

    userInput = input("\nPlease Enter a value: ")

    res = srvProxy(int(userInput))

    print("The output is : ", res.theImage)



if __name__ == "__main__":
    try:
        initRoverCameraClient()
    except: 
        pass