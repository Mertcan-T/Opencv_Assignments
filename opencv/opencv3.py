import cv2
import matplotlib.pyplot as plt

resim = cv2.imread("C:\\Users\\M.T\\Desktop\\calismalarim\\opencv\\kopke.jpeg")
plt.imshow(resim)
plt.show()

kes=resim[49:165,216:300]
kes2=cv2.resize(kes,(resim.shape[1],resim.shape[0]))

cv2.imshow("images",resim)
cv2.imshow("images2",kes)
cv2.imshow("images2",kes2)

cv2.waitKey(0)
cv2.destroyAllWindows()
