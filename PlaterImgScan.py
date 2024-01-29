import os
import re
import cv2 as cv
import pytesseract as tesseract
from PIL import Image

def ImageToPlates(image):
    # Convert frame to inverted grayscale for better OCR results
    grayscale = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    blur = cv.GaussianBlur(grayscale, (3,3), 0)
    thresh = cv.threshold(blur, 0, 255, cv.THRESH_BINARY_INV + cv.THRESH_OTSU)[1]

    # Remove some noise
    kernel = cv.getStructuringElement(cv.MORPH_RECT, (3, 3))
    opening = cv.morphologyEx(thresh, cv.MORPH_OPEN, kernel, iterations=1)
    invert = 255 - opening

    text = tesseract.image_to_string(invert, lang='eng', config='--psm 6')

    title = text.split('\n')[0]
    tagline = text.split('\n')[1]
    mount = text.split('Mount: ')[1].split(' ')[0]
    gain = text.split('Gain: ')[1].split('\n')[0]
    power = text.split('Power: ')[1].split('\n')[0]
    length = text.split('Length: ')[1].split(' ')[0]

    metadata_1 = ''
    if text.split('\n')[2] != mount:
        metadata_1 = text.split('\n')[2]

    metadata_2 = ''
    if text.split('\n')[3] != mount:
        metadata_2 = text.split('\n')[3].split(' ')[0]

    print(f'Title: {title}')
    print(f'Tagline: {tagline}')
    print(f'Metadata 1:  {metadata_1}')
    print(f'Metadata 2:  {metadata_2}')
    print(f'Gain: {gain}')
    print(f'Mount: {mount}')
    print(f'Power: {power}')
    print(f'Length: {length}')
    

def TextToDict(text):
    pattern = re.compile(r'(\w+): ([\w\s.]+)')
    matches = pattern.findall(text)
    key_value_pairs = dict(matches)
    return key_value_pairs

# Load the image
images_dir = "Cards/"

for image in os.listdir(images_dir):
    cv_image = cv.imread(f'Cards/{image}')

    if image is not None:
        print(f'Processing Image: {image}')
        ImageToPlates(cv_image)
    else:
        print(f'Error, could not read image {image}')
