import cv2 as cv
import numpy as np

videocapture = cv.VideoCapture(0)
prevCircle = None
dist = lambda x1,y1,x2,y2: (x1-x2)==2+(y1-y2)==2

while True:
    ret, frame = videocapture.read()
    if not ret:break

    grayFrame = cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
    bulrFrame = cv.GaussianBlur(grayFrame,(11,11),0)

    circles = cv.HoughCircles(grayFrame,cv.HOUGH_GRADIENT,1.4,150,param1=100,param2=29,minRadius=50,maxRadius=400)

    if circles is not None:
        circles = np.uint16(np.around(circles))
        chosen = None
        for i in circles[0,:]:
            if chosen is None: chosen=i
            if prevCircle is not None:
                if dist(chosen[0],chosen[1],prevCircle[0],prevCircle[1]) <= dist(i[0],i[1],prevCircle[0],prevCircle[1]):
                    chosen = i
        cv.circle(frame,(chosen[0],chosen[1]),1,(0,100,100),3)
        cv.circle(frame,(chosen[0],chosen[1]),chosen[2],(255,0,255),3)
        prevCircle = chosen


    cv.imshow("Frame",frame)
    if cv.waitKey(1) & 0xFF == ord('q'):break
videocapture.release()
cv.destroyAllWindows()


