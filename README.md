# 💊 Counterfeit Medicine Detection System Using Deep Learning

A deep learning-based image classification system that identifies medicine packaging as genuine or counterfeit using Convolutional Neural Networks (CNN) and TensorFlow/Keras.

## 📌 Project Overview

Counterfeit medicines can pose serious risks to consumers. This project uses computer vision and deep learning to classify medicine images into two categories:

- Real Medicine
- Fake Medicine

The trained CNN model is integrated into a Streamlit web application that allows users to upload a medicine image and receive a prediction.

## 🚀 Features

- Medicine image upload
- Image preprocessing
- CNN-based image classification
- Real vs Fake medicine prediction
- Streamlit web interface
- Real-time prediction

## 🛠️ Technologies Used

- Python
- TensorFlow
- Keras
- NumPy
- OpenCV
- CNN
- Computer Vision
- Streamlit
- Jupyter Notebook

## 🔄 Project Workflow

Image Upload
      ↓
Image Preprocessing
      ↓
Resize to 224 × 224
      ↓
Pixel Normalization
      ↓
CNN Model
      ↓
Prediction
      ↓
Real / Fake Medicine

## 🧠 Model

The project uses a Convolutional Neural Network (CNN) for image classification.

Input image size:

224 × 224 pixels

Pixel values are normalized to the range:

0–1

## 🌐 Streamlit Application

The trained model is integrated into a Streamlit application.

Users can upload a JPG, JPEG, or PNG medicine image and receive a classification result.

## 📂 Project Structure

```text
Counterfeit-Medicine-Detection-System/
│
├── app.py
├── medicine_model.keras
├── counterfeit_Medicine_detector.ipynb
├── requirements.txt
└── screenshots/d CNN.
