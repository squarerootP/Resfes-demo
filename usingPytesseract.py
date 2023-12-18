import pytesseract
import cv2

img = "data/grayscale of inverted.png"
im = cv2.imread(img)
imo = "data/text1.png"
im = cv2.imread(imo)
img2 = "data/grayscale of text1.png"
im2 = cv2.imread(img2)


# text1 = pytesseract.image_to_string(im)
# print(text1)
# print("----")
text2 = pytesseract.image_to_string(imo)
print(text2)

with open("output","w") as file:
    file.write(text2)