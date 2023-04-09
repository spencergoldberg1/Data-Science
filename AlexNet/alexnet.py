import os
import requests
from io import BytesIO
from tkinter import Tk, filedialog
from tqdm import tqdm

import torch
import torch.nn as nn
import torch.optim as optim
import torchvision.models as models
import torchvision.datasets as datasets
import torchvision.transforms as transforms
from PIL import Image


# Define the data transformation pipeline
transform = transforms.Compose([
    transforms.Resize(256),
    transforms.CenterCrop(224),
    transforms.RandomHorizontalFlip(),
    transforms.ToTensor(),
    transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
])
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
# Prompt the user to select the data directory
Tk().withdraw()
data_dir = filedialog.askdirectory(title="Select the data directory")
model_path = os.path.join(data_dir, "alexnet_custom_model.pt")

def classify():
    model = torch.load(model_path)
    model.to(device)
    train_dir = os.path.join(data_dir, 'train')
    train_dataset = datasets.ImageFolder(train_dir, transform=transform)
    classify_image(model, train_dataset, device)

def load_image(image_path, url=False, transform=None):
    if url:
        response = requests.get(image_path)
        img = Image.open(BytesIO(response.content)).convert('L')
    else:
        img = Image.open(image_path).convert('L')
    img = img.convert("RGB")  # Duplicate grayscale channel to create 3-channel image
    if transform:
        img_transformed = transform(img)
    else:
        img_transformed = transforms.ToTensor()(img)
    img_batch = img_transformed.unsqueeze(0)
    if device:
        img_batch = img_batch.to(device)
    return img_batch


def classify_image(model, train_dataset, device):
    # Prompt the user to select the image to classify
    Tk().withdraw()
    image_path = filedialog.askopenfilename(title="Select the image to classify", filetypes=(("JPEG files", "*.jpg"), ("PNG files", "*.png"), ("All files", "*.*")))
    if not image_path:
        print("No image selected.")
        return

    # Load and preprocess the image
    img_batch = load_image(image_path, transform=transform)

    # Classify the image
    with torch.no_grad():
        outputs = model(img_batch)
        _, predicted = torch.max(outputs.data, 1)

    # Print the predicted class label
    # Print out the class names
    class_names = train_dataset.classes
    print("Classes found:", class_names)
    print(f"Predicted class: {class_names[predicted.item()]}")

def prepare_data(data_dir, split_ratio):
    # Split the data into train and validation sets
    train_dir = os.path.join(data_dir, 'train')
    valid_dir = os.path.join(data_dir, 'valid')
    if not os.path.exists(train_dir) or not os.path.exists(valid_dir):
        datasets.ImageFolder(data_dir, transform=transform).split_folder(split_ratio)
    return train_dir, valid_dir


def train_model(data_dir, device):
    # Load the pretrained AlexNet model
    model = models.alexnet(pretrained=True)

    # Load the custom dataset
    train_dir = os.path.join(data_dir, 'train')
    train_dataset = datasets.ImageFolder(train_dir, transform=transform)

    # Update the last fully connected layer to match the number of classes in the custom dataset
    num_classes = len(train_dataset.classes)
    model.classifier[6] = nn.Linear(model.classifier[6].in_features, num_classes)

    # Print out the class names
    class_names = train_dataset.classes
    print("Classes found:", class_names)

    # Set up the model, criterion, and optimizer
    model = model.to(device)
    criterion = nn.CrossEntropyLoss()
    optimizer = optim.SGD(model.parameters(), lr=0.001, momentum=0.9)

    # Define the file path for the saved model
    model_path = os.path.join(data_dir, "alexnet_custom_model.pt")

    # Always train a new model and overwrite the old one if it exists
    folder_setup = input("Is the folder setup with 'train' and 'valid' folders? (y/n): ")
    if folder_setup.lower() != 'y':
        split_ratio = int(input("Enter the train/valid split percentage (e.g., 80 for 80/20 split): "))
        train_dir, valid_dir = prepare_data(data_dir, split_ratio)
    else:
        valid_dir = os.path.join(data_dir, 'valid')

    # Load the validation dataset
    valid_dataset = datasets.ImageFolder(valid_dir, transform=transform)

    # Create data loaders
    print("Creating data loaders...")
    train_loader = torch.utils.data.DataLoader(train_dataset, batch_size=64, shuffle=True)
    valid_loader = torch.utils.data.DataLoader(valid_dataset, batch_size=64, shuffle=False)
    print("Data loaders created successfully!")

    # Train the model
    num_epochs = int(input("Enter the number of epochs to train: "))
    print("Training model...")
    for epoch in range(num_epochs):
        epoch_loss = 0
        correct = 0
        total = 0
        for i, (images, labels) in enumerate(tqdm(train_loader, desc=f"Epoch {epoch + 1}/{num_epochs}")):
            optimizer.zero_grad()
            images, labels = images.to(device), labels.to(device)
            outputs = model(images)
            loss = criterion(outputs, labels)
            epoch_loss += loss.item()
            loss.backward()
            optimizer.step()

            _, predicted = torch.max(outputs.data, 1)
            total += labels.size(0)
            correct += (predicted == labels).sum().item()

        epoch_loss /= len(train_loader)
        accuracy = correct / total
        print('Epoch [{}/{}], Loss: {:.4f}, Accuracy: {:.2f}%'.format(epoch + 1, num_epochs, epoch_loss,accuracy * 100))
        torch.save(model, model_path)

    print("Model saved successfully!")
print("Training complete.")

action = int(input("Select an action:\n1. Train model\n2. Classify image\nEnter action number: "))

if action == 1:
    # Train the model
    train_model(data_dir, device)
    shouldClassify = input("Do you also want to classify a new image? (y/n): ")
    if shouldClassify:
        classify()
elif action == 2:
    # Classify an image
    # Load the model
    if not os.path.exists(model_path):
        print("Model not found. Please train a model first.")
        train_model(data_dir, device)
        classify()
    else:
        classify()
else:
    print("Invalid action selected.")
