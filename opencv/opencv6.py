import cv2
import numpy as np

resim =np.zeros((512,512,3),np.uint8)

cv2.line(resim,(0,0),(511,511),(0,0,255),3)
cv2.rectangle(resim,(110,110),(210,210),(255,50,200),2)
cv2.rectangle(resim,(210,210),(310,310),(0,255,0),-1)
cv2.circle(resim,(360,360),70,(255,0,0),3)
cv2.putText(resim,"Believe",(110,100),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),1)

cv2.imshow("siyahbos",resim)

cv2.waitKey(0)
cv2.destroyAllWindows()