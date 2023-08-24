from PIL import Image
import numpy as np
from collections import Counter

def get_top_colors(image_path, top_n=10):
    image = Image.open(image_path)
    image = image.convert("RGB")
    data = np.array(image)
    reshaped_data = data.reshape(-1, 3)
    hex_colors = ['#{:02x}{:02x}{:02x}'.format(r, g, b) for r, g, b in reshaped_data]
    color_count = Counter(hex_colors)
    common_colors = color_count.most_common(top_n)
    return [color[0] for color in common_colors]
