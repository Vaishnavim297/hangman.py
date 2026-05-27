import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image

st.title("🖼️ CNN Image Classifier App")
st.write("Upload an image to see the trained CNN model classify it.")

CLASS_NAMES = ['Airplane', 'Automobile', 'Bird', 'Cat', 'Deer', 'Dog', 'Frog', 'Horse', 'Ship', 'Truck']

@st.cache_resource
def load_model():
    return tf.keras.models.load_model('cnn_model.h5')

try:
    model = load_model()
    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption='Uploaded Image', use_container_width=True)
        
        img = image.resize((32, 32)).convert("RGB")
        img_array = np.array(img) / 255.0
        img_batch = np.expand_dims(img_array, axis=0)
        
        predictions = model.predict(img_batch)
        predicted_class = CLASS_NAMES[np.argmax(predictions[0])]
        confidence = np.max(predictions[0]) * 100
        
        st.success(f"Prediction: **{predicted_class}** ({confidence:.2f}% confidence)")
except Exception as e:
    st.error("Please run 'python train.py' in your terminal first to generate 'cnn_model.h5'.")