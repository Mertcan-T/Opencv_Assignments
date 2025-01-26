#bir tuşa basınca kapanan resim uygulaması
import cv2
import numpy as np
resim = cv2.imread("C:\\Users\\M.T\\Desktop\\calismalarim\\opencv\\kopke.jpeg")


while(1):
     cv2.imshow("paint",resim)
     if cv2.waitKey(1)& 0xFF==ord("q"):
         break

cv2.destroyAllWindows()


