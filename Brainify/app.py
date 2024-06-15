import os
import numpy as np
import cv2
from keras.models import load_model
from flask import Flask, request, render_template
from werkzeug.utils import secure_filename

app = Flask(__name__)

# Load the model
model_path = 'braintumorV3.h5'
if not os.path.exists(model_path):
    print("Error: Model file not found.")
    exit(1)

model = load_model(model_path)
print('Model loaded. Check http://127.0.0.1:5000/')
labels = ['glioma_tumor', 'meningioma_tumor', 'no_tumor', 'pituitary_tumor']


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
        print("Error in processing image:", e)
        return None


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def upload():
    try:
        if 'file' not in request.files:
            return "No file part"

        f = request.files['file']
        if f.filename == '':
            return "No selected file"

        # Validate file type
        allowed_extensions = {'png', 'jpg', 'jpeg'}
        if '.' not in f.filename or f.filename.rsplit('.', 1)[1].lower() not in allowed_extensions:
            return "Invalid file type"

        # Save file
        uploads_dir = os.path.join(app.root_path, 'uploads')
        os.makedirs(uploads_dir, exist_ok=True)
        file_path = os.path.join(uploads_dir, secure_filename(f.filename))
        f.save(file_path)

        # Get prediction
        value = get_result(file_path)
        if value is not None:
            result = get_class_name(value)
            return result
        else:
            return "Error processing image"
    except Exception as e:
        print("Error:", e)
        return "Internal Server Error"


if __name__ == '__main__':
    app.run(debug=False)
