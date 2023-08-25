import os
from flask import Flask, request, render_template
from utils import allowed_file, save_file
from image_processing import get_top_colors

app = Flask(__name__)

UPLOAD_FOLDER = 'static/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Check if the UPLOAD_FOLDER exists, if not, create it
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_image():
    message = None
    colors = None
    uploaded_image_path = None

    try:
        if 'file' not in request.files:
            message = "No file part in the request."
            return render_template('index.html', message=message)

        file = request.files['file']

        if file.filename == '':
            message = "No file selected."
            return render_template('index.html', message=message)

        if file and allowed_file(file.filename):
            filepath = save_file(file, app.config['UPLOAD_FOLDER'])
            uploaded_image_path = os.path.join('uploads', os.path.basename(filepath)).replace('\\', '/')
            colors = get_top_colors(filepath)
        else:
            message = "Invalid file type. Please upload an image."
    
    except Exception as e:
        # This will catch any unexpected errors during processing.
        message = "An error occurred while processing the image. Please try again."

    return render_template('index.html', colors=colors, uploaded_image_path=uploaded_image_path, message=message)


if __name__ == '__main__':
    app.run(debug=True)
