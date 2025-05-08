import pyautogui
import time
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np

# Load trained model
model = load_model('weed_classifier.h5')

# Image path
img_path = r'C:/Users/pes12/Downloads/dataiot/non_weeds/Maize/34.png'  # <-- change this!

# Preprocess image
img = image.load_img(img_path, target_size=(96, 96))  # ✅ match training input
img_array = image.img_to_array(img) / 255.0
img_array = np.expand_dims(img_array, axis=0)

# Run prediction
pred = model.predict(img_array)[0][0]
result = "WEED" if pred > 0.5 else "NON_WEED"
print(f"Model Prediction: {result} ({pred:.4f})")

# Choose your message
prediction = result

# Wait for Serial Monitor to be focused
print("⏳ Click on Arduino Serial Monitor (5s)...")
time.sleep(5)

pyautogui.write(prediction + "\n", interval=0.1)
print(f"✅ Sent to Arduino: {result}")
