import cv2
import numpy as np
screenRead = cv2.VideoCapture(0)
while (1):
 _, image = screenRead.read()
 gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
 ret, esik_image = cv2.threshold(gray, 110, 255, cv2.THRESH_BINARY)
 kernel = np.ones((5, 5), np.uint8)
 opening=cv2.erode(esik_image, kernel, iterations=2)
 cv2.imshow('Erozyon', opening)
 cv2.imshow('orijinal', esik_image)
 if cv2.waitKey(1) & 0xFF == ord('a'):
    break