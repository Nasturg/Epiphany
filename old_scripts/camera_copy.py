import cv2
import sys
import numpy as np
import math

average_points = []
average_sizes = []
DIFFERENCE = 20
MIN = 80
MAX = 110
MODULE = 5
LINE_WIDTH = 10
LINE_HEIGH = 10
BLUR_CORE_CONVULTION = (3, 3)

WAY = "/home/pi/"
FILE = WAY + "result.txt"
TRESHOLD = 0.8

matrix_size = 6
matrix =   [[0,0,0,0,0,0], 
            [0,0,0,0,0,0],
            [0,0,0,0,0,0],
            [0,0,0,0,0,0],
            [0,0,0,0,0,0],
            [0,0,0,0,0,0]]
shift_x = 422;
shift_end_x = 991;
shift_y = 141;
shift_end_y = 656;
x_cell_size = int((shift_end_x - shift_x) / matrix_size)
y_cell_size = int((shift_end_y - shift_y) / matrix_size)
NS_x = -1
NS_y = -1
NS_w = -1
NS_h = -1

template__ = None
def addAveragePoint(point, minDif, w, h):
    for pt in average_points:
        if point[0] <= pt[0] + minDif and point[0] >= pt[0] - minDif:
            if point[1] <= pt[1] + minDif and point[1] >= pt[1] - minDif:
                return
    average_points.append(point)
    average_sizes.append((w,h))

def writeToFILE(matrix_):
    file = open(FILE, "w")
    result = ""
    x = 0
    while x < matrix_size:
        y = 0
        while y < matrix_size:
            result += (str(matrix[x][y])+';')
            y += 1
        x += 1

    file.write(result + "\n")
    file.close()

def fillMatrix(index):
    i = 0
    string = ""
    if NS_x > 0:
        global shift_end_x
        global shift_x
        global shift_end_y
        global shift_y
        global x_cell_size
        global y_cell_size 
        shift_end_x = NS_x + (NS_w)
        shift_y = NS_y + (NS_h)
        shift_x = shift_end_x - NS_w*matrix_size-1
        shift_end_y = shift_y + NS_h*matrix_size
        x_cell_size = int((shift_end_x - shift_x) / matrix_size)
        y_cell_size = int((shift_end_y - shift_y) / matrix_size)
        #print("x1: " + str(shift_x) + " y1: " + str(shift_y) + " x2: " + str(shift_end_x) + " y2: " + str(shift_end_y) + " w: " + str(x_cell_size) + " h: " + str(y_cell_size))
    while i < len(average_sizes):
        X = int(average_points[i][0] + average_sizes[i][0]/2)
        Y = int(average_points[i][1] + average_sizes[i][1]/2)
        x = math.floor((X-shift_x) / x_cell_size)
        y = math.floor((Y-shift_y) / y_cell_size)
        
        matrix[int(y)][int(x)] = int(index)
        i += 1

def findingWithResize(template, MinPercent, maxPercent, module):
    if ((MinPercent < 0 or MinPercent > 150) or (maxPercent > 150 or maxPercent < 0) or (maxPercent < MinPercent)):
        print("Wrong MIN, MAX sizes")
        exit()
    size = maxPercent
    while size >= MinPercent:
        if size%module == 0:
            width = int(template.shape[1] * size / 100)
            height = int(template.shape[0] * size / 100)
            dsize = (width, height)
            #print(str(width) + " - " + str(height))
            if getContourse(cv2.resize(template, dsize)) == True:
                 return True
        size -= 1
    return False

def getContourse(template):
  
    w, h = template.shape[::-1]
  
    res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)
    loc = np.where( res >= TRESHOLD) 
    for pt in zip(*loc[::-1]):
        addAveragePoint(pt, DIFFERENCE, w, h)


img = cv2.VideoCapture(0)
img.set(cv2.CAP_PROP_FPS, 30)
img.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
img.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
_, img_rgb = img.read()
#img_rgb = cv2.GaussianBlur(img_rgb, BLUR_CORE_CONVULTION , 0)

#img_rgb = cv2.imread(WAY + 'Table.png')
img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
i = 0
NS_template = cv2.imread(WAY + 'NS.png', 0)
findingWithResize(NS_template, MIN, MAX, MODULE)
if len(average_sizes) > 0:
    NS_w = average_sizes[0][0] + LINE_WIDTH
    NS_h = average_sizes[0][1] + LINE_HEIGH
    NS_x = average_points[0][0]
    NS_y = average_points[0][1]
    print("x: " + str(NS_x) + " y: " + str(NS_y) + " w: " + str(NS_w) + " h: " + str(NS_h))
    del average_points[:]
    del average_sizes[:]

while i < len(sys.argv)-1:
    template__ = cv2.imread(sys.argv[i+1] , 0)
    findingWithResize(template__, MIN, MAX, MODULE)
    fillMatrix(int(i+1))
    del average_points[:]
    del average_sizes[:]
    i += 1
writeToFILE(matrix)
img.release()
