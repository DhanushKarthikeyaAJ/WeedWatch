import tensorflow as tf

# Load your model
model = tf.keras.models.load_model("weed_classifier.h5")

# Convert to TensorFlow Lite
converter = tf.lite.TFLiteConverter.from_keras_model(model)
converter.optimizations = [tf.lite.Optimize.DEFAULT]  # This helps reduce model size
tflite_model = converter.convert()

# Save the .tflite model
with open("weed_classifier.tflite", "wb") as f:
    f.write(tflite_model)

print("✅ Model converted to TensorFlow Lite!")
