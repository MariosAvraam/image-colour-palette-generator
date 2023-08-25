import os
from flask import Flask, request, render_template
from utils import allowed_file, save_file
from image_processing import get_top_colors

# Initialize Flask application
app = Flask(__name__)

# Configuration for uploaded file directory
UPLOAD_FOLDER = 'static/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Ensure the upload directory exists, create it if not
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

@app.route('/', methods=['GET'])
def index():
    """Render the main page for file upload."""
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_image():
    """Handles image upload and processing to return dominant colors."""
    message = None
    colors = None
    uploaded_image_path = None

    try:
        # Check if the request contains the file part
        if 'file' not in request.files:
            message = "No file part in the request."
            return render_template('index.html', message=message)

        file = request.files['file']

        # Check if no file was selected
        if file.filename == '':
            message = "No file selected."
            return render_template('index.html', message=message)

        # Process the file if it's an allowed type
        if file and allowed_file(file.filename):
            filepath = save_file(file, app.config['UPLOAD_FOLDER'])
            uploaded_image_path = os.path.join('uploads', os.path.basename(filepath)).replace('\\', '/')
            colors = get_top_colors(filepath)
        else:
            message = "Invalid file type. Please upload an image."
    
    except Exception as e:
        # Handle unexpected errors during image processing
        message = "An error occurred while processing the image. Please try again."

    return render_template('index.html', colors=colors, uploaded_image_path=uploaded_image_path, message=message)

# Start the Flask application
if __name__ == '__main__':
    app.run(debug=True)
