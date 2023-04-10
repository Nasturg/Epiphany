# Отрисовка ползунков

import cv2
import numpy as np

def nothing(x):
    pass

img = np.zeros((300, 300, 3), np.uint8)

cv2.namedWindow('image')

cv2.createTrackbar('R', 'image', 0, 255, nothing) # Отрисовка ползунков
# name - название ползунка
# window - окно,  к которому будет прикреплен ползунок
# x - начальное значение
# y - конечное значение
# func - функция, котрая вызывается при изменении ползунка
cv2.createTrackbar('G', 'image', 0, 255, nothing)
cv2.createTrackbar('B', 'image', 0, 255, nothing)

while True:
    cv2.imshow('image', img)

    k = cv2.waitKey(1) & 0xFF
    if k == 27: # выход по esc
        break

    r = cv2.getTrackbarPos('R', 'image')
    g = cv2.getTrackbarPos('G', 'image')
    b = cv2.getTrackbarPos('B', 'image')

    img[:] = [b, g, r]

