#Chapter3: Resizing and Cropping

import cv2
import numpy as np

img = cv2.imread("Resources/lena.png")
print(img.shape)

imgResize = cv2.resize(img, (1000, 500))
print(imgResize.shape)

imgCropped = img[0:200, 200:480]

cv2.imshow("Image", img)
cv2.imshow("Resized Image", imgResize)
cv2.imshow("Cropped Image", imgCropped)
cv2.waitKey(0)
