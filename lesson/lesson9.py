import cv2
import numpy as np
import time

def nothing(x):
    pass

kernel = np.ones((5, 5), np.uint8)

cap = cv2.VideoCapture(0)

cv2.namedWindow('track', cv2.WINDOW_NORMAL)

cv2.createTrackbar('H', 'track', 0, 180, nothing)
cv2.createTrackbar('S', 'track', 0, 255, nothing)
cv2.createTrackbar('V', 'track', 0, 255, nothing)

cv2.createTrackbar('HL', 'track', 0, 180, nothing)
cv2.createTrackbar('SL', 'track', 0, 255, nothing)
cv2.createTrackbar('VL', 'track', 0, 255, nothing)

while True:
    ret, frame = cap.read()

    frame = cv2.bilateralFilter(frame, 9, 75, 75)

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    h = cv2.getTrackbarPos('H', 'track')
    s = cv2.getTrackbarPos('S', 'track')
    v = cv2.getTrackbarPos('V', 'track')

    hl = cv2.getTrackbarPos('HL', 'track')
    sl = cv2.getTrackbarPos('SL', 'track')
    vl = cv2.getTrackbarPos('VL', 'track')

    lower = np.array([hl, sl, vl])
    upper = np.array([h, s, v])
    mask = cv2.inRange(hsv, lower, upper)
    res = cv2.bitwise_and(frame, frame, mask=mask)
    opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
    closing = cv2.morphologyEx(opening, cv2.MORPH_CLOSE, kernel)

    contours, h = cv2.findContours(closing, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    contours = sorted(contours, key=cv2.contourArea, reverse=True)

    for x in range(len(contours)):
        area = cv2.contourArea(contours[x])
        if area > 300:
            x, y, w, h = cv2.boundingRect(contours[x])
            frame = cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
            frame = cv2.rectangle(frame, (x, y), (x + 60, y - 25), (0, 0, 0), -1)

            frame = cv2.circle(frame, (x + (x // 2), y + (h // 2)), 20, (0, 255, 0), -1)
            print('x: ', x + (x // 2), y + (h // 2))

            cv2.putText(frame, 'Some', (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (255, 255, 255), 2)

    cv2.imshow('mask', mask)
    cv2.imshow('close', closing)
    cv2.imshow('frame', frame)

    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()

