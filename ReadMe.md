# FaceSense - Facial Recognition with AlexNet
<img src="images/FaceSense.png" alt="FaceSense logo">
Facial recognition technology has numerous potential applications in real-world scenarios, particularly in commerce and marketing. The ability to accurately identify human emotions in real-time applications has significant implications, including in customer experience, healthcare, and security.

[![Video Preview](https://img.youtube.com/vi/tQvNlkWWUNg/0.jpg)](https://youtu.be/tQvNlkWWUNg)


## Motivation
The motivation for this project was to explore the potential of deep learning techniques for image recognition, specifically in the field of facial recognition. By accurately identifying human emotions, businesses and researchers can gain insight into a person's emotional state and reactions to various stimuli, including products, advertisements, and other forms of media.

## Dataset
The dataset used for training and testing the model consists of images of happy and sad faces. The classes used were taken from the dataset that can be found [here](https://www.kaggle.com/datasets/chiragsoni/ferdata), and I only used the happy and sad image data for training.

<div style="width: 100%;">
  <div style="display:flex; justify-content:center; align-items:center; padding: 50px; margin: 0 auto;">
    <img src="https://declutterthemind.com/wp-content/uploads/traitshappypeople.jpg.webp" alt="Happy Face" width="250" height="250" style="padding: 0px 20px;">
    <img src="https://health.wyo.gov/wp-content/uploads/2020/08/sad-man-sitting-in-hoodie.jpg" alt="Sad Face" width="250" height="250" style="padding: 0px 20px;">
  </div>
</div>

## Methodology
The model was implemented using the PyTorch library and the AlexNet architecture, which has been shown to be effective in image classification tasks. The network consists of five convolutional layers and three fully connected layers, with ReLU activation and dropout regularization to prevent overfitting. The model was trained on a GPU for 100 epochs, achieving an accuracy of 98% on the test set.

## Results and Discussion
The model achieved an accuracy of 92% on the validation set, demonstrating its effectiveness in recognizing human emotions. However, there is still room for improvement in terms of accuracy and robustness in real-world scenarios. Future work could involve expanding the dataset to include additional emotions, refining the model architecture to improve accuracy, and testing the model in real-world scenarios.

## Train New Model
If you are interested in training your own model on any dataset you like, follow this link [here](https://github.com/spencergoldberg1/FaceSense/blob/develop/Script), and to view the instructions on how to run the python script.

NOTE: Must be in the 'Script' directory to run the python script titled ['alexnet.py'](https://github.com/spencergoldberg1/FaceSense/blob/develop/Script/alexnet.py).

## Retail
Facial recognition technology can be used in retail to identify customers and track their behavior in stores. This can provide valuable insights into customer preferences and help businesses improve their marketing and sales strategies. For example, by analyzing customer emotions, retailers can identify which products are resonating with customers and which are not. This information can then be used to make changes to the store layout or product placement to better meet the needs and preferences of customers.

<img src="https://gigasource.b-cdn.net/wp-content/uploads/2020/03/face-recognition-in-retail-store.jpg" alt="Retail Store">

## Healthcare
Facial recognition technology can be used to monitor patients in hospitals and clinics. By analyzing facial expressions, healthcare professionals can gain insight into patient well-being and identify potential mental health concerns. For example, a patient who is displaying signs of stress or anxiety could be identified and provided with additional support or resources.

## <img src="https://indatalabs.com/wp-content/uploads/2020/07/facial-recognition-for-healthcare-disruption-1.png" alt="Healthcare">

Security
Facial recognition technology can be used in security applications to identify individuals and prevent fraud or unauthorized access. For example, facial recognition technology can be used to monitor access to high-security areas in buildings or to prevent identity theft. In airports, facial recognition technology is being used to identify potential security risks and prevent unauthorized individuals from entering restricted areas.

<img src="https://diginomica.com/sites/default/files/images/2019-11/facial-recognition-threat.jpg" alt="Security">

## Advertising
Facial recognition technology can be used in advertising to identify customer emotions and tailor advertising messages accordingly. For example, if a customer appears sad, the advertising message could be designed to improve mood or offer a discount on a product that is designed to lift spirits. Similarly, if a customer appears happy, the advertising message could be tailored to offer complementary products or to encourage additional purchases.

## <img src="https://www.noldus.com/static/images/core-blog/persuasion-advertisements-facial-expresssion-1601906960.jpg" alt="Advertising">
Overall Impact
Facial recognition technology has the potential to revolutionize a wide range of industries, from customer experience to healthcare to security. By accurately identifying emotions and reactions, businesses and organizations can better meet the needs and preferences of their customers and clients. As the technology continues to evolve and become more sophisticated, we can expect to see even more applications of facial recognition technology in the future.

# Learn More
To learn more about this project and my other work, please visit [my portfolio website](https://spencergoldberg1.github.io/Portfolio-Website/).

## Acknowledgments
Special thanks to the Kaggle community for providing the Facial Expression Recognition Dataset used in this project. Additionally, thanks to the PyTorch team for creating a powerful and easy-to-use deep learning library.

## About FaceSense
FaceSense is a project aimed at understanding people and how they interact with the world. By understanding someone's true emotion, it will help not only in making better product and advertisement recommendations based on how they are feeling but can also help marketers target their ads to the desired audience.
