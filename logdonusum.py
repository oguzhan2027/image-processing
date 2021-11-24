import cv2
import numpy as np
from matplotlib import pyplot as plt
image1=cv2.imread('orangutan.jpg')
cv2.imshow("original",image1)
c=144
#c=255/np.log(1+np.max(image1))
log_image=c+np.log(1+image1)
log_image =np.array(log_image,dtype=np.uint8)
cv2.imshow("logartimik donusum",log_image)
log_image=255/(c+np.log(1+image1))
log_image=np.array(log_image,dtype=np.uint8)
cv2.imshow("logartimik donusum_255",log_image)
cv2.waitKey()
