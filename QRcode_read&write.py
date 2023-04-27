import cv2
import os

# import qrcode
# import numpy as np

'''
Создание qr-кодов.
Чтение qr-кодов и их последующая запись, по указанному пути,
заданного размера 75 х 75 пикселей.
'''

path = 'image/'
path_qr = 'image/qr/'
path_qr_clean = 'image/qr_clean/'

qr_create = 'ya.png'
qr_format = 'png'
qr_format_old = 'jpg'

color = (255, 255, 255)  # Белый цвет в формате BGR
thickness = 0  # Толщина рамки в пикселях
border_size = 2  # Размер рамки в пикселях

'''
# Генерация QR кода
qr = qrcode.QRCode(
    version=2,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)

qr.add_data('white, white, yellow')  # информация в qr коде
qr.make(fit=True)

img = qr.make_image(fill_color='black', back_color='white')  # Отрисовка qr кода
img.save(path + qr_create, qr_format)
'''

# Количество изображений
num_images = len([f for f in os.listdir(path_qr) if f.endswith(qr_format_old)])

print(num_images)

for i in range(num_images):  # Чтение QR кода

    img_qrcode = cv2.imread(path_qr + str(i + 1) + '.' + qr_format_old)
    print(path_qr + str(i + 1) + '.' + qr_format_old)
    detector = cv2.QRCodeDetector()

    data, bbox, clear_qrcode = detector.detectAndDecode(img_qrcode)

    # '''
    if i < 11:
        # Добавление рамки к изображению
        img_with_border = cv2.copyMakeBorder(clear_qrcode, border_size, border_size, border_size, border_size,
                                             cv2.BORDER_CONSTANT, value=color)

        # Определение координат рамки
        x1, y1 = border_size - 1, border_size - 1  # Верхний левый угол
        x2, y2 = clear_qrcode.shape[1] + border_size, clear_qrcode.shape[
            0] + border_size  # Нижний правый угол

        # Добавление рамки к изображению
        img_with_border = cv2.rectangle(img_with_border, (x1, y1), (x2, y2), color, thickness)

        clear_qrcode = img_with_border
    # '''

    # cv2.imshow('frame', clear_qrcode)

    # увеличиваем размер изображения в два раза
    new_size = (clear_qrcode.shape[1] * 3, clear_qrcode.shape[0] * 3)
    # Увеличение
    resized_img = cv2.resize(clear_qrcode, new_size, interpolation=cv2.INTER_NEAREST)
    # resized_img = cv2.resize(resized, (75, 75))

    cv2.imwrite(path_qr_clean + str(i + 1) + '.' + qr_format, resized_img)
    print(path_qr_clean + str(i + 1) + '.' + qr_format)

    # print(data)
    # print(bbox)

cv2.waitKey(0)
