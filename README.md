# Setup Guide for Brainify ML Flask App

## 0. Download the zip file from http://detect-tumor.rf.gd/V1.zip

## 1. Unzip the file 
unzip V1.zip

## 2. Change the dir to Brainify 
cd brainify

## 3. Install Dependencies
pip install -r requirements.txt

## 4. Setup Jupyter Notebook
cd notebooks

## 5. Run Jupyter Notebook
jupyter notebook

## 6. Prepare Training Data
Ensure that your training data images are located in the `data` folder within the notebook directory.

## 7. Training the Model
Follow the instructions in the notebook (`brainify_ml.ipynb`) to train and test your ML model using the provided data.

## 8. Deploying the Flask App
Navigate back to the root directory of your Brainify project and run the Flask app.
cd ..
python app.py

## 9. Accessing the Deployed Version http://detect-tumor.rf.gd/
Once the Flask app is running, the online version of your project can be accessed through the URL: `detect-tumor.rf.gd`.

## 10. Patient Login Credentials
To login as a patient on the website, use the following credentials:
- Email: `patient@brainify.com`
- Password: `123`
