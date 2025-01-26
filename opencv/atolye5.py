import cv2
import numpy as np

resim =np.zeros((512,512,3),np.uint8)

cv2.imshow("resim",resim)
cv2.line(resim,(0,0),(511,511),(0,0,255),2)
cv2.rectangle(resim,(250,250),(350,350),(0,255,255),2)
cv2.rectangle(resim,(150,150),(250,250),(255,0,255),-1)
cv2.circle(resim,(387,387),50,(255,0,0),2)
cv2.putText(resim,"Believe",(150,145),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),1)
cv2.putText(resim,"kare",(270,305),cv2.FONT_HERSHEY_COMPLEX,0.8,(100,100,100),1)
cv2.imshow("resim",resim)

cv2.waitKey(0)
cv2.destroyAllWindows()