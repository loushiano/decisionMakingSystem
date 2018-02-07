'''
Created on Feb 6, 2018

@author: Owner
this class inherits from the EnvironmentConnection abstract class, and it plays the role of an interface between airsim environments and the car agent
'''
from ConnectionModule import EnvironmentInterface

from PythonClient import AirSimClient
from PythonClient.AirSimClient import *

class AirSimConnection(EnvironmentInterface):
    
    client = CarClient()
    car_controls = CarControls()
    
    def connectToEnvironment(self):
        self.client.confirmConnection()
        self.enableApi(True)
        
    def getSensoryData(self):
        pass
    #this methods takes a float and sets it to the throttle of the simulated car in the simulation environment
    def setThrottle(self,value):
        self.car_controls.throttle=value
        self.client.setCarControls(self.car_controls)
    #this method takes a float and sets it to the steering angle of the simulated car in the simulation environment
    
    def setSteeringAngle(self,value):
        pass
    #this methods takes a float and sets it to the break of the simulated car in the simulation environment
    
    def setBreak(self,value):
        pass
    def recordImages(self,fileName):
        pass
    def enableApi(self,value):
        self.client.enableApiControl(value)

x=AirSimConnection()
x.connectToEnvironment()
x.setThrottle(1)
    
