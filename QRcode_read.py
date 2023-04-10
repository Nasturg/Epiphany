import cv2
import qrcode
# import numpy as np

# Генерация QR кода
qr = qrcode.QRCode(
    version=2,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)

qr.add_data('Robotics_Mob')  # информация в qr коде
qr.make(fit=True)

img = qr.make_image(fill_color='black', back_color='white')  # Отрисовка qr кода
img.save('image/QRtest.jpeg', 'JPEG')

cap = cv2.VideoCapture(0)



# cv2.imshow('res', clear_qrcode)
cv2.waitKey(0)

while True:
    ret, frame = cap.read()
    cv2.imshow('frame', frame)

    # Чтение QR кода
    img_qrcode = cv2.imread('frame')  # Загрузка изображения с несколькими QR-кодами
    detector = cv2.QRCodeDetector()  # Поиск и распознавание всех QR-кодов на изображении

    # data, bbox, clear_qrcode = detector.detectAndDecode(img_qrcode)

    # Обработка каждого QR-кода
    for qr_code in detector:
        # Извлечение содержимого QR-кода
        qr_data = qr_code.data.decode('utf-8')
        # data, bbox, clear_qrcode = detector.detectAndDecode(img_qrcode)
        print('QR Code:', qr_data)


    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
