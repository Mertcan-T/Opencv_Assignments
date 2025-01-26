import cv2
import numpy as np

resim = cv2.imread("C:\\Users\\M.T\\Desktop\\calismalarim\\opencv\\kopke.jpeg")

hsv=cv2.cvtColor(resim,cv2.COLOR_BGR2HSV)
lower = np.array([50,50,150])
upper = np.array([255,255,250])
mask=cv2.inRange(hsv,lower,upper)

res=cv2.bitwise_and(resim,resim,mask=mask)
while(1):
     cv2.imshow("paint",res)
     if cv2.waitKey(1)& 0xFF==ord("q"):
         break

cv2.destroyAllWindows()