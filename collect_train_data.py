import numpy as np
import image, time
from PIL import ImageGrab
import cv2 
from getkeys import key_check
import os

display_width = 400
display_height = 600

def countdown(tictoc):
    print(tictoc,'seconds countdown is starting...')
    while tictoc >= 0:
            print(tictoc,'...')
            time.sleep(1)
            tictoc -= 1
    
def keys_to_output(keys):
    #[A,D,nothing]
    output = [0,0,0]

    if 'A' in keys:
        output[0]=1
    elif 'D' in keys:
        output[1]=1
    else:
        output[2]=1

    return output
        
file_name = 'training_data.npy'

if os.path.isfile(file_name):
    training_data = list(np.load(file_name))
    print('There exists training data with',len(training_data),'length. New data is concatenating.')
else:
    print('New training data is creating.')
    training_data = []

def screen_record(): 
    while(True):
        screen =  np.array(ImageGrab.grab(bbox=(0,50,display_width,display_height))) #50 px below from top to skip the title of the game
        screen = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)
        screen = cv2.resize(screen,(40,60))
        cv2.imshow('window',screen)
        if cv2.waitKey(25) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break

        keys = key_check()
        output = keys_to_output(keys)
        training_data.append([screen,output]) 
        if len(training_data) % 500 == 0:
            np.save(file_name,training_data)
            print("Data saved with length",len(training_data))
            
countdown(5)            
screen_record()
