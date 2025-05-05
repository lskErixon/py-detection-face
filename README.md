# py-detection-face
## ℹ️ About the Project

This application is a simple **face recognition tool** that compares two images and determines whether they contain the **same person**. It uses the `face_recognition` library (based on dlib) to encode facial features and match them.

The interface is designed to be user-friendly with graphical buttons for selecting images and displaying results in popup windows. It’s a great starting point for learning how facial recognition works in Python.

---

## 🎯 Purpose

This project was created to:

- Demonstrate basic face recognition using Python.
- Provide a simple desktop interface for comparing faces.
- Help beginners learn how to work with image processing and machine learning libraries like `face_recognition` and `tkinter`.

---

## 🚀 Possible Future Improvements

This simple prototype can evolve into more advanced applications. Here are a few development ideas:

### 1. Real-time face recognition via webcam  
Integrate OpenCV to capture live video and compare faces in real-time.

### 2. Show face detection on image  
Display rectangles around detected faces in both images as visual feedback.

### 3. Face database  
Allow users to save known faces and match new images against a stored database of people.

### 4. Security system  
Use face recognition as a login method or smart door unlock system.

### 5. Web version  
Convert the program into a web app using Flask, FastAPI or Django for remote access.

### 6. Mobile support  
Create a mobile app using Flutter or React Native that uses on-device face comparison.

### 7. Multiple face handling  
Support images with multiple faces, and identify which ones match across photos.

---

This project is a functional base for learning, experimentation, or building something more advanced.

# Face Recognition App – Setup Instructions

This guide explains how to set up and run the face recognition application in a Python virtual environment.

## 1. Navigate to your project folder

Open your terminal and run:

```bash
cd /path/to/your/project
2. Create a virtual environment
Run the following command to create a new virtual environment named venv:

bash
python3 -m venv venv
3. Activate the virtual environment

On macOS / Linux:
source venv/bin/activate

On Windows:
venv\Scripts\activate

4. Install the dependencies
Use pip to install all dependencies listed in requirements.txt:

pip install -r requirements.txt

