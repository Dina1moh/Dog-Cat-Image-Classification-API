# Arabic Handwritten Characters Recognition API

Welcome to the Arabic Handwritten Characters Recognition API! This API allows you to classify Arabic handwritten characters into one of the 28 Arabic alphabet classes. It uses a TensorFlow model trained on grayscale images of handwritten characters.

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

- Predicts Arabic handwritten characters from grayscale image files.
- Returns the predicted class, name, and confidence percentage.
- Includes API key authentication for secure usage.
- Fully asynchronous FastAPI-based backend.
- CORS middleware for cross-origin requests.

---

## Requirements

- Python 3.8+
- pip (Python package manager)
- TensorFlow >= 2.x
- FastAPI
- Pydantic
- PIL (Pillow)
- Python-dotenv
- NumPy

---

## Setup

1. **Clone the repository:**
    ```bash
    git clone <repository-url>
    cd <repository-folder>
    ```

2. **Create a virtual environment:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3. **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4. **Set up environment variables:**
    - Create a `.env` file in the root directory and add the following variables:
        ```env
        APP_NAME=Hand_Written_Recognation
        VERSION=1.0.0
        API_SECRET_KEY=your-secret-key
        ```

5. **Run the API:**
    ```bash
    uvicorn main:app --reload
    ```

6. **Access the API documentation:**
    - Navigate to `http://127.0.0.1:8000/docs` for the interactive Swagger UI.

---

## API Endpoints

### 1. **Home**
   **URL:** `/`
   **Method:** `GET`
   **Headers:**
   - `X-API-KEY`: API key for authentication.

   **Response:**
   ```json
   {
       "message": "Welcome to the Arabic Handwritten Characters API!"
   }
   ```

### 2. **Prediction**
   **URL:** `/prediction`
   **Method:** `POST`
   **Headers:**
   - `X-API-KEY`: API key for authentication.

   **Body:**
   - `file`: Upload an image file containing a handwritten Arabic character.

   **Response:**
   ```json
   {
       "class_index": 0,
       "class_name": "أ",
       "confidence": 98.76
   }
   ```

---

## Example Request

### Using cURL:

```bash
curl -X POST "http://127.0.0.1:8000/prediction" \
     -H "X-API-KEY: your-secret-key" \
     -H "Content-Type: multipart/form-data" \
     -F "file=@path/to/image.png"
```

### Using Python:

```python
import requests

url = "http://127.0.0.1:8000/prediction"
headers = {
    "X-API-KEY": "your-secret-key"
}
files = {
    "file": open("path/to/image.png", "rb")
}

response = requests.post(url, headers=headers, files=files)
print(response.json())
```

---

## Environment Variables

The following environment variables are required:

| Variable         | Description                                   |
|------------------|-----------------------------------------------|
| `APP_NAME`       | Name of the application                      |
| `VERSION`        | Version of the application                   |
| `API_SECRET_KEY` | Secret key for authenticating API requests   |

---

## Folder Structure

```
.
├── src
│   ├── utils
│   │   ├── config.py          # Configuration for the app
│   │   ├── models.py          # Pydantic models
│   ├── inference.py           # Inference logic for predictions
├── main.py                    # Main FastAPI application
├── artifacts
│   └── handwriting_recognition_model.keras  # Trained model
├── requirements.txt           # Dependencies list
├── .env                       # Environment variables
```

---

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

