import cv2
'''
# загрузка изображений
img = cv2.imread('../image/win.png')
pattern = cv2.imread('../image/win2.png')

# преобразование в оттенки серого
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray_pattern = cv2.cvtColor(pattern, cv2.COLOR_BGR2GRAY)

# поиск паттерна в изображении
result = cv2.matchTemplate(gray_img, gray_pattern, cv2.TM_CCOEFF_NORMED)

# получение координат паттерна на изображении
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
top_left = max_loc
bottom_right = (top_left[0] + pattern.shape[1], top_left[1] + pattern.shape[0])

# выделение рамкой паттерна на изображении
cv2.rectangle(img, top_left, bottom_right, (0, 255, 0), 2)

# отображение результата
cv2.imshow('Result', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
'''

# загрузка изображения
img = cv2.imread('image/Test1.png', 0)

# бинаризация изображения
ret, thresh = cv2.threshold(img, 127, 255, 0)

# поиск объектов
num_labels, labels = cv2.connectedComponents(thresh)

# конвертация типа данных изображения
labels = cv2.convertScaleAbs(labels)

# отображение меток объектов
cv2.imshow('Labels', labels)

cv2.waitKey(0)
cv2.destroyAllWindows()

# ddd/
