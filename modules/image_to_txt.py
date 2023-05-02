import os
import pytesseract
from PIL import Image

def image_to_text(input_dir, output_dir):
    try:

        image_files = [f for f in os.listdir(input_dir) if f.endswith('.jpg') or f.endswith('.png')]
        output_file = os.path.join(output_dir, 'output.txt')

        with open(output_file, 'w') as f:
            for image_file in image_files:
                image_path = os.path.join(input_dir, image_file)
                image = Image.open(image_path)
                text = pytesseract.image_to_string(image)
                f.write(text)

        print('Text extracted from images and saved to directory:', output_dir)

    except:
        print('Error in converting image to text:', image_path)
