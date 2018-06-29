# CNN-simple-game
In this repo, convolutional neural network learns to play a Python game with supervised learning method.

## Contents:

**game.py:** This is the main game. You can start and play by yourself. To collect training data or to test your model, you should first run this code and open the game.

**collect_train_data.py:** This file collects training input data by getting the pixel values of the game. As a training output data, keyboard activities are recorded and saved.  

**balance_data.py:** With this file, dataset is being balanced before the training.

**train_data.py:** Datasets are being trained and model is saved in this file. As a CNN model, AlexNet is used.

**aiPlays.py:** Game is being played with the CNN model that is saved.

## Setup and Requirements:
**Required Libraries:**
Numpy
PIL 
CV2 
tflearn

With collect_train_data.py file, you should collect training data. Initially, open the game.py and move the game screen to the top left of the monitor screen. collect_train_data.py file collects the pixels data from the top left with the determined screen width and height. To stop the collecting data, simply press Ctrl+C and quit. It should save the data named as "training_data.npy". 

The more data you collect means better learning and higher scores for AI. (You should make scores.)

After collecting data, some preprocessing is required for data to prevent overfitting. Run the balance_data.py file to equate the input sample keys.  As a last step of training, run train_data.py which uses the AlexNet as a CNN model. After training, model will be created and saved. And now the AI can play the game with the created model (game must be opened and moved to the top left of the screen).

**Game Screenshot:**

![alt text](https://github.com/azadkaratas/CNN-simple-game/blob/master/images/gameImage.PNG)

