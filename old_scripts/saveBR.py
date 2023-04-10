import cv2
import sys
import numpy as np
import math


def increase_brightness(img, value=30):
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    h, s, v, = cv2.split(hsv)

    lim = 255 - value
    v[v > lim] = 255
    v[v <= lim] += value

    final_hsv = cv2.merge((h, s, v))
    img = cv2.cvtColor(final_hsv, cv2.COLOR_HSV2BGR)
    return img

img = cv2.VideoCapture(0)
img.set(cv2.CAP_PROP_FPS, 30)
img.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
img.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
_, img_rgb_OLD = img.read()
img_rgb = increase_brightness(img_rgb_OLD, 70)
cv2.imwrite(sys.argv[1], img_rgb);
img.release()