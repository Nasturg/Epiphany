# Цветовое пространство

import cv2
import numpy as np

def nothing(x):
    pass

cap = cv2.VideoCapture(0)
cv2.namedWindow('frame')

# Генерация ползунков для управления
cv2.createTrackbar('HL', 'frame', 0, 180, nothing)
cv2.createTrackbar('SL', 'frame', 0, 255, nothing)
cv2.createTrackbar('VL', 'frame', 0, 255, nothing)

cv2.createTrackbar('H', 'frame', 0, 180, nothing)
cv2.createTrackbar('S', 'frame', 0, 255, nothing)
cv2.createTrackbar('V', 'frame', 0, 255, nothing)

while True:
    ret, frame = cap.read()

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV) # Изменение цветового
    # отображения с rgb на hsv

    # Переменные считывающие значения ползунков
    hl = cv2.getTrackbarPos('HL', 'frame')
    sl = cv2.getTrackbarPos('SL', 'frame')
    vl = cv2.getTrackbarPos('VL', 'frame')

    h = cv2.getTrackbarPos('H', 'frame')
    s = cv2.getTrackbarPos('S', 'frame')
    v = cv2.getTrackbarPos('V', 'frame')

    # Создание массивов с диапозоном данных с ползунков
    lower = np.array([hl, sl, vl])
    upper = np.array([h, s, v])

    # Создание маски, то есть фильтрации пикселей находящихся в диапозоне
    mask = cv2.inRange(hsv, lower, upper)

    res = cv2.bitwise_or(frame, frame, mask = mask)

    # Вывод видео
    cv2.imshow('frame', frame)
    cv2.imshow('mask', mask)
    cv2.imshow('resultion', res)

    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()