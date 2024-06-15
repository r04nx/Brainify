import os
import numpy as np
import cv2
import streamlit as st
from keras.models import load_model

# Load the model
model_path = 'braintumorV3.h5'
if not os.path.exists(model_path):
    st.error("Error: Model file not found.")
    st.stop()

model = load_model(model_path)
st.write('Model loaded.')

labels = ['glioma_tumor', 'eningioma_tumor', 'no_tumor', 'pituitary_tumor']

def get_class_name(class_no):
    class_names = [
        "Warning! Glioma Tumor detected. Please contact us immediately for further evaluation and treatment.",
        "Warning! Meningioma Tumor detected. Please contact us immediately for further evaluation and treatment.",
        "No Brain Tumor",
        "Warning! Pituitary Tumor detected. Please contact us immediately for further evaluation and treatment."]
    return class_names[class_no]

def get_result(img):
    try:
        image = cv2.imread(img)
        image = cv2.resize(image, (150, 150))  # Resize the image
        img_array = np.array(image)  # Convert to array
        img_array = img_array.reshape(1, 150, 150, 3)  # Reshape
        predictions = model.predict(img_array)
        result = np.argmax(predictions)
        return result
    except Exception as e:
        st.error("Error in processing image:", e)
        return None

st.title("Brain Tumor Detection")
st.write("Upload an image to detect brain tumors:")

uploaded_file = st.file_uploader("Choose a file", type=["png", "jpg", "jpeg"])

if uploaded_file is not None:
    file_path = uploaded_file.name
    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    value = get_result(file_path)
    if value is not None:
        result = get_class_name(value)
        st.write(result)
    else:
        st.error("Error processing image")