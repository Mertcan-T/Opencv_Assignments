import cv2
import numpy as np

cv2.namedWindow("cam",cv2.WINDOW_NORMAL)
cam=cv2.VideoCapture(0)
while cam.isOpened():
    ret,frame=cam.read()
    frame2=cv2.resize(frame,(512,512))
    
    cv2.line(frame2,(0,0),(511,511),(0,0,255),2)
    cv2.rectangle(frame2,(250,250),(350,350),(0,255,255),2)
    cv2.rectangle(frame2,(150,150),(250,250),(255,0,255),-1)
    cv2.circle(frame2,(387,387),50,(255,0,0),2)
    cv2.putText(frame2,"Believe",(150,145),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),1)
    cv2.putText(frame2,"kare",(270,305),cv2.FONT_HERSHEY_COMPLEX,0.8,(100,100,100),1)
    cv2.imshow("cam",frame2)
    if cv2.waitKey(1)& 0xFF==ord("q"):
        break
cam.release
cv2.destroyAllWindows()