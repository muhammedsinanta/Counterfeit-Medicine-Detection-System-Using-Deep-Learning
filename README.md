# 💊 Counterfeit Medicine Detection System Using Deep Learning

A deep learning-based image classification system that identifies medicine packaging as **Real** or **Fake** using **Convolutional Neural Networks (CNN)** and **TensorFlow/Keras**.

The trained deep learning model is integrated with a **Streamlit web application**, allowing users to upload a medicine image and receive a prediction.

---

## 📌 Project Overview

Counterfeit medicines can create serious risks for consumers and healthcare systems.

This project demonstrates how **Deep Learning and Computer Vision** can be used to classify medicine images into two categories:

- ✅ Real Medicine
- ❌ Fake Medicine

The system takes a medicine image as input, preprocesses the image, and passes it through a trained CNN model to generate the classification result.

---

## 🎯 Objectives

- Build an image classification model using CNN.
- Classify medicine images as real or fake.
- Apply image preprocessing before prediction.
- Integrate the trained model into a web application.
- Provide an easy-to-use interface for image-based predictions.

---

## 🚀 Features

- 📷 Upload medicine images
- 🖼️ Image preprocessing
- 🧠 CNN-based image classification
- 💊 Real vs Fake medicine prediction
- 🌐 Streamlit web application
- ⚡ Real-time prediction
- 🐍 Python-based implementation

---

## 🛠️ Technologies Used

### Programming Language
- Python

### Deep Learning
- TensorFlow
- Keras
- Convolutional Neural Networks (CNN)

### Data Processing
- NumPy
- Image preprocessing

### Computer Vision
- OpenCV

### Web Application
- Streamlit

### Development Tools
- Jupyter Notebook
- Visual Studio Code
- Git
- GitHub

---

## 🔄 Project Workflow

```text
Medicine Image
      ↓
Image Upload
      ↓
Image Preprocessing
      ↓
Resize to 224 × 224
      ↓
Pixel Normalization
      ↓
Trained CNN Model
      ↓
Model Prediction
      ↓
Real / Fake Medicine

---

##🧠 Deep Learning Model

The project uses a Convolutional Neural Network (CNN) for image classification.

The input image is resized to:

224 × 224 pixels

Pixel values are normalized by dividing them by:

255

This converts the pixel values into a range between approximately 0 and 1.

The trained model then generates a prediction for the uploaded medicine image.

---
.

##🌐 Streamlit Web Application

The trained model is integrated into a Streamlit application.

Users can:

Open the web application.
Upload a medicine image.
The image is resized and preprocessed.
The trained CNN model processes the image.
The application displays the predicted result.

---

##Application

Real Medicine Prediction

Fake Medicine Prediction

