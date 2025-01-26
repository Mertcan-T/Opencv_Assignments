import cv2
import numpy as np

sifir = np.zeros([100,100])
bir=np.ones([100,100])

cv2.imshow("sifir",sifir)
cv2.imshow("bir",bir)

cv2.waitKey(0)
cv2.destroyAllWindows()