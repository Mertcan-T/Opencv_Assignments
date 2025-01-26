#video çekme

import cv2
cam=cv2.VideoCapture(0)

fourcc=cv2.VideoWriter_fourcc(*'XVID')

out = cv2.VideoWriter("kayit.avi",fourcc,30,(640,480))

while cam.isOpened:
    
    ret,frame=cam.read()

    out.write(frame)

    cv2.imshow("kamera",frame)

    if cv2.waitKey(1) == ord("q"):
        print("video kapatıldı")
        break

cam.release()
out.release()
cv2.destroyAllWindows()