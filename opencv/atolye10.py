import cv2
import numpy as np

resim = cv2.imread("C:\\Users\\M.T\\Desktop\\calismalarim\\opencv\\kopke.jpeg")

print(resim.shape)

rows,cols=resim.shape[:2]

rot_matrix=cv2.getRotationMatrix2D((cols/2,rows/2),45,1)
rot_matrix2=cv2.getRotationMatrix2D((cols/2,rows/2),90,1)
img_rotation=cv2.warpAffine(resim,rot_matrix,(cols,rows))
img_rotation2=cv2.warpAffine(resim,rot_matrix,(cols,rows))

cv2.imshow("resim",resim)
cv2.imshow("resim2",img_rotation)
cv2.imshow("resim3",img_rotation2)
cv2.waitKey(0)
cv2.destroyAllWindows()