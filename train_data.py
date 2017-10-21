import numpy as np
from alexnet import alexnet
import os

training_data_name = 'balanced_training_data.npy'

WIDTH = 40
HEIGHT = 60
LR = 1e-3
EPOCHS = 10

MODEL_NAME = 'CNN-Play-Race-{}-{}-{}.model'.format(LR,'alexnetv3',EPOCHS)
model = alexnet(WIDTH, HEIGHT, LR)

train_data = np.load(training_data_name)

X = np.array([i[0] for i in train_data]).reshape(-1,WIDTH,HEIGHT,1)
Y = [i[1] for i in train_data]

model.fit({'input': X}, {'targets': Y}, n_epoch=EPOCHS, snapshot_step=500, show_metric=True, run_id=MODEL_NAME)
model.save(MODEL_NAME)

