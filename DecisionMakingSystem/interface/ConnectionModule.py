'''
Created on Feb 6, 2018

@author: Ibrahim Ali Fawaz

the intent of this class is to define a set of methods that are going to be used by the car agent (Decision Making Agent)
'''
from abc import ABC, abstractmethod
import csv
from PIL import Image
import utils.KeybordListener as listen
import threading

class EnvironmentInterface(ABC):
    i=0
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
    #this method records from the environment images while the user is driving the car manually in the environment
    
   
    def recordImages(self,image,fileName,csvFileName=None):
        if(self.i==0):
            
            threading.Thread(target = listen.thread1).start()
        image.save(fileName+str(self.i)+".png")
        if(csvFileName !=None):
            with open(csvFileName, 'a', newline='') as csvfile:
                fieldnames = ['image_name', 'Action']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

     
                writer.writerow({'image_name':'img'+str(self.i)+'.png', 'Action': str(listen.getSteering())})
        csvfile.close()
        self.i=self.i+1

    
    