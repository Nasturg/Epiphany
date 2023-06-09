# Открытие нужное изображения, а так же чтения данных с камеры в
# реальном масштабе времени

import cv2

# import numpy as np

'''
img = cv2.imread('image/OpenCV.png', -1) # выбор картиники с которой будем работать
# 1 - цветное чтение, 0 - черно-белое, -1 - альфа канал

cv2.namedWindow("image_logo", cv2.WINDOW_NORMAL) # Настрой ка открываемого окна с изображение
cv2.imshow("image_logo", img) # Вывод изображение в окно
cv2.waitKey(0) # Ожидание события нажатия кнопки бесконечность плюс
cv2.destroyAllWindows() # Закрыть все окна
'''

cap = cv2.VideoCapture(cv2.CAP_DSHOW, 0)  # Считывание видео потока с веб-камеры ноута
# Можно вместо "0" ввести название видео с расширением
# "0" - номер камеры. Обычно нулевая камера это ветка ноута

# Цикл обработки потока изображений в реальном масштабе времени
while True:
    ret, frame = cap.read()  # Считывание изображения по кадрово
    # ret - возвращает значение истины или лжи, есть поток изображений
    # frame - изображение
    cv2.imshow('video', frame)  # Вывод видео в реальном масштабе времени
    if cv2.waitKey(1) & 0xFF == ord('q'):
        # cv2.waitKey(0) - бесконечно ожидание нажатия кнопки
        # cv2.waitKey(1) - ожидание нажатия кнопки в течение 1 мили секунд
        break

cap.release()
cv2.destroyAllWindows()
