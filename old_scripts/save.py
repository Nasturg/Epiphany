import cv2
import sys
import numpy as np
import math
img = cv2.VideoCapture(0)
img.set(cv2.CAP_PROP_FPS, 30)
img.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
img.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
_, img_rgb = img.read()
cv2.imwrite(sys.argv[1], img_rgb);
img.release()