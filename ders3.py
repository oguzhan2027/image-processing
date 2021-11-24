import cv2
import numpy as np
image = cv2.imread('castlee.jpg',0)
inverted = np.invert(image)
cv2.imshow("original",image)
cv2.imshow("inverted",inverted)
negimage = 255-image
cv2.imshow("negimage",negimage)
cv2.waitKey()