# Image Color Extractor

Extract the top 10 dominant colors from any uploaded image using this simple Flask-based web application.

![Screenshot of website](static/images/website_screenshot_image.png)

## Features

- Easy to use: Just upload an image and see the results.
- Fast processing: Uses NumPy and PIL for quick image analysis.
- Interactive: Click on any color box to copy its HEX code.

## Installation

1. Clone the repository:
```
git clone https://github.com/MariosAvraam/image-colour-palette-generator.git
```

2. Navigate to the project directory:
```
cd image-colour-palette-generator
```

3. (Optional) Set Up a Virtual Environment:
```
python -m venv venv
source venv/bin/activate #On Windows use venv\Scripts\activate
```

4. Install the required packages:
```
pip install -r requirements.txt
```

## Usage

1. Run the Flask app:
```
python app.py
```

2. Open your web browser and go to:
```
http://127.0.0.1:5000/
```

3. Upload an image and view the top 10 dominant colors extracted from it.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

[MIT](https://choosealicense.com/licenses/mit/)