import cv2
import qrcode
# import numpy as np

# Генерация QR кода
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)

qr.add_data('Robotics_Rob')  # информация в qr коде
qr.make(fit=True)

img = qr.make_image(fill_color='black', back_color='white')  # Отрисовка qr кода
img.save('image/QRtest.jpeg', 'JPEG')

# Чтение QR кода

img_qrcode = cv2.imread('image/win2.png')
detector = cv2.QRCodeDetector()

data, bbox, clear_qrcode = detector.detectAndDecode(img_qrcode)

print(data)
print(bbox)

# cv2.imshow('res', clear_qrcode)
cv2.waitKey(0)

