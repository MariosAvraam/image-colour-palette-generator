import os
from flask import Flask, request, jsonify, render_template, redirect, url_for
from utils import allowed_file, save_file
from image_processing import get_top_colors

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Check if the UPLOAD_FOLDER exists, if not, create it
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_image():
    colors = None
    if 'file' not in request.files:
        return redirect(url_for('index'))
    file = request.files['file']
    if file.filename == '':
        return redirect(url_for('index'))
    if file and allowed_file(file.filename):
        filepath = save_file(file, app.config['UPLOAD_FOLDER'])
        colors = get_top_colors(filepath)
    return render_template('index.html', colors=colors)

if __name__ == '__main__':
    app.run(debug=True)
