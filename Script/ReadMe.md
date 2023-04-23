# Image Classification using AlexNet

This script provides a simple interface for training an image classification model using AlexNet and classifying new images using the trained model. The script assumes that the data is organized in the following format:

```
data_dir/
├── train/
│   ├── class_1/
│   │   ├── image_1.jpg
│   │   ├── image_2.jpg
│   │   ├── ...
│   ├── class_2/
│   │   ├── image_1.jpg
│   │   ├── image_2.jpg
│   │   ├── ...
│   ├── ...
├── valid/
│   ├── class_1/
│   │   ├── image_1.jpg
│   │   ├── image_2.jpg
│   │   ├── ...
│   ├── class_2/
│   │   ├── image_1.jpg
│   │   ├── image_2.jpg
│   │   ├── ...
│   ├── ...
```

Each class is represented by a directory in `train/` and `valid/`. The images for each class are stored in their respective directories. The script will split the images into training and validation sets based on the percentage split entered by the user.

## Requirements

To run this script, you will need:

1. Python 3.x
2. PyTorch
3. torchvision
4. tqdm

You can install PyTorch and torchvision using `pip`:

```sh
pip install torch torchvision
```

You can install tqdm using `pip`:

```sh
pip install tqdm
```

## How to use

### 1. Train a new model

To train a new model, follow the steps below:

1. Run the script.
2. Select action number `1` to train a new model.
3. Select the data directory containing the training images when prompted.
4. If no model exists in the data directory, enter the percentage split for the training and validation datasets.
5. Enter the number of epochs to train the model.
6. The best model will be saved in the data directory as `alexnet_custom_model.pt`.

### 2. Classify a new image

To classify a new image, follow the steps below:

1. Run the script.
2. Select action number `2` to classify a new image.
3. Select the data directory containing the training images when prompted.
4. If no model exists in the data directory, you will be prompted to train a new model.
5. Choose an image file from your computer or enter a URL to download the image.
6. The predicted class label will be displayed.

### 3. Print model stats

To print the training and validation accuracy of a trained model, follow the steps below:

1. Run the script.
2. Select action number `3` to print model stats.
3. Select the data directory containing the training images when prompted.
4. The training and validation accuracy of the trained model will be displayed.
