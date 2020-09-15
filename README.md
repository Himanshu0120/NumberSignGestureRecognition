# NumberSignGestureRecognition

This project uses OpenCv and Convolution Neural Networks to recognize the numer from the gesture of the hand shown to the camera.
The process invloved is thresholding of the image to seprate the hand from the background to create a binary image which can be sent to the pretrained 
model to recognize the number.
The model can predict number from 0-5

## How to run

* dataCollection.py-This file is collect the image data from the user to get training and testing data.The user has to first select that whether he is giving 
training or testing data and them show his hand to the camera and press the number key from 0-5 corresponding to his hand gesture.
This will save the image in the respective folder.

* Training.py-This file training the model on the data provided by the user using CNN. And the model with the best validtion accuracy is then saved so that
it can be later used for recogintion.The validation accuracy of the model is around 95


* Recognition.py- This file is to be run for recognition. The user has to show his hand to the camera and the number shown by him will be displayed on the
image screen.


### The background in the image should be white or other light colour for thresholding to work. Or else it wont seprate the hand from the background.

