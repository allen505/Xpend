
import numpy as np
import pytesseract as pt
from PIL import Image
import cv2
import tempfile

IMAGE_SIZE = 1800
BINARY_THREHOLD = 180

def set_image_dpi(file_path):
    im = Image.open(file_path)
    length_x, width_y = im.size
    factor = max(1, int(IMAGE_SIZE / length_x))
    size = factor * length_x, factor * width_y
    # size = (1800, 1800)
    im_resized = im.resize(size, Image.ANTIALIAS)
    temp_file = tempfile.NamedTemporaryFile(delete=False, suffix='.jpg')
    temp_filename = temp_file.name
    im_resized.save(temp_filename, dpi=(300, 300))
    return temp_filename


def image_smoothening(img):
    ret1, th1 = cv2.threshold(img, BINARY_THREHOLD, 255, cv2.THRESH_BINARY)
    ret2, th2 = cv2.threshold(th1, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    blur = cv2.GaussianBlur(th2, (1, 1), 0)
    ret3, th3 = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    return th3


def remove_noise_and_smooth(file_name):
    img = cv2.imread(file_name, 0)
    filtered = cv2.adaptiveThreshold(img.astype(np.uint8), 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 41, 3)
    kernel = np.ones((1, 1), np.uint8)
    opening = cv2.morphologyEx(filtered, cv2.MORPH_OPEN, kernel)
    closing = cv2.morphologyEx(opening, cv2.MORPH_CLOSE, kernel)
    img = image_smoothening(img)
    or_image = cv2.bitwise_or(img, closing)
    return or_image


def process_image_for_ocr(file_path):
    # TODO : Implement using opencv
    temp_filename = set_image_dpi(file_path)
    im_new = remove_noise_and_smooth(temp_filename)
    return im_new


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
    im=process_image_for_ocr(file_path)
    print(im)
    #set_image_dpi(file_path)
    #image_smoothening(file_path)
    #remove_noise_and_smooth(file_path)
    print('--- Start recognize text from image ---')
    text = pt.image_to_string(im)
    print(text)
    #text = str(text)
    file2 = open("prctxt.txt", 'w')
    file2.write(str(text))
    file2.close()
    print("------ Done -------")
#return textext()