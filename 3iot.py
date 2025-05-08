from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np

# Load your trained model
model = load_model('weed_classifier.h5')

# Path to a test image (change this!)
img_path = r'C:/Users/pes12/Downloads/dataiot/non_weeds/Maize/222.png'

# Load image and preprocess
#img = image.load_img(img_path, target_size=(224, 224))
img = image.load_img(img_path, target_size=(96, 96))
img_array = image.img_to_array(img) / 255.0
img_array = np.expand_dims(img_array, axis=0)

# Predict
pred = model.predict(img_array)[0][0]

# Output result
if pred >= 0.5:
    print("🌿 It's a WEED!")
else:
    print("🌾 It's NOT a weed.")
