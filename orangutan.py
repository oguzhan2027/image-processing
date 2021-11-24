import cv2
import numpy as np

foto = cv2.imread("orangutan.jpg")
cv2.imshow("orangutan",foto)
cv2.waitKey()
B = foto [:,:,0]
G = foto [:,:,1]
R = foto [:,:,2]
cv2.imshow("Mavi",B)
cv2.imshow("Yesil",G)
cv2.imshow("Kirmizi",R)
cv2.waitKey()
print(foto.shape)
print(R.shape)

x=1
y=0
kanal=0
yogunluk_rgb = foto [y, x, kanal]
print("yogunluk:",yogunluk_rgb)

yogunluk_r= R[y,x]
print("yogunluk_gray :",yogunluk_r)

yogunluk_r= R [y,x]
print("yogunluk_gray : ",yogunluk_r)

maksimum_yogunluk = np.max(B)
minimum_yogunluk = np.min(B)
print("maksimum yogunluk :",maksimum_yogunluk)
print("minimum yogunluk :",minimum_yogunluk)