
from keras.preprocessing.image import ImageDataGenerator
import cv2
import matplotlib.pyplot as plt
import tensorflow as tf
import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
# For TensorFlow
from tensorflow.keras.models import load_model

# For Keras
# from keras.models import load_model


import os

from keras.preprocessing import image

def image_detect(image_path):
    # Load the CNN model and make a prediction
    loaded_model = load_model('pothole_classifier_model.h5')  # Replace with the actual path to your CNN model
    test_image = image.load_img(f'{image_path}', target_size=(64, 64))

    test_image = image.img_to_array(test_image)
    test_image = np.expand_dims(test_image, axis=0)
    result = loaded_model.predict(test_image)

    # Get the class indices from the training set
    class_indices = {'normal': 0, 'pothole': 1}  # Replace with your class indices mapping

    # Map the predicted value to the class name
    prediction = 'pothole' if result[0][0] == class_indices['pothole'] else 'normal'
    print(prediction)
    return prediction
