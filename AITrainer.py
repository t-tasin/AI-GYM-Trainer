import cv2
import numpy as np
import time
import PoseDetector as pd

cap = cv2.VideoCapture(0)
detector = pd.poseDetector()
count = 0
direction = 0

while True:
    success, img = cap.read()
#    img = cv2.imread("Push_Ups.png")
    img = detector.findPose(img, False)
    lmlist = detector.findPosition(img, False)
#    print(lmlist)

    if len(lmlist) != 0:
        angle = detector.findAngle(img, 11, 13, 15)
        per = np.interp(angle, (200, 270), (0, 100))

        if per == 100:
            if direction == 0:
                count += 0.5
                direction = 1
        if per == 0:
            if direction == 1:
                count += 0.5
                direction = 0

        print(count)

        cv2.putText(img, f'{count}', (50,100), cv2.FONT_HERSHEY_PLAIN, 5, (255, 0, 0), 5)

    cv2.imshow("Video", img)
    cv2.waitKey(1)