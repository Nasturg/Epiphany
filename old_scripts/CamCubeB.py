
import cv2
import sys
import numpy as np

if len(sys.argv) < 2:
    print("have no argument!    (png, jpg, ...)")
    exit()

MIN = 100
MAX = 115
MODULE = 5

MIN_ROTATION = -1
MAX_ROTATION = 1
ROTATION_MODULE = 1

BLUR_CORE_CONVULTION = (3, 3)
FILE = "result1.txt"
TRESHOLD = 0.8

def writeToFILE(data):
    file = open(FILE, "w")
    print(data)
    file.write(str(data))
    file.close()

def increase_brightness(img, value=30):
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    h, s, v, = cv2.split(hsv)

    lim = 255 - value
    v[v > lim] = 255
    v[v <= lim] += value

    final_hsv = cv2.merge((h, s, v))
    img = cv2.cvtColor(final_hsv, cv2.COLOR_HSV2BGR)
    return img

def rotation(template):
    for deg in range(MIN_ROTATION, MAX_ROTATION):
        if deg % ROTATION_MODULE == 0:
            (h, w) = template.shape[:2]
            center = (int(w / 2), int(h / 2))
            rotation_matrix = cv2.getRotationMatrix2D(center, deg, 1)
            route_img = cv2.warpAffine(template, rotation_matrix, (w, h))
            if getContourse(route_img) == True:
                return True
    return False

def findingWithResize(MinPercent, maxPercent, module, temp):
    if ((MinPercent < 0 or MinPercent > 250) or (maxPercent > 250 or maxPercent < 0) or (maxPercent < MinPercent)):
        print("Wrong MIN, MAX sizes")
        exit()
    size = maxPercent
    while size >= MinPercent:
        if size%module == 0:
            width = int(temp.shape[1] * size / 100)
            height = int(temp.shape[0] * size / 100)
            dsize = (width, height)
            if rotation(cv2.resize(temp, dsize)) == True:
                return True
        size -= 1
    return False

def getContourse(template):
  
    w, h = template.shape[::-1]
  
    res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)

    loc = np.where( res >= TRESHOLD) 

    for pr in zip(*loc[::-1]):
        return True
    return False

img = cv2.VideoCapture(0)
img.set(cv2.CAP_PROP_FPS, 30)
img.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
img.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)



temp = cv2.imread(sys.argv[1],0)
_, img_rgb_OLD = img.read()
img_rgb = increase_brightness(img_rgb_OLD, 70)
img_rgb = cv2.GaussianBlur(img_rgb, BLUR_CORE_CONVULTION , 3, 3)
img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
if(findingWithResize(MIN, MAX, MODULE, temp) == True):
    writeToFILE("1")
else:
    writeToFILE("0")
img.release()