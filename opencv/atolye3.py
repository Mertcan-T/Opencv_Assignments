import cv2
import numpy as np
import cv2
import numpy as np
import matplotlib.pyplot as plt

resim = cv2.imread("C:\\Users\\M.T\\Desktop\\calismalarim\\opencv\\kopke.jpeg",0)
resim2 = cv2.imread("C:\\Users\\M.T\\Desktop\\calismalarim\\opencv\\kopke.jpeg")
cv2.imshow("paint",resim)
cv2.imshow("paint2",resim2)

while(1):
     if cv2.waitKey(1)& 0xFF==ord("q"):
         cv2.destroyWindow("paint")
         continue
     elif cv2.waitKey(1)& 0xFF==ord("w"):
         cv2.destroyWindow("paint2")
         continue
     elif cv2.waitKey(1)& 0xFF==ord("s"):
         cv2.imwrite("resim3.jpeg",resim)
         continue
     elif cv2.waitKey(1)& 0xFF==ord("m"):
         break

cv2.destroyAllWindows()

# import cv2

# image = cv2.imread("C:\\Users\\M.T\\Desktop\\calismalarim\\opencv\\kopke.jpeg")
# gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  
# cv2.imshow("Normal Görüntü", image)
# cv2.imshow("Gri Görüntü", gray_image)

# key = cv2.waitKey(0) & 0xFF
# if key == ord('q'):  
#     cv2.destroyWindow("Normal Görüntü")
# elif key == ord('w'):  
#     cv2.destroyWindow("Gri Görüntü")
# elif key == ord('s'): 
#     cv2.imwrite("renkli_goruntu.jpg", image)
#     cv2.imwrite("gri_goruntu.jpg", gray_image)
#     print("Görüntüler kaydedildi!")

# key = cv2.waitKey(0) & 0xFF
# if key == ord('q'):  
#     cv2.destroyWindow("Normal Görüntü")
# elif key == ord('w'): 
#     cv2.destroyWindow("Gri Görüntü")
# elif key == ord('s'): 
#     cv2.imwrite("renkli_goruntu.jpg", image)
#     cv2.imwrite("gri_goruntu.jpg", gray_image)
#     print("Görüntüler kaydedildi!")

# cv2.destroyAllWindows()

