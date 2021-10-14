from LaneDetectionModule import *
from objdetector import *


vid = cv2.VideoCapture('vid1.mp4')
vid.set(3, 640)
vid.set(4, 480)

cap = cv2.VideoCapture('vid1.mp4')
intialTracbarVals = [102, 80, 20, 214]
Utlis.initializeTrackbars(intialTracbarVals)
frameCounter = 0

while True:
    frameCounter += 1
    if cap.get(cv2.CAP_PROP_FRAME_COUNT) == frameCounter:
        cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
        frameCounter = 0
    success, img = cap.read()
    img = cv2.resize(img, (480, 240))
    getLaneCurve(img)
    curve = getLaneCurve(img, display=1)
    print(curve)
    success, img = vid.read()
    result, objectInfo = getObjects(img)
    # print(objectInfo)
    cv2.imshow("Output", img)
    #cv2.waitKey(1)
    # cv2.imshow('vid',img)
    cv2.waitKey(1)

    #
    #
    # vid = cv2.VideoCapture(0)
    # vid.set(3, 640)
    # vid.set(4, 480)
    # # cap.set(10, 70)
    # while True:
    #     success, img = vid.read()
    #     result, objectInfo = getObjects(img)
    #     # print(objectInfo)
    #     cv2.imshow("Output", img)
    #     cv2.waitKey(1)