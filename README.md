# Cats vs Dogs Classification API

Welcome to the **Cats vs Dogs Classification API**! This API allows you to classify images of cats and dogs using a trained deep learning model built with TensorFlow. The backend is implemented with FastAPI and supports image upload for inference.

---

## Table of Contents

1. [Features](#features)  
2. [Requirements](#requirements)  
3. [Setup](#setup)  
4. [API Endpoints](#api-endpoints)  
5. [Example Request](#example-request)  
6. [Environment Variables](#environment-variables)  
7. [Folder Structure](#folder-structure)  
8. [License](#license)

---

## Features

- Classifies uploaded image as either a **cat** or a **dog**.  
- Returns class label and prediction confidence.  
- Built with FastAPI for asynchronous performance.  
- Supports secure API usage via secret key header.  
- Uses CORS middleware for cross-origin request handling.

---

## Requirements

- Python 3.8+  
- TensorFlow >= 2.x  
- FastAPI  
- Uvicorn  
- NumPy  
- Pandas  
- Pillow  
- Python-dotenv  
- Python-multipart

---

## Setup

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd <repository-folder>



## folders 
``` bash
├── src
│   ├── utils
│   │   ├── config.py          # Application configuration
│   │   ├── models.py          # Pydantic request/response models
│   ├── inference.py           # Prediction and preprocessing logic
├── main.py                    # Main FastAPI app entry point
├── artifacts
│   └── cat_dog_model.keras    # Trained Keras model
├── requirements.txt           # Project dependencies
├── .env                       # Environment variables
