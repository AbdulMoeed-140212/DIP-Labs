import numpy as np
import cv2
import math

filterSize = 5

rawimg = cv2.imread("saltandpaper.tif",0)
height , width = rawimg.shape
img = rawimg.copy()

fsize = int(filterSize / 2)

for i in range(height):
    print int(float(i)/height *100)
    for j in range(width):
        listofValues = []
        for x in range(-fsize, fsize + 1):
            for y in range(-fsize, fsize + 1):
                i_n = i + x
                j_n = j + x
                if (i_n >= 0 and i_n < height and j_n >= 0 and j_n < width):
                    listofValues.append(rawimg[i_n, j_n])
                else:
                    listofValues.append(0)
        listofValues.sort()
        img[i,j] =  listofValues[len(listofValues)/2]

cv2.imshow("original", rawimg)
cv2.imshow("something",img)
cv2.imwrite("saltnperpper1.tif",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
