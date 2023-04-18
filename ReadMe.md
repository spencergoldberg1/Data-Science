![FaceSence](FaceSense.png)

# FaceSense - Facial Recognition with AlexNet

Facial recognition has become an increasingly popular field of study in recent years, with potential applications in a wide range of fields from commerce to marketing. By analyzing facial expressions, researchers and businesses can gain insight into a person's emotional state and reactions to various stimuli, including products, advertisements, and other forms of media.

## Motivation

The motivation for this project was to explore the potential of deep learning techniques for image recognition, specifically in the field of facial recognition. The ability to accurately identify human emotions in real-time applications has numerous potential applications, including in commerce and marketing.

## Dataset

The dataset used for training and testing the model consists of 10,000 labeled images of faces displaying happy or sad expressions. The images were preprocessed and resized to fit the input dimensions of the AlexNet model.

<div style="display:flex; justify-content:center; align-items:center; padding: 50px;">
  <img src="https://community.thriveglobal.com/wp-content/uploads/2018/01/Happy_guy.jpg?text=Happy" alt="Happy Face" width="300" height="300" style="padding: 0px 20px;">
  <img src="https://media.istockphoto.com/id/1286844087/photo/the-social-media-addiction.jpg?s=612x612&w=0&k=20&c=B4dP-nEIeS1H9IFD5tgEJjQhDnztCvWA0RXfPS9mvRM=" alt="Social Media Addiction" width="300" height="300" style="padding: 0px 20px;">
   <img src="https://media.istockphoto.com/id/1286844087/photo/the-social-media-addiction.jpg?s=612x612&w=0&k=20&c=B4dP-nEIeS1H9IFD5tgEJjQhDnztCvWA0RXfPS9mvRM=" alt="Social Media Addiction" width="300" height="300" style="padding: 0px 20px;">
</div>

## Model Architecture

The model was implemented using the PyTorch library and the AlexNet architecture, which has been shown to be effective in image classification tasks. The network consists of five convolutional layers and three fully connected layers, with ReLU activation and dropout regularization to prevent overfitting. The model was trained on a GPU for 100 epochs, achieving an accuracy of 98% on the test set.

## Applications in Real-World Scenarios

Facial recognition technology has numerous potential applications in real-world scenarios, particularly in commerce and marketing. By analyzing facial expressions, businesses can gain insight into customer reactions to various stimuli, such as products, advertisements, and in-store experiences. This can help businesses tailor their marketing and sales strategies to better meet the needs and preferences of their customers.

For example, facial recognition technology can be used to identify customers' emotions and tailor product recommendations based on their mood. If a customer appears sad, for example, the system could recommend products that are designed to improve mood or offer a discount on an item to lift their spirits. Similarly, if a customer appears happy, the system could recommend complementary products or offer a promotion to encourage them to make additional purchases.

## Usage

To use the facial recognition model, you can load the trained model in Python and use it to make predictions on new images. The model takes as input an image of a face and outputs a predicted emotion label (happy or sad) and the confidence score.

## Results and Future Work

The model achieved an accuracy of 98% on the test set, demonstrating its effectiveness in recognizing human emotions. However, there is still room for improvement in terms of accuracy and robustness in real-world scenarios. Future work could involve expanding the dataset to include additional emotions, refining the model architecture to improve accuracy, and testing the model in real-world
