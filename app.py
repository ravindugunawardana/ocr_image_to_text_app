from flask import Flask, render_template, request
import pytesseract
from PIL import Image
import os

app = Flask(__name__)

# Set Tesseract path (Windows)
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/upload', methods=['POST'])
def upload_image():
    if 'image' not in request.files:
        return "No file uploaded"

    image_file = request.files['image']
    image_path = os.path.join(UPLOAD_FOLDER, image_file.filename)
    image_file.save(image_path)

    image = Image.open(image_path)
    extracted_text = pytesseract.image_to_string(image)

    return render_template(
        'index.html',
        extracted_text=extracted_text
    )


if __name__ == '__main__':
    app.run(debug=True)
