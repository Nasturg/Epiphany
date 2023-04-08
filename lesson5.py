import cv2
import numpy as np

cap = cv2.VideoCapture(0)
cv2.namedWindow('frame')

while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) # Изображение в ч\б

    framex = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize = 5)  # создание градиента по x
    # cv2.CV_64F = размер изображения с которым будет работать
    framey = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize = 5) # создание градиента по y

    cv2.imshow('frame', frame)
    cv2.imshow('x', framex)
    cv2.imshow('y', framey)

    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()