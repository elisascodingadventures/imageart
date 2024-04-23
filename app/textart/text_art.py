from PIL import Image, ImageDraw, ImageFont
import numpy as np
from io import BytesIO
from fastapi import UploadFile

def create_image_from_text(image_file: UploadFile, word: str):
    with Image.open(image_file.file) as image:
        np_image = np.array(image)
        width, height = image.size

    image_text = Image.new('RGB', (width, height), (0, 0, 0))
    draw = ImageDraw.Draw(image_text)
    font = ImageFont.truetype("/Users/ll-studio/Desktop/textart/static/Anonymous.ttf", size=12)  # Load your font file here

    char_width, char_height = draw.textsize(word[0], font=font)
    x_text, y_text = 50, 50  # Starting position of the text

    # Sample color from the image for the text
    for char in word:
        char_x_center = x_text + char_width // 2
        char_y_center = y_text + char_height // 2
        color = tuple(np_image[min(char_y_center, height-1), min(char_x_center, width-1)])
        draw.text((x_text, y_text), char, font=font, fill=color)
        x_text += char_width

    byte_io = BytesIO()
    image_text.save(byte_io, 'PNG')
    byte_io.seek(0)
    return byte_io
