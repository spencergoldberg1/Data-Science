# Facial Recognition with AlexNet

![Facial Recognition](https://img.shields.io/badge/Facial%20Recognition-AlexNet-blue.svg)

This repository contains the code and dataset used to build a facial recognition model using AlexNet. The model is trained to recognize emotions and distinguish between happy and sad facial expressions.

## Background

Facial recognition has become increasingly popular in industries such as commerce and marketing, as it can provide insights into how people react to certain products or stimuli. It can also help companies make informed decisions about what to purchase, based on average reactions to their products.

## Motivation

The project was developed as part of a data science class to explore deep learning techniques for image recognition. The goal was to develop a model that could accurately identify human emotions in real-time applications.

## Dataset

The dataset used for training and testing the model consists of 10,000 labeled images of faces displaying happy or sad expressions. The images were preprocessed and resized to fit the input dimensions of the AlexNet model.

![Happy Face](https://via.placeholder.com/150x150.png?text=Happy) ![Sad Face](https://via.placeholder.com/150x150.png?text=Sad)

## Model Architecture

The model was implemented using the PyTorch library and the AlexNet architecture. The network consists of five convolutional layers and three fully connected layers, with ReLU activation and dropout regularization. The model was trained on a GPU for 100 epochs, achieving an accuracy of 90% on the test set.

## Usage

To use the facial recognition model, run the `alexnet.py` script. There are two actions to choose from:

1. Train model: This action trains the model using the dataset provided or a custom dataset. The user is prompted to select a data directory and specify the number of epochs to train for. The resulting model is saved to the data directory.
2. Classify image: This action loads the trained model and prompts the user to select an image to classify. The predicted emotion label (happy or sad) and confidence score are output to the console.

## Train Model

To train a model with your own dataset, follow these steps:

1. Create a new directory with the following structure:
    ```
    root/
    ├── class1/
    │   ├── img1.jpg
    │   ├── img2.jpg
    │   └── ...
    ├── class2/
    │   ├── img1.jpg
    │   ├── img2.jpg
    │   └── ...
    └── ...
    ```
    where `root/` is the root directory, `class1/`, `class2/`, etc. are subdirectories containing images for each class, and `img1.jpg`, `img2.jpg`, etc. are the image files.
2. Run the `alexnet.py` script and select action 1. Enter the path to the root directory when prompted to select the data directory.
3. Specify the split percentage for the data (train/test).
4. Specify the number of epochs to train for.

The resulting model will be saved to the data directory.

## Classify Image

To classify a new image using the trained model, follow these steps:

1. Run the `alexnet.py` script and select action 2.
2. Select how to choose the image to classify:
    * Enter URL
    * Pick from computer
3. If entering a URL, enter the URL of the image when prompted.
4. If picking from the computer, navigate to the image file and select it.
5. The predicted emotion label (happy or sad) and confidence score
