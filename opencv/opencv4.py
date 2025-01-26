import cv2
import numpy as np
import matplotlib.pyplot as plt

resim = cv2.imread("C:\\Users\\M.T\\Desktop\\calismalarim\\opencv\\kopke.jpeg")
resim2= cv2.cvtColor(resim,cv2.COLOR_BGR2GRAY)
bugu=cv2.GaussianBlur(resim,(5,5),2)
cizim=cv2.Canny(resim,250,250)

yatay=np.hstack((resim,bugu))
dikey=np.vstack((resim,bugu))

cv2.imshow("dikey",dikey)
cv2.imshow("yatay",yatay)

plt.subplot(1,4,1)
plt.imshow(resim)
plt.subplot(1,4,2)
plt.imshow(resim2)
plt.subplot(1,4,3)
plt.imshow(bugu)
plt.subplot(1,4,4)
plt.imshow(cizim)
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()