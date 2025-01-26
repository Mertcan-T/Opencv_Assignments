import cv2
import numpy as np

cam = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter("kayit3.mp4", fourcc, 30, (640, 480))

def nothing(x):
    pass

cv2.namedWindow("frame")
cv2.createTrackbar("H1", "frame", 0, 179, nothing)
cv2.createTrackbar("H2", "frame", 0, 179, nothing)
cv2.createTrackbar("S1", "frame", 0, 255, nothing)
cv2.createTrackbar("S2", "frame", 0, 255, nothing)
cv2.createTrackbar("V1", "frame", 0, 255, nothing)
cv2.createTrackbar("V2", "frame", 0, 255, nothing)

while cam.isOpened():
    _, frame = cam.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    H1 = int(cv2.getTrackbarPos("H1", "frame") / 2)
    H2 = int(cv2.getTrackbarPos("H2", "frame") / 2)
    S1 = cv2.getTrackbarPos("S1", "frame")
    S2 = cv2.getTrackbarPos("S2", "frame")
    V1 = cv2.getTrackbarPos("V1", "frame")
    V2 = cv2.getTrackbarPos("V2", "frame")

    lower = np.array([H1, S1, V1])
    upper = np.array([H2, S2, V2])

    mask = cv2.inRange(hsv, lower, upper)

    res = cv2.bitwise_and(frame, frame, mask=mask)

    contours1, hierarchy1 = cv2.findContours(mask.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    for c in contours1:
        x, y, w, h = cv2.boundingRect(c)
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)  # Yeşil renk

    out.write(frame)

    cv2.imshow("frame", frame)
    cv2.imshow("counters", res)
    cv2.imshow("hsv", mask)

    if cv2.waitKey(1) == ord("q"):
        break

cam.release()
out.release()
cv2.destroyAllWindows()
