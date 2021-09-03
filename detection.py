import re

def isValidPanCardNo(panCardNo):
	regex = "[A-Z]{5}[0-9]{4}[A-Z]{1}"
	p = re.compile(regex)
	if(re.search(p, panCardNo) and
	len(panCardNo) == 10):
		return panCardNo



def detect_text(path,card):
    """Detects text in the file."""
    from google.cloud import vision
    import io
    client = vision.ImageAnnotatorClient()

    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = vision.Image(content=content)

    response = client.text_detection(image=image)
    texts = response.text_annotations
    print('Texts:')
    if response.error.message:
        raise Exception(
            '{}\nFor more info on error messages, check: '
            'https://cloud.google.com/apis/design/errors'.format(
                response.error.message))
    for text in texts:
        if isValidPanCardNo(text.description)!=None:
            print(isValidPanCardNo(text.description))

    print(card)
    lst=[]
    for text in texts:
        lst.append(text.description)
    print(lst)

import json
import pytesseract
import cv2
import numpy as np
import sys
import re
import os
from PIL import Image
import ftfy
      
'''module which we made to read the text of the document'''
import io

img = cv2.imread("adhar.jpg")
img = cv2.resize(img, None, fx=2, fy=2,interpolation=cv2.INTER_CUBIC)
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
var = cv2.Laplacian(img, cv2.CV_64F).var()
if var < 50:
    print("Image is Too Blurry....")
    k= input('Press Enter to Exit.')
    exit(1)


filename = "adhar.jpg"
text = pytesseract.image_to_string(Image.open(filename), lang = 'eng')

text_output = open('output.txt', 'w', encoding='utf-8')
text_output.write(text)
text_output.close()

file = open('output.txt', 'r', encoding='utf-8')
text = file.read()

text = ftfy.fix_text(text)
text = ftfy.fix_encoding(text)

if "income" in text.lower() or "tax" in text.lower() or "department" in text.lower():
    card="pan"
else:
    card="adhar"





detect_text(r"adhar.jpg",card)


 #set GOOGLE_APPLICATION_CREDENTIALS=neural-proton-321810-6acea742b507.json