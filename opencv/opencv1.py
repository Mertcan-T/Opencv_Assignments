import cv2

# #resim2=cv2.imread("C:\\Users\\M.T\\Desktop\\dataset\\balon\\6640161695.webp")
# resim = cv2.imread("C:\\Users\\M.T\\Desktop\\calismalarim\\opencv\\kopke.jpeg",0)
# if resim is None:
#     print("Resim yüklenemedi, dosya yolunu kontrol edin.")
# cv2.imwrite("grikopke.jpg",resim)
# cv2.imshow("images",resim)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# cam=cv2.VideoCapture(0)

# while True:
#     ret,frame = cam.read()
#     cv2.imshow("goruntu",frame)

#     if cv2.waitKey(1)& 0xFF==ord("q"):
#         print("Kamera kapatıldı")
#         break
# cam.release()
# cv2.destroyAllWindows()

cv2.namedWindow("resim",cv2.WINDOW_NORMAL)