import cv2
import numpy as np

enlem=640
boylam=480

cam=cv2.VideoCapture(0)
cam.set(3,enlem)
cam.set(4,boylam)

def empty(a):
    pass

cv2.namedWindow("HSV")
cv2.resizeWindow("HSV",640,240)
cv2.createTrackbar("HUE Min","HSV",0,179,empty)
cv2.createTrackbar("HUE Max","HSV",0,179,empty)
cv2.createTrackbar("SAT Min","HSV",0,255,empty)
cv2.createTrackbar("SAT Max","HSV",0,255,empty)
cv2.createTrackbar("Value Min","HSV",0,255,empty)
cv2.createTrackbar("Value Max","HSV",0,255,empty)



while cam.isOpened:
    ret,frame=cam.read()
    resimHsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

    h_min=cv2.getTrackbarPos("HUE Min","HSV")
    h_max=cv2.getTrackbarPos("HUE Max","HSV")
    s_min=cv2.getTrackbarPos("SAT Min","HSV")
    s_max=cv2.getTrackbarPos("SAT Max","HSV")
    v_min=cv2.getTrackbarPos("Value Min","HSV")
    v_max=cv2.getTrackbarPos("Value Max","HSV")

    lower=np.array([h_min,s_min,v_min])
    upper=np.array([h_max,s_max,v_max])
    mask=cv2.inRange(frame,lower,upper)
    result=cv2.bitwise_and(frame,frame,mask=mask)

    cv2.imshow("kamera",frame)
    cv2.imshow("Hsv image",resimHsv)
    cv2.imshow("mask",mask)
    cv2.imshow("result",result)
    if cv2.waitKey(1)& 0xFF==ord("q"):
        break
cam.release
cv2.destroyAllWindows()