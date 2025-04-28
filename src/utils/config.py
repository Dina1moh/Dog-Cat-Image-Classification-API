import os
from pathlib import Path
from dotenv import load_dotenv
import tensorflow as tf

# Load environment variables
load_dotenv(override=True)

# App configuration
APP_NAME = os.getenv("APP_NAME", "CatVSDogs Classifier")  
VERSION = os.getenv("VERSION", "1.0.0") 
API_SECRET_KEY = os.getenv("API_SECRET_KEY")

if not API_SECRET_KEY:
    raise ValueError("API_SECRET_KEY environment variable is not set")

# Model configuration
MODEL_PATH = Path(__file__).parent.parent
MODEL_FILE = MODEL_PATH / "artifacts" / "model.h5"

if not MODEL_FILE.exists():
    raise FileNotFoundError(f"Model file not found at {MODEL_FILE}")

MODEL = tf.keras.models.load_model(str(MODEL_FILE))

# Class labels
classes = [
    "cat",
    "dog"
]