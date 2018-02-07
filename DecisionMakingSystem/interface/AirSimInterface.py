'''
Created on Feb 6, 2018

@author: Owner
this class inherits from the EnvironmentConnection abstract class, and it plays the role of an interface between airsim environments and the car agent
'''
from ConnectionModule import EnvironmentInterface

class AirSimConnection(EnvironmentInterface):
    
    
    def connectToEnvironment(self):
        print('ayre')
        
    def getSensoryData(self):
        pass
    #this methods takes a float and sets it to the throttle of the simulated car in the simulation environment
    def setThrottle(self,value):
        pass
    #this method takes a float and sets it to the steering angle of the simulated car in the simulation environment
    
    def setSteeringAngle(self,value):
        pass
    #this methods takes a float and sets it to the break of the simulated car in the simulation environment
    
    def setBreak(self,value):
        pass

x= AirSimConnection()
y=x.connectToEnvironment()
    
