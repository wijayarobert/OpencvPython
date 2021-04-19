#Chapter 1 and Chapter 2
#Chapter 1: Read Img, Video and Webcam
#Chapter 2: Basic Funtions

import cv2
import numpy as np

# READ IMG
# =========
# print("package imported")
#
# img = cv2.imread("Resources/lena.png")
#
# cv2.imshow("Output", img)
# cv2.waitKey(0)

# READ VIDEO
# cap = cv2.VideoCapture("Resources/video_test.mp4")
#
# while True:
#     success, img = cap.read()
#     cv2.imshow("Video", img)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# READ FROM WEBCAM
# cap = cv2.VideoCapture(0)
# cap.set(3, 640) #width
# cap.set(4, 480) #height
#
# while True:
#     success, img = cap.read()
#     cv2.imshow("Video", img)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

img = cv2.imread("Resources/lena.png")
kernel = np.ones((5,5), np.uint8)

imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray, (7,7), 0)
imgCanny = cv2.Canny(img, 200, 200)
imgDialation = cv2.dilate(imgCanny, kernel, iterations=1)
imgEroded = cv2.erode(imgDialation, kernel, iterations=1)

cv2.imshow("Gray Image", imgGray)
cv2.imshow("Blur Image", imgBlur)
cv2.imshow("Canny Image", imgCanny)
cv2.imshow("Dialation Image", imgDialation)
cv2.imshow("Eroded Image", imgEroded)

cv2.waitKey(0)