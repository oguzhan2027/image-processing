import cv2
import numpy as np
image =cv2.imread('fotograflarin-flu-cikmasinin-nedenleri.jpg')

blur_filter1=np.ones((3,3))/(9.0)
image_blur1 = cv2.filter2D(image,-1,blur_filter1)
gaussian_blur=cv2.GaussianBlur(image,(7,7),0)
medyan_filter=cv2.medianBlur(image,5)

cv2.imshow('babun1',image_blur1)
cv2.imshow('original',image)
cv2.imshow('gaussian filter',gaussian_blur)
cv2.imshow('median filter',medyan_filter)
img_bilateral=cv2.bilateralFilter((gaussian_blur),3,7,50)
img_bilateral2=cv2.bilateralFilter((img_bilateral),3,7,50)
cv2.imshow('bualnık',img_bilateral)
cv2.imshow('çok bulanık',img_bilateral2)
cv2.waitKey()