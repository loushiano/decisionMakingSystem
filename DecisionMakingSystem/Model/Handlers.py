'''
Created on Feb 8, 2018

@author: Ibrahim Ali Fawaz
this module has class that handle sensory data.
'''
from abc import ABC, abstractmethod
from enum import Enum
import PIL
class SensoryDataHandler(ABC):
    
    @abstractmethod
    def handleSensoryInput(self,dataInput):
        pass
    
class ImageDataHandler(SensoryDataHandler):
    
    def handleSensoryInput(self,dataInput):
        pass
    
class LidarDataHandler(SensoryDataHandler):
    
    
    def handleSensoryInput(self,dataInput):
        pass
class DistanceSensorHandler(SensoryDataHandler):
    
    def handleSensoryInput(self,dataInput):
        pass
class handlerUtil(Enum):
    PILIMAGE='PIL.Image.Image'
    
    def describe(self):
        print('tize')