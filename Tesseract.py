# GoogleMeetBot
# By Adin Ackerman
# Tesseract interface library

import numpy as np
import pytesseract
import cv2
from PIL import ImageGrab

def imToString(x1,y1,x2,y2):
    pytesseract.pytesseract.tesseract_cmd ='Tesseract/tesseract.exe'
    cap = ImageGrab.grab(bbox =(x1,y1,x2,y2))
    tesstr = pytesseract.image_to_string(
            cv2.cvtColor(np.array(cap), cv2.COLOR_BGR2GRAY),
            lang ='eng')
    return tesstr
