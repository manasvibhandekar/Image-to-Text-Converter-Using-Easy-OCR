#from app import app

#if __name__ == '__main__':
 #  app.run()

from flask import Flask, request, jsonify
import easyocr

app = Flask(__name__)
reader = easyocr.Reader(['en'])  # Specify the languages you want to extract

@app.route('/extract_text', methods=['POST'])
def extract_text():
    image_file = request.files['image']
    image = image_file.read()
    result = reader.readtext(image)
    extracted_text = [res[1] for res in result]
    return jsonify({'text': extracted_text})

if __name__ == '__main__':
    app.run()
