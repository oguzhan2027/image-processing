import cv2
import numpy as np
img =cv2.imread('castlee.jpg',0)
cv2.imshow("giris",img)
ret,esik_image=cv2.threshold(img,80,255,cv2.THRESH_BINARY)
kernel=np.ones((2,2),dtype=np.uint8)
erode_result=cv2.erode(esik_image,kernel,iterations=3)
dilate_result=cv2.dilate(esik_image,kernel,iterations=3)
cv2.imshow("esiklenen giris görünütüsü",esik_image)
cv2.imshow("erezyon",erode_result)
cv2.imshow("genisleme",dilate_result)
cv2.waitKey()