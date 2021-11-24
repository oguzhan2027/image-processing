import cv2
import numpy as np

foto = cv2.imread("orangutan.jpg")
cv2.imshow("orangutan",foto)
cv2.waitKey()
B = foto [:,:,0]
G = foto [:,:,1]
R = foto [:,:,2]
#cv2.imshow("Mavi",B)
#cv2.imshow("Yesil",G)
 #cv2.imshow("Kirmizi",R)
 #cv2.waitKey()

fotogray = cv2.imread("orangutan.jpg",0)
cv2.imshow("orangutan",fotogray)
cv2.waitKey()
from matplotlib import pyplot as plt
imGray = 0.2989 * R + 0.5870 * G+ 0.1140*B
plt.imshow(imGray,cmap='gray')
plt.show()

