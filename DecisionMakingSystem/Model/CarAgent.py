'''
Created on Feb 6, 2018

@author: Ibraim ali fawaz
this is the car Agent Class the makes decision on inputs that it receives when the simulated car is being controlled in a simulation environment
'''
import interface.AirSimInterface as environment
from PIL import Image
class CarAgent():
    simEnv= environment.AirSimConnection()
    
    def driveAI(self):
        while(True):
            self.doSomething(self.simEnv.getSensoryData())
    
    
    def doSomething(self,image):
        return
            
    def recordFromEnvironment(self,image,fileName,csvFileName=None):
        self.simEnv.recordImages(image, fileName, csvFileName)
