import cv2

vid_capture = cv2.VideoCapture(0)

# frame_width = int(vid_capture.get(3))
vid_capture.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
vid_capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
frame_width = 1280
# frame_height = int(vid_capture.get(4))
frame_height = 720
frame_size = (frame_width, frame_height)
fps = 30
frames = 100

fourcc = cv2.VideoWriter_fourcc('M', 'J', 'P', 'G')
video_writer = cv2.VideoWriter('../../media/usb/output.avi', fourcc, fps, frame_size)

cap = cv2.VideoCapture(0)

for i in range(frames):
    ret, frame = cap.read()
    # cv2.imshow('frame', frame)
    if not ret:
        break
    video_writer.write(frame)


video_writer.release()
cap.release()
