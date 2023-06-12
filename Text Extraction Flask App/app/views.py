# Important imports
from app import app
from flask import request, render_template, url_for
import os
import cv2
import numpy as np
from PIL import Image
import random
import string
import pytesseract
import re
import tensorflow as tf
import easyocr

# Adding path to config
app.config['INITIAL_FILE_UPLOADS'] = 'app/static/uploads'

# Route to home page
@app.route("/", methods=["GET", "POST"])
def index():
    # Execute if request is get
    if request.method == "GET":
        full_filename = 'images/white_bg.jpg'
        return render_template("index.html", full_filename=full_filename)

    # Execute if request is post
    if request.method == "POST":
        image_upload = request.files['image_upload']
        imagename = image_upload.filename
        image = Image.open(image_upload)

        # Converting image to array
        image_arr = np.array(image.convert('RGB'))
        # Converting image to grayscale
        gray_img_arr = cv2.cvtColor(image_arr, cv2.COLOR_BGR2GRAY)
        # Converting image back to RGB
        image = Image.fromarray(gray_img_arr)

        # Printing lowercase
        letters = string.ascii_lowercase
        # Generating unique image name for dynamic image display
        name = ''.join(random.choice(letters) for i in range(10)) + '.png'
        full_filename = 'uploads/' + name

        # Extracting text from image using Tesseract OCR
        custom_config = r'-l eng --oem 3 --psm 6'
        tesseract_text = pytesseract.image_to_string(image, config=custom_config)

        # Extracting text from image using easyocr
        reader = easyocr.Reader(['en'])
        easyocr_text = reader.readtext(image_arr)

        # Remove symbols if any
        characters_to_remove = "!()@—*“>+-/,'|£#%$&^_~"
        new_string = tesseract_text
        for character in characters_to_remove:
            new_string = new_string.replace(character, "")

        # Converting string into list to display extracted text in separate lines
        new_string = new_string.split("\n")

        # Extract numeric values using regular expression from each element of new_string list
        numeric_values = []
        for line in new_string:
            values = re.findall(r'\d+', line)
            numeric_values.extend(values)

        # TensorFlow operations
        # Example: Generating a random tensor
        random_tensor = tf.random.normal(shape=(3, 3))

        # Saving image to display in HTML
        img = Image.fromarray(image_arr, 'RGB')
        img.save(os.path.join(app.config['INITIAL_FILE_UPLOADS'], name))

        # Returning template, filename, extracted text, and numeric values
        return render_template('index.html', full_filename=full_filename, text=new_string, numeric_values=numeric_values,
                               random_tensor=random_tensor, easyocr_text=easyocr_text)

# Main function
if __name__ == '__main__':
    app.run(debug=True)
