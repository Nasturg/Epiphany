# Запись видео потока

import cv2

vid_capture = cv2.VideoCapture(0, cv2.CAP_DSHOW)

# Определение параметров видео потока
frame_width = int(vid_capture.get(3))
frame_height = int(vid_capture.get(4))
frame_size = (frame_width, frame_height)
fps = 30
frames = 100

# Инициализировать объект записи видео
fourcc = cv2.VideoWriter_fourcc('M', 'J', 'P', 'G')
video_writer = cv2.VideoWriter('../video/output.avi', fourcc, fps, frame_size)

cap = cv2.VideoCapture(0)

for i in range(frames):
    ret, frame = cap.read()
    # cv2.imshow('imshowframe', frame)
    if not ret:
        break
    video_writer.write(frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        # cv2.waitKey(0) - бесконечно ожидание нажатия кнопки
        # cv2.waitKey(1) - ожидание нажатия кнопки в течение 1 мили секунд
        break

# Закрытие объектов VideoWriter и VideoCapture
video_writer.release()
cap.release()
