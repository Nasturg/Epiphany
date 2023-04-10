# Градиенты и края

import cv2
import numpy as np

def on_trackbar(x):
    pass

cap = cv2.VideoCapture(0)
cv2.namedWindow('frame')

cv2.createTrackbar('Lower', 'frame', 0, 255, on_trackbar) # Отрисовка ползунков
cv2.createTrackbar('Upper', 'frame', 0, 255, on_trackbar) # Отрисовка ползунков


while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) # Изображение в ч\б

    framex = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize = 5)  # создание градиента по x
    # cv2.CV_64F = размер изображения с которым будет работать
    framey = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize = 5) # создание градиента по y


    # получем текущие значение ползунка
    lower_val = cv2.getTrackbarPos('Lower', 'frame')
    upper_val = cv2.getTrackbarPos('Upper', 'frame')

    edge = cv2.Canny(gray, lower_val, upper_val)

    cv2.imshow('frame', frame)
    cv2.imshow('x', framex)
    cv2.imshow('y', framey)
    cv2.imshow('edge', edge)

    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()