import cv2
import pytesseract
import numpy as np


# get grayscale image
def get_grayscale(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


# noise removal
def remove_noise(image):
    return cv2.medianBlur(image, 5)


# thresholding
def thresholding(image):
    return cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]


# dilation
def dilate(image):
    kernel = np.ones((5, 5), np.uint8)
    return cv2.dilate(image, kernel, iterations=1)


# erosion
def erode(image):
    kernel = np.ones((5, 5), np.uint8)
    return cv2.erode(image, kernel, iterations=1)


# opening - erosion followed by dilation
def opening(image):
    kernel = np.ones((5, 5), np.uint8)
    return cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel)


# canny edge detection
def canny(image):
    return cv2.Canny(image, 100, 200)


# skew correction
def deskew(image):
    coords = np.column_stack(np.where(image > 0))
    angle = cv2.minAreaRect(coords)[-1]

    if angle < -45:
        angle = -(90 + angle)
    else:
        angle = -angle

    (h, w) = image.shape[:2]
    center = (w // 2, h // 2)
    M = cv2.getRotationMatrix2D(center, angle, 1.0)
    rotated = cv2.warpAffine(image, M, (w, h), flags=cv2.INTER_CUBIC, borderMode=cv2.BORDER_REPLICATE)

    return rotated


# template matching
def match_template(image, template):
    return cv2.matchTemplate(image, template, cv2.TM_CCOEFF_NORMED)


from sys import argv

#jpg_path="pdf/RG_100068630897.pdf0.jpg"


if len(argv) > 1:
    jpg_path = argv[1]
else:
    jpg_path = input('pdf file path>>> ')

try:
    # Store Pdf with convert_from_path function
    print(jpg_path)
    image = cv2.imread(jpg_path)
    #gray = get_grayscale(image)
    #thresh = thresholding(gray)
    #opening = opening(gray)
    #canny = canny(gray)

    custom_config = r'--oem 3 --psm 6'
    txt_content = (pytesseract.image_to_string(image, config=custom_config))

    with open(jpg_path + ".txt", 'w') as file:
        file.write(txt_content)


except FileNotFoundError:
    print(f'{argv[1]} not found')

except TypeError as error:
    print(error)

