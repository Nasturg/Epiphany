import cv2

img = cv2.imread('image/win2.png')
height, widht, _ = img.shape
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('ready', img)