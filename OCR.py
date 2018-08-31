import numpy as np
import pytesseract as pt
from PIL import Image
import cv2
   
def thresholding(im):
    resize = cv2.resize(im, None, fx=1.2, fy=1.2, interpolation=cv2.INTER_CUBIC)
    th = cv2.adaptiveThreshold(resize, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 95, 20)
    return th


def pre_process_ocr(file_name):
    im = cv2.imread(file_name, 0)
    thresh = thresholding(im)
    kernel = np.ones((1,1),np.uint8)
    erode = cv2.erode(thresh, kernel, iterations = 1)
    dilation = cv2.dilate(erode, kernel, iterations=1)
    opening = cv2.morphologyEx(dilation, cv2.MORPH_OPEN, kernel)
    closing = cv2.morphologyEx(opening, cv2.MORPH_CLOSE, kernel)
    bfilter = cv2.bilateralFilter(closing,9,75,75)
    return bfilter

####################################################################################################
def textext():
    # Open the file with read only permit
    f = open('prctxt.txt', "r")
    # use readlines to read all lines in the file
    # The variable "lines" is a list containing all lines in the file
    lines = f.readlines()
    # close the file after reading the lines.
    amt=0
    amt1 = ''
    for i in lines:
        i = i.lower()

        if i.startswith('net amount '):
            for j in i:
                if not j.isalpha():
                    amt1 = amt1 + j
    a = (amt1.split())
    print(a[1])
    amt += a[1]
    f.close()
    return amt

#####################################################################################################
def final_image(file_path):
    pt.pytesseract.tesseract_cmd = r"C:\Program Files (x86)\Tesseract-OCR\tesseract.exe"
    im = pre_process_ocr(file_path)
    print('--- Start recognize text from image ---')
    text = pt.image_to_string(im)
    print(text)
    file2 = open("prctxt.txt", 'w')
    file2.write(str(text))
    file2.close()
    print("------ Done -------")
#return textext()
