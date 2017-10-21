# CNN-simple-game
In this repo, convolutional neural network learns to play a Python game with supervised learning method.

## Contents:

**game.py:** This is the main game. You can start and play by yourself. To collect training data or to test your model, you should first run this code and open the game.

**collect_train_data.py:** This file collects training input data by getting the pixel values of the game. As a training output data, keyboard activities are recorded and saved.  

**balance_data.py:** With this file, dataset is being balanced before the training.

**train_data.py:** Datasets are being trained and model is saved in this file. As a CNN model, AlexNet is used.

**aiPlays.py:** Game is being played with the CNN model that is saved.
