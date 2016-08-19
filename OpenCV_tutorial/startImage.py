import numpy as np
import cv2
from matplotlib import pyplot as plt

# Load an color image in grayscale
#img = cv2.imread("D:/SherlockHolmes/Pictures/FLASH.jpg",0)
#cv2.namedWindow('image', cv2.WINDOW_NORMAL)

# plt.imshow(img, cmap = 'gray', interpolation = 'bicubic')
# plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
# plt.show()


# cv2.imshow('image',img)
# k = cv2.waitKey(0)
# if k == 27:         # wait for ESC key to exit
#     cv2.destroyAllWindows()
# elif k == ord('s'): # wait for 's' key to save and exit
#     cv2.imwrite('messigray.png',img)
#     cv2.destroyAllWindows()

#img = cv2.imread('messi4.jpg')

img = cv2.imread("D:/SherlockHolmes/Pictures/FLASH.jpg")
b, g, r = cv2.split(img)
img2 = cv2.merge([r, g, b])
plt.subplot(121);plt.imshow(img) # expects distorted color
plt.subplot(122);plt.imshow(img2) # expect true color
plt.show()

cv2.imshow('bgr image',img) # expects true color
cv2.imshow('rgb image',img2) # expects distorted color
cv2.waitKey(0)
cv2.destroyAllWindows()