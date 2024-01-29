import cv2
from matplotlib import pyplot as plt

image_file = "data/text1.png"

# GRAYSCALING IMAGES
img = cv2.imread(image_file) # 0 means image in grayscale
def grayscaling(img):
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    return(img)
# SAVING IMAGES


# INVERTING IMAGES
inverted_image = cv2.bitwise_not(img) 


# cv2.imshow("inverted_image", inverted_image)
# cv2.waitKey(0)


img = cv2.imread("data/text1.png")
inverted_img = cv2.bitwise_not(img)
def inverting(img):
    img = cv2.bitwise_not(img)
    return(img)
# THRESHOLDING IMAGES

def threshold_img(img, code1=230, code2=250):
    thresh, im_bw = cv2.threshold(img, code1, code2, cv2.THRESH_BINARY)
    return(im_bw)

# NOISE REMOVAL
def noise_removal(image):
    import numpy as np
    kernel = np.ones((1, 1), np.uint8)
    image = cv2.dilate(image, kernel, iterations=1)
    kernel = np.ones((1,1), np.uint8)
    image = cv2.erode(image, kernel, iterations=1)
    # image = cv2.morphologyEx(image, cv2.MORPH_CLOSE, kernel)
    # image = cv2.medianBlur(image, 3)
    return(image)

"""another_image = cv2.imread("data/text1.png") #original image
another_image = cv2.imread("data/grayscale of inverted.png")
no_noise = noise_removal(another_image)
cv2.imshow("img", no_noise)
cv2.waitKey(0)"""
# DILATION AND EROSION, DILATION MIGHT BE NEEDED
def thick_font(image):
    import numpy as np
    image = cv2.bitwise_not(image)
    kernel = np.ones((2, 1), np.uint8)
    image = cv2.dilate(image, kernel, iterations=1)
    image = cv2.bitwise_not(image)
    return(image)
another_image = cv2.imread("data/text1.png")
dilated_image = thick_font(another_image)
# cv2.imshow("img", dilated_image)
# cv2.waitKey(0)
