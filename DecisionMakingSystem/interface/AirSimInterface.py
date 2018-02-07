'''
Created on Feb 6, 2018

@author: Owner
this class inherits from the EnvironmentConnection abstract class, and it plays the role of an interface between airsim environments and the car agent
'''
from ConnectionModule import EnvironmentInterface

from PythonClient import AirSimClient
from PythonClient.AirSimClient import *
import cv2
from PIL import Image

class AirSimConnection(EnvironmentInterface):
    
    client = CarClient()
    car_controls = CarControls()
    
    def connectToEnvironment(self):
        self.client.confirmConnection()
        self.enableApi(True)
        
    def getSensoryData(self):
        rawImage = self.client.simGetImage(1, AirSimImageType.Scene)
 
        png = cv2.imdecode(AirSimClientBase.stringToUint8Array(rawImage), cv2.IMREAD_UNCHANGED)
        return Image.fromarray(png)
    #this methods takes a float and sets it to the throttle of the simulated car in the simulation environment
    def setThrottle(self,value):
        self.car_controls.throttle=value
        self.client.setCarControls(self.car_controls)
    #this method takes a float and sets it to the steering angle of the simulated car in the simulation environment
    
    def setSteeringAngle(self,value):
        self.car_controls.steering=value
        self.client.setCarControls(self.car_controls)
    #this methods takes a float and sets it to the break of the simulated car in the simulation environment
    
    def setBreak(self,value):
        self.car_controls.brake=value
        self.client.setCarControls(self.car_controls)
    def recordImages(self,fileName,i):
        self.getSensoryData().save(fileName+str(i)+".png")
    def enableApi(self,value):
        self.client.enableApiControl(value)


    
