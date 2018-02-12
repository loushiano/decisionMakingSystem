'''
Created on Feb 8, 2018

@author: Ibrahim Ali Fawaz
this module has class that handle sensory data.
'''
from abc import ABC, abstractmethod
from enum import Enum
import PIL
import cv2
import numpy as np
class SensoryDataHandler(ABC):
    
    @abstractmethod
    def handleSensoryInput(self,dataInput):
        pass
    
class ImageDataHandler(SensoryDataHandler):
    
    def handleSensoryInput(self,dataInput):
        dataInput=cv2.cvtColor(dataInput,cv2.COLOR_BGR2GRAY)
        dataInput=cv2.Canny(dataInput,threshold1=200,threshold2=300)
        dataInput=self.roi(dataInput)
        lines=cv2.HoughLinesP(dataInput,1,np.pi/180,180,20,15)
    
    def roi(self,img):
        processed_img =img[50:144,0:256]
    
        return processed_img
    
class LidarDataHandler(SensoryDataHandler):
    
    
    def handleSensoryInput(self,dataInput):
        pass
class DistanceSensorHandler(SensoryDataHandler):
    
    def handleSensoryInput(self,dataInput):
        pass
class handlerUtil(Enum):
    PILIMAGE=ImageDataHandler()
    
    def describe(self,dataInput):
        self.value.handleSensoryInput(dataInput)
        