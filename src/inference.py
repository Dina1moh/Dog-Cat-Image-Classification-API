from src.utils.config import MODEL, classes
from PIL import Image
import numpy as np
from io import BytesIO
def Predict(image):
    """
    Predict the class of the image using the pre-trained model.

    Args:
        image (numpy.ndarray): The input image to classify.

    Returns:
        dict: A dictionary containing the predicted class and confidence score.
    """
    img = Image.open(BytesIO(image)).convert("RGB")
    img = img.resize((150,150))
    img = np.array(img) 
    img =img.astype("float32") / 255.0
    img = np.expand_dims(img, axis=0) 
    prediction = MODEL.predict(img)
    
    if prediction[0][0] > 0.5 :
        class_index = 1
        class_name = classes[1]
    else:
        class_index = 0
        class_name = classes[0]
    confidence = prediction[0][0] if class_index == 1 else 1 - prediction[0][0]
    return {
        "class_index": class_index,
        "class_name": class_name,
        "confidence": float(confidence) 
    }
      