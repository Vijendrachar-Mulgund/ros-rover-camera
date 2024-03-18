#! /usr/bin/env python3

import rospy

from rover_camera.srv import RoverCamera, RoverCameraResponse

def processInputData(request):
    print("The Request is -> ", request.angle)

    return RoverCameraResponse( str( request.angle))

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