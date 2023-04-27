import cv2
import sys
import numpy as np
import math

average_points = []
average_sizes = []
DIFFERENCE = 20
MIN = 90
MAX = 110
MODULE = 5
LINE_WIDTH = 40
LINE_HEIGH = 40
BLUR_CORE_CONVULTION = (3, 3)

# WAY = "/home/pi/"
# FILE = WAY + "result.txt"
TRESHOLD = 0.8

matrix_width = 1
matrix_heigth = 4
matrix = [[0],
          [0],
          [0],
          [0]]
shift_x = 160;
shift_end_x = 1149;
shift_y = 45;
shift_end_y = 644;
x_cell_size = int((shift_end_x - shift_x) / matrix_width)
y_cell_size = int((shift_end_y - shift_y) / matrix_heigth)

template__ = None


def addAveragePoint(point, minDif, w, h):
    for pt in average_points:
        if point[0] <= pt[0] + minDif and point[0] >= pt[0] - minDif:
            if point[1] <= pt[1] + minDif and point[1] >= pt[1] - minDif:
                return
    average_points.append(point)
    average_sizes.append((w, h))


def increase_brightness(img, value=30):
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    h, s, v, = cv2.split(hsv)

    lim = 255 - value
    v[v > lim] = 255
    v[v <= lim] += value

    final_hsv = cv2.merge((h, s, v))
    img = cv2.cvtColor(final_hsv, cv2.COLOR_HSV2BGR)
    return img


def writeToFILE(matrix_):
    # file = open(FILE, "w")
    result = ""
    x = matrix_heigth - 1
    while x >= 0:
        y = 0
        while y < matrix_width:
            # print("x: " + str(x) + " y: " + str(y))
            result += (str(matrix[x][y]) + ';')
            y += 1
        x -= 1

    print(result + "\n")


def fillMatrix(index):
    i = 0
    string = ""
    while i < len(average_sizes):
        X = int(average_points[i][0] + average_sizes[i][0] / 2)
        Y = int(average_points[i][1] + average_sizes[i][1] / 2)
        x = math.floor((X - shift_x) / x_cell_size)
        y = math.floor((Y - shift_y) / y_cell_size)

        matrix[int(y)][int(x)] = int(index)
        i += 1


def findingWithResize(template, MinPercent, maxPercent, module):
    if ((MinPercent < 0 or MinPercent > 150) or (maxPercent > 150 or maxPercent < 0) or (maxPercent < MinPercent)):
        print("Wrong MIN, MAX sizes")
        exit()
    size = maxPercent
    while size >= MinPercent:
        if size % module == 0:
            width = int(template.shape[1] * size / 100)
            height = int(template.shape[0] * size / 100)
            dsize = (width, height)
            # print(str(width) + " - " + str(height))
            if getContourse(cv2.resize(template, dsize)) == True:
                return True
        size -= 1
    return False


def getContourse(template):
    w, h = template.shape[::-1]

    res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
    loc = np.where(res >= TRESHOLD)
    for pt in zip(*loc[::-1]):
        addAveragePoint(pt, DIFFERENCE, w, h)


img = cv2.VideoCapture(0)
img.set(cv2.CAP_PROP_FPS, 30)
img.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
img.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
_, img_rgb_OLD = img.read()
img_rgb = increase_brightness(img_rgb_OLD, 70)

img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
i = 0

while i < len(sys.argv) - 1:
    template__ = cv2.imread(sys.argv[i + 1], 0)
    findingWithResize(template__, MIN, MAX, MODULE)
    fillMatrix(int(i + 1))
    del average_points[:]
    del average_sizes[:]
    i += 1
writeToFILE(matrix)
