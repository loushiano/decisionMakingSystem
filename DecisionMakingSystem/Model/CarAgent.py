'''
Created on Feb 6, 2018

@author: Ibraim ali fawaz
this is the car Agent Class the makes decision on inputs that it receives when the simulated car is being controlled in a simulation environment
'''
import interface.AirSimInterface as environment
from PIL import Image
import PIL
from Model.Handlers import *

class CarAgent():
    dTypeImage={PIL.Image.Image:'PILIMAGE'}
    simEnv= environment.AirSimConnection()
    imd=ImageDataHandler()
    
    
    def driveAI(self):
        handlerUtil[self.dTypeImage[PIL.Image.Image]].describe(1)
        
        self.simEnv.connectToEnvironment(False)
        img= self.simEnv.getSensoryData()
        
    
    
    
            
    def recordFromEnvironment(self,image,fileName,csvFileName=None):
        self.simEnv.recordImages(image, fileName, csvFileName)

x= CarAgent()
x.driveAI()