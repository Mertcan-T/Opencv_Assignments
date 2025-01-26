import cv2
import numpy as np

resim =np.zeros((512,512,3),np.uint8)
resim2 =np.ones((512,512,3),np.uint8)

resim[:]=255,0,0 #mavi boş ekran

cv2.imshow("siyahbos",resim)
cv2.imshow("siyahbos2",resim2)
cv2.waitKey(0)
cv2.destroyAllWindows()