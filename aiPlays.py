from alexnet import alexnet
from directkeys import PressKey,ReleaseKey, W, A, S, D
import numpy as np
import image, time
from PIL import ImageGrab
import cv2 
from getkeys import key_check
import os

def left():
    PressKey(A)
    ReleaseKey(D)
    print('A')
        
def right():
    PressKey(D)
    ReleaseKey(A)
    print('D')

def no_keys():
    ReleaseKey(A)
    ReleaseKey(D)


WIDTH = 40
HEIGHT = 60
LR = 1e-3
EPOCHS = 10
MODEL_NAME = 'CNN-Play-Race-{}-{}-{}.model'.format(LR,'alexnetv3',EPOCHS)
model = alexnet(WIDTH, HEIGHT, LR)

model.load(MODEL_NAME)

def main():
    paused = False
    while(True):
        if not paused:
            screen =  np.array(ImageGrab.grab(bbox=(0,40,400,600)))
            screen = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)
            screen = cv2.resize(screen,(40,60))

            prediction = model.predict([screen.reshape(WIDTH,HEIGHT,1)])[0]
            moves = list(np.around(prediction))

            if moves == [1,0,0]:
                left()
            elif moves == [0,1,0]:
                right()
            elif moves == [0,0,1]:
                no_keys()
         
        keys = key_check()

        if 'P' in keys:
            if paused:
                paused = False
                print('resuming...')
                time.sleep(1)
            else:
                paused = True
                print('paused...')
                ReleaseKey(A) 
                ReleaseKey(D)
                time.sleep(1)
                
 
main()



    
