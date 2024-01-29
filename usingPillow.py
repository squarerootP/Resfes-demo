import cv2
from PIL import Image
import pytesseract

# im_file = "data/Screenshot 2023-12-14 200033.png"
# im = Image.open(im_file)
# print(im)
# print(im.size) #show the size of the image
# im.show() #show the image
# im.rotate(90) #rotate the image with certain angle
# im.save("data/Hello1.png") # save image with certain name within certain foler using folder/name
img = "data/text1.png"
im = Image.open(img)
im.show()
