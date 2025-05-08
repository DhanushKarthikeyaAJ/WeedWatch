from PIL import Image
import numpy as np

# Load and preprocess image
img_path = r'C:/Users/pes12/Downloads/dataiot/non_weeds/Maize/222.png'  # <-- change this!
img = Image.open(img_path).resize((224, 224))
img = np.array(img, dtype=np.float32) / 255.0
img = np.expand_dims(img, axis=0)  # shape becomes (1, 224, 224, 3)

# Save as a C-style float array
with open("image_data.cc", "w") as f:
    f.write("const float test_image[1][224][224][3] = ")
    f.write(np.array2string(img, separator=',', threshold=np.inf).replace('\n', ''))
    f.write(";")
