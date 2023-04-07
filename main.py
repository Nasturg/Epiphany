import cv2
import numpy as np

img = cv2.imread('logo.png', -1)
cv2.imshow("image_logo", img)

cv2.waitKey(0)

cv2.destroyAllWindow()