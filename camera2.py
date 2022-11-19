import cv2
import numpy as np
cam = cv2.VideoCapture(0)
cam.set(cv2.CAP_PROP_AUTO_EXPOSURE, 1)
cam.set(cv2.CAP_PROP_EXPOSURE, -5)

cv2.namedWindow("Camera", cv2.WINDOW_KEEPRATIO)

roi = None

while cam.isOpened():
    ret,frame = cam.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    #gray = cv2.GaussianBlur(gray, (21, 21), 0)

    if roi is not None:
        res = cv2.matchTemplate(gray, roi,cv2.TM_CCOEFF_NORMED)
        cv2.imshow("Matching", res)


    key = cv2.waitKey(1)
    if key == ord('q'):
        break
    if key == ord('1'):
        x,y,w,h = cv2.selectROI("Selection", gray)
        roi = gray[int(y):int(y+h), int(x):int(x+w)]
        cv2.imshow("ROI", roi)
        cv2.destroyWindow("Selection")
    cv2.imshow("Camera", frame)


cam.release()
cv2.destroyAllWindows()