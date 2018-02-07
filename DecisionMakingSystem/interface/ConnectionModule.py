'''
Created on Feb 6, 2018

@author: Ibrahim Ali Fawaz

the intent of this class is to define a set of methods that are going to be used by the car agent (Decision Making Agent)
'''
from abc import ABC, abstractmethod

class EnvironmentInterface(ABC):
    
    #this method is called to connect to the simulation environment
    @abstractmethod
    def connectToEnvironment(self):
        pass
    
    #this method should return the sensoryData from the simulation environment
    @abstractmethod
    def getSensoryData(self):
        pass
    #this methods takes a float and sets it to the throttle of the simulated car in the simulation environment
    @abstractmethod
    def setThrottle(self,value):
        pass
    #this method takes a float and sets it to the steering angle of the simulated car in the simulation environment
    @abstractmethod
    def setSteeringAngle(self,value):
        pass
    #this methods takes a float and sets it to the break of the simulated car in the simulation environment
    @abstractmethod
    def setBreak(self,value):
        pass
    
    

    
    