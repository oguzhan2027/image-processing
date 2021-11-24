import cv2
import numpy as np
from matplotlib import pyplot as plt

renkli = cv2.imread("orangutan.jpg")
gri = cv2.imread("orangutan.jpg",0)

hist_color = cv2.calcHist([renkli], [0],None,[256],[0,256])#renkli görüntü

hist_gray = cv2.calcHist([gri], [0],None,[256],[0,256])#gri görüntü


plt.figure(2)
plt.plot(hist_gray)

B = renkli[:,:,0]
hist_B = cv2.calcHist([B], [0],None,[256],[0,256])

print(np.sum(hist_B))

plt.figure(3)
plt.hist(gri.ravel(),256,[0,256])
# plt.show()

# plt.figure(3)
# plt.hist(gri.ravel(),bins=256,cumulative=True)
# plt.xlabel('Intensty Value')
# plt.ylabel('Count')
# plt.show()

a=np.histogram(gri,256,[0,256])
print(a[0])
print(np.sum(a[0]))
plt.figure(1)
plt.plot(a[0])
plt.show()
