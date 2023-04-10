'''
Поиск углов объекта

Посик углов объекта прямоугольника в библиотеке OpenCV на Python
можно использовать функцию cv2.minAreaRect() для определения минимульной
ограничивающей прямоугольной оласти вокруг объекта, а затем
использовать функцию cv2.boxPoints() для получения координат углов этого
прямоугольника

'''
# ee

import cv2
import numpy as np

# функция обратного вызова
def on_trackbgar(x):
    pass

#img = cv2.imread('image/Test1.png')  # чтение картинки

cap = cv2.VideoCapture(0)  # Считывание видео потока с веб камеры ноута

cv2.namedWindow('image')

cv2.createTrackbar('Lower', 'image', 0, 255, on_trackbar) # Отрисовка ползунков
cv2.createTrackbar('Upper', 'image', 0, 255, on_trackbar) # Отрисовка ползунков

while True:

    ret, frame = cap.read() # Считываение изображения по кадрово
    # ret - возращает значение истины или лжи, есть поток изображений
    # frame - изображение

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) # преобразует исходное цветное изображение
    # (в формате BGR) в черно-белое (градации серого)
    # Функция cv2.cvtColor() используется для изменения цветовой модели изображения
    # константу cv2.COLOR_BGR2GRAY для преобразования в градации серого

    # получем текущие значение ползунка
    lower_val = cv2.getTrackbarPos('Lower', 'image')
    upper_val = cv2.getTrackbarPos('Upper', 'image')

    edges = cv2.Canny(gray, lower_val, upper_val) # оздает изображение, на котором выделены контуры объектов
    # функция cv2.Canny(), которая находит границы объектов на изображении с помощью алгоритма Canny
    # Первый аргумент функции - это исходное изображение в градациях серого
    # второй и третий аргументы определяют пороги, при которых будут определены границы объектов


    countours, hierarchy = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    # находит контуры объектов на изображении, которое было создано с помощью функции cv2.Canny()
    # Первый аргумент edges - это изображение с границами объектов
    # второй аргумент cv2.RETR_EXTERNAL указывает, что нужно найти только внешние контуры объектов
    # третий аргумент cv2.CHAIN_APPROX_SIMPLE определяет метод упрощения контуров

    # Результатом работы функции являются массивы contours и hierarchy,
    # которые содержат координаты точек,
    # образующих контуры объектов, и информацию о вложенных контурах.

    # Перебирает все найденые контуры
    for countour in countours:
        rect = cv2.minAreaRect(countour) # находит ограничивающий прямоугольник (bounding box) для контура
        # граничивающий прямоугольник - это прямоугольник минимальной площади,
        # который полностью охватывает контур
        # возвращает объект типа Rect, который содержит информацию о координатах и размерах
        # ограничивающего прямоугольника
        box = cv2.boxPoints(rect) # преобразует объект Rect, полученный из функции
        # cv2.minAreaRect(), в массив из четырех точек (координат углов)
        box = np.intp(box) # реобразует массив координат углов
        # ограничивающего прямоугольника в целочисленный тип данных
        cv2.drawContours(frame, [box], 0, (0, 0, 255), 2) # рисует контур на изображении "frame"
        # вокруг прямоугольника, ограничивающего объект на изображении

    cv2.imshow('image', frame) # Вывод изображения


    if cv2.waitKey(1) & 0xFF == ord('q'):
        # cv2.waitKey(0) - бесконечное ожидание нажатия кнопки
        # cv2.waitKey(1) - ожидание нажатия кнопки в течение 1 мили секунд
        break

cap.release()
cv2.destroyAllWindows()
