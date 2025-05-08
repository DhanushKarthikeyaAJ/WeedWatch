import serial
import time
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np

# Load trained model
model = load_model('weed_classifier.h5')

# Serial port setup (adjust COM port)
ser = serial.Serial('COM5', 9600)  # Replace 'COM5' with your Arduino's port
time.sleep(2)  # Give time for Arduino to reset

# Image path
img_path = r'C:/Users/pes12/Downloads/dataiot/non_weeds/Maize/222.png'  # <-- change this!

# Preprocess image
img = image.load_img(img_path, target_size=(96, 96))  # ✅ match training input
img_array = image.img_to_array(img) / 255.0
img_array = np.expand_dims(img_array, axis=0)

# Run prediction
pred = model.predict(img_array)[0][0]
result = "WEED" if pred > 0.5 else "NON_WEED"
print(f"Model Prediction: {result} ({pred:.4f})")

# Send to Arduino
#ser.write(result.encode())
import time
time.sleep(2)
ser.write((result + "\n").encode())
ser.close()
