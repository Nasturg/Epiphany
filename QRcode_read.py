import cv2
import os

# import qrcode
# import numpy as np

path = 'image/'
path_qr = 'image/qr/'
path_qr_clean = 'image/qr_clean/'

qr_create = 'ya.png'
qr_format = 'png'
qr_format_old = 'jpg'

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

    # cv2.imshow('frame', clear_qrcode)

    cv2.imwrite(path_qr_clean + str(i + 1) + '.' + qr_format, clear_qrcode)
    print(path_qr_clean + str(i + 1) + '.' + qr_format)

    # print(data)
    # print(bbox)

cv2.waitKey(0)
