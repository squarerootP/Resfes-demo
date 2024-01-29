import pytesseract
import cv2
import usingOpenCV
# INPUTING DIFFERENT IMAGE VARIATIONS
# img = "data/dilated image of text1.png"
# im = cv2.imread(img)
# imo = "data/text1.png"
# im = cv2.imread(imo)
img2 = "data/grayscale of text1.png"
im2 = cv2.imread(img2)

# imgtext2 = cv2.imread("data/text2.png")
# imgtext2 = cv2.bitwise_not(imgtext2)
# imgtext2 = usingOpenCV.grayscaling(imgtext2)
# imgtext2 = usingOpenCV.threshold_img(imgtext2, 128, 255)
# imgtext2 = cv2.bitwise_not(imgtext2)

# cv2.imshow("text2img", im2)
# cv2.waitKey(0)
# OCR THE IMAGES
text = pytesseract.image_to_string(im2, lang="eng", config="--psm 6 --oem 3")

print(text)
text = text[text.find("Slot 1") : text.find("More note")-1]

# SAVE OUTPUT TEXT TO FILE
with open("output2","w") as file:
    file.write(text)


