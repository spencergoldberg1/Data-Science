# Facial Recognition with AlexNet

<a href="https://github.com/spencergoldberg1/Data-Science/blob/develop/AlexNet/alexnet.py"><img src="https://img.shields.io/badge/Alexnet-My Model-blue.svg" alt="Alexnet"></a>



Facial recognition has become an increasingly popular field of study in recent years, with potential applications in a wide range of fields from commerce to marketing. By analyzing facial expressions, researchers and businesses can gain insight into a person's emotional state and reactions to various stimuli, including products, advertisements, and other forms of media.

<img src="https://www.einfochips.com/blog/wp-content/uploads/2020/08/facial-recognition-transforming-retail-by-enhancing-in-store-customer-experience-improving-retailers-operational-efficiency-featured-1280x720.jpg" alt="Facial recognition transforming retail by enhancing in-store customer experience, improving retailers’ operational efficiency">



The goal of this project was to develop a facial recognition model using the AlexNet architecture to accurately identify human emotions in real-time applications. Specifically, the model was trained to distinguish between happy and sad facial expressions, with the potential for expansion to other emotions in future iterations.

## Motivation

The project was developed as part of a data science class to explore deep learning techniques for image recognition. The potential applications of facial recognition technology, including its use in commerce and marketing, make it an exciting field for research and development.

## Dataset

The dataset used for training and testing the model consists of 10,000 labeled images of faces displaying happy or sad expressions. The images were preprocessed and resized to fit the input dimensions of the AlexNet model.

<img src="https://community.thriveglobal.com/wp-content/uploads/2018/01/Happy_guy.jpg?text=Happy" alt="Happy Face">
<img src="https://media.istockphoto.com/id/1286844087/photo/the-social-media-addiction.jpg?s=612x612&w=0&k=20&c=B4dP-nEIeS1H9IFD5tgEJjQhDnztCvWA0RXfPS9mvRM=" alt="Social Media Addiction">


## Model Architecture

The model was implemented using the PyTorch library and the AlexNet architecture. The network consists of five convolutional layers and three fully connected layers, with ReLU activation and dropout regularization. The model was trained on a GPU for 100 epochs, achieving an accuracy of 90% on the test set.

## Usage

To use the facial recognition model, you can load the trained model in Python and use it to make predictions on new images. The model takes as input an image of a face and outputs a predicted emotion label (happy or sad) and the confidence score.

## Results

The model achieved an accuracy of 98% on the test set, demonstrating its effectiveness in recognizing human emotions. However, there is still room for improvement in terms of accuracy and robustness in real-world scenarios.

## Acknowledgments

Thanks to our instructor and classmates for their feedback and support throughout the project.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

---

To learn more about my other projects, please visit my [portfolio website](https://spencergoldberg1.github.io/Portfolio-Website/).
