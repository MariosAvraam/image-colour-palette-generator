from PIL import Image
import numpy as np
from collections import Counter

def get_top_colors(image_path, top_n=10):
    # Open the image and convert it to RGB
    image = Image.open(image_path)
    image = image.convert("RGB")
    
    # Convert image to numpy array and reshape it to be a 2D
    data = np.array(image)
    reshaped_data = data.reshape(-1, 3)
    
    # Convert RGB values to HEX
    hex_colors = ['#{:02x}{:02x}{:02x}'.format(r, g, b) for r, g, b in reshaped_data]
    
    # Count occurrences of each color and get the top N
    color_count = Counter(hex_colors)
    common_colors = color_count.most_common(top_n)
    
    # Return only the colors (not the counts)
    return [color[0] for color in common_colors]

# Let's test the function with a sample image (assuming you have one on your end)
print(get_top_colors('image_example.png'))  # Uncomment this with an actual image path to test

