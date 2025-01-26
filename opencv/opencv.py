# # import cv2
# # resim=cv2.imread("kopke.jpeg")
# # if resim is None:
# #     print("Resim yüklenemedi, dosya yolunu kontrol edin.")
# # cv2.imshow("kopke",resim)
# # cv2.waitKey(0)
# # cv2.destroyAllWindows()
# import os
# import cv2

# # Resmin tam yolunu belirtin
# resim_path = "cocukvebalon.jpg"

# # Dosya yolunun doğru olduğundan emin olun
# if not os.path.isfile(resim_path):
#     print(f"Dosya bulunamadı: {resim_path}")
# else:
#     resim = cv2.imread(resim_path)
#     if resim is None:
#         print("Resim yüklenemedi.")
#     else:
#         cv2.imshow("kopke", resim)
#         cv2.waitKey(0)
#         cv2.destroyAllWindows()

import cv2
cam=cv2.VideoCapture(0)
while cam.isOpened:
    ret,frame=cam.read()
    if not ret:
        print("kamerada görüntü oluşmuyor.")
        break
    cv2.imshow("goruntu",frame)
    if cv2.waitKey(1) & 0xFF==ord("q"):
        print("video kapatıldı.")
        break
cam.release()
cv2.destroyAllWindows()