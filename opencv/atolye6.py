import cv2
import numpy as np
#cvto.flip

cam=cv2.VideoCapture(0)

while cam.isOpened:
    ret,frame = cam.read()
    cv2.imshow("cam",frame)

    cam2=cv2.flip(frame,1)
    cv2.imshow("cam2",cam2)

    if cv2.waitKey(1)& 0xFF==ord("q"):
        break
cam.release
cv2.destroyAllWindows()
