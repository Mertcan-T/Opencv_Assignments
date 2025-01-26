import cv2
import numpy as np

img = np.zeros((512,512,3),np.uint8)

cv2.putText(img,"OpenCV",(200,255),cv2.FONT_HERSHEY_TRIPLEX,1,(0,0,255),1,cv2.LINE_AA)

cv2.imshow("YAZI",img)

cv2.waitKey(0)
cv2.destroyAllWindows()