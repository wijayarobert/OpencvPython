#Shapes and Texts

import cv2
import numpy as np

img = np.zeros((512, 512, 3), np.uint8)
# print(img)
# #make blue img
# img[:] = 255, 0, 0

cv2.line(img,(0,0), (300,300), (0,255,0), 3)
cv2.rectangle(img, (0,0), (250, 300), (0,0,255), cv2.FILLED)
cv2.circle(img, (400,450), 20, (255,0,0), 5)
cv2.putText(img, " OPEN CV ", (300, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 150, 0), 2)

cv2.imshow("Image", img)

cv2.waitKey(0)