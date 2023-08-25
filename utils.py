import os
from werkzeug.utils import secure_filename

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

def allowed_file(filename):
    """
    Check if the given file is of an allowed type.

    Args:
        filename (str): Name of the file.

    Returns:
        bool: True if allowed, False otherwise.
    """
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def save_file(file, upload_folder):
    """
    Save the uploaded file to the specified directory.

    Args:
        file (File): Uploaded file object.
        upload_folder (str): Directory to save the uploaded file.

    Returns:
        str: Path where the file was saved.
    """
    filename = secure_filename(file.filename)
    filepath = os.path.join(upload_folder, filename)
    file.save(filepath)
    return filepath
