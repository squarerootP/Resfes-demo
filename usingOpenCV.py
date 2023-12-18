import cv2
from matplotlib import pyplot as plt
"""
image_file = "data/text1.png"

# GRAYSCALING IMAGES
img = cv2.imread(image_file, 0) # 0 means image in grayscale

# SAVING IMAGES
cv2.imwrite("text2.png", img)

# INVERTING IMAGES
inverted_image = cv2.bitwise_not(img) 

inverted_image = cv2.cvtColor(inverted_image, cv2.COLOR_BGR2GRAY)
cv2.imshow("inverted_image", inverted_image)
cv2.waitKey(0)
cv2.imwrite("data/grayscale of inverted.png", inverted_image)

img = cv2.imread("data/text1.png")
inverted_img = cv2.bitwise_not(img)

# THRESHOLDING IMAGES
thresh, im_bw = cv2.threshold(img, 230, 255, cv2.THRESH_BINARY)
cv2.imshow("image", im_bw)
cv2.waitKey(0)
# cv2.imwrite("data/grayscale1.png", im_bw)

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

another_image = cv2.imread("data/text1.png") #original image
another_image = cv2.imread("data/grayscale of inverted.png")
no_noise = noise_removal(another_image)
cv2.imshow("img", no_noise)
cv2.waitKey(0)"""
# DILATION AND EROSION, DILATION MIGHT BE NEEDED
def thick_font(image):
    import numpy as np
    image = cv2.bitwise_not(image)
    kernel = np.ones((2, 2), np.uint8)
    image = cv2.dilate(image, kernel, iterations=1)
    image = cv2.bitwise_not(image)
    return(image)
another_image = cv2.imread("data/text1.png")
dilated_image = thick_font(another_image)
cv2.imshow("img", dilated_image)
cv2.waitKey(0)

cv2.imwrite("data/dilated image of text1.png", dilated_image)