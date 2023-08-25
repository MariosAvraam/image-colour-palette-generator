from PIL import Image
import numpy as np
from collections import Counter

def get_top_colors(image_path, top_n=10):
    """
    Extract the top N dominant colors from an image.

    Args:
        image_path (str): Path to the image file.
        top_n (int): Number of dominant colors to retrieve.

    Returns:
        list: List of HEX values of dominant colors.
    """
    # Open the image and convert to RGB mode
    image = Image.open(image_path)
    image = image.convert("RGB")

    # Convert image data to numpy array and reshape
    data = np.array(image)
    reshaped_data = data.reshape(-1, 3)

    # Convert RGB values to HEX
    hex_colors = ['#{:02x}{:02x}{:02x}'.format(r, g, b) for r, g, b in reshaped_data]

    # Count occurrences of each color
    color_count = Counter(hex_colors)

    # Get top N colors
    common_colors = color_count.most_common(top_n)

    return [color[0] for color in common_colors]
