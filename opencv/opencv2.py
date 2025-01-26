import cv2
import numpy as np
resim = cv2.imread("C:\\Users\\M.T\\Desktop\\calismalarim\\opencv\\kopke.jpeg")
resim2= cv2.cvtColor(resim,cv2.COLOR_BGR2GRAY)
bugu=cv2.GaussianBlur(resim,(5,5),2)
cizim=cv2.Canny(resim,250,250)

cv2.imshow("images",resim)
cv2.imshow("images2",resim2)
cv2.imshow("images3",bugu)
cv2.imshow("images4",cizim)

cv2.waitKey(0)
cv2.destroyAllWindows()