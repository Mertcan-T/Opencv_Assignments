import cv2
import numpy as np
import matplotlib.pyplot as plt

resim = cv2.imread("C:\\Users\\M.T\\Desktop\\calismalarim\\opencv\\kopke.jpeg")
resim2 = cv2.imread("C:\\Users\\M.T\\Desktop\\calismalarim\\opencv\\kopke.jpeg",0)
gray_image = cv2.cvtColor(resim, cv2.COLOR_BGR2GRAY)

plt.subplot(121)
plt.imshow(resim)
plt.subplot(122)
plt.imshow(gray_image)
plt.show()

cv2.imshow("paint",resim)
cv2.imshow("paint2",resim2)
cv2.waitKey(0)

cv2.destroyAllWindows()
