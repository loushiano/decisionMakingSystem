'''
Created on Jan 9, 2018

@author: Ibrahim Ali Fawaz
this class listens to keyboard entries from the user.
'''
from pynput import keyboard
import time

def on_press(key):
    
    if key==keyboard.Key.left:
        setsteering(-1)
    if key==keyboard.Key.right:
        setsteering(1)

def on_release(key):
    
    if key==keyboard.Key.left:
        setsteering(0)
    if key==keyboard.Key.right:
        setsteering(0)
    if key == keyboard.Key.esc:
        # Stop listener
        return False
    

# Collect events until released
def thread1():
        global steeringAngle
        steeringAngle=0
        with keyboard.Listener(
            on_press=on_press,
            on_release=on_release) as listener:
            listener.join()
        time.sleep(1)
        
def getSteering():
    global steeringAngle
    return steeringAngle
def setsteering(st):
    global steeringAngle
    steeringAngle=st


    
