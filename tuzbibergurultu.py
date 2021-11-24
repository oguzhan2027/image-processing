import cv2
import numpy as np
from skimage.util import random_noise
img= cv2.imread('orangutan.jpg')
noise_img =random_noise(img,mode="s&p",amount =0.1)
noise_img=np.array(255*noise_img,dtype='uint8')
img_gaussian=cv2.GaussianBlur(noise_img,(3,3),0)
img_bilateral=cv2.bilateralFilter(noise_img,3,70,50)
median=cv2.medianBlur(noise_img,3)
blur_filter1= np.ones((3,3),np.float64)/(9.0)
mean_image=cv2.filter2D(noise_img,-1,blur_filter1)
cv2.imshow('gurultulu goruntu',noise_img)
cv2.imshow('gaussian filter',img_gaussian)
cv2.imshow('bilateral filter',img_bilateral)
cv2.imshow('medyan filter',median)
cv2.imshow('mean filter',mean_image)
cv2.waitKey(0)
