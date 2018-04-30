import numpy as np
import cv2
from math import sqrt as squareRoot


def filtering(rawimg , weight, filterSize):
    height, width , depth= rawimg.shape
    img = rawimg.copy()
    fsize = int(filterSize / 2)

    for i in range(height):
        print int(float(i)/height *100)
        for j in range(width):
            listofValues = [[],[],[]]
            for x in range(-fsize, fsize + 1):
                for y in range(-fsize, fsize + 1):
                    i_n = i + x
                    j_n = j + x
                    if (i_n >= 0 and i_n < height and j_n >= 0 and j_n < width):
                        listofValues[0].append(rawimg[i_n, j_n][0])
                        listofValues[1].append(rawimg[i_n, j_n][1])
                        listofValues[2].append(rawimg[i_n, j_n][2])
                    else:
                        listofValues[0].append(0)
                        listofValues[1].append(0)
                        listofValues[2].append(0)
            b = [[],[],[]]
            for k in range(len(weight)):
                b[0].append(listofValues[0][k]* weight[k])
                b[1].append(listofValues[1][k] * weight[k])
                b[2].append(listofValues[2][k] * weight[k])
            img[i,j][0]=sum(b[0])/3
            img[i,j][1]=sum(b[1])/3
            img[i,j][2]=sum(b[2])/3

    return  img

filterSize = 3
w_horizontal = [ 1, 1, 1,
                 0, 0, 0,
                -1,-1, -1]
w_vertical = [1, 0,-1,
              1, 0,-1,
              1, 0,-1]
rawimg = cv2.imread("two_cats.jpg")
vEdge = filtering(rawimg,w_vertical , filterSize)
hEdge = filtering(rawimg,w_horizontal , filterSize)

mergedImg = rawimg.copy()
height , width ,depth= rawimg.shape
for i in range(height):
    for  j in range(width):
        mergedImg[i, j][0] = int(np.emath.sqrt((vEdge[i, j][0] ** 2) + (hEdge[i, j][0] ** 2)))
        mergedImg[i, j][1] = int(np.emath.sqrt((vEdge[i, j][1] ** 2) + (hEdge[i, j][1] ** 2)))
        mergedImg[i, j][2] = int(np.emath.sqrt((vEdge[i, j][2] ** 2) + (hEdge[i, j][2] ** 2)))
cv2.imshow("original", rawimg)
cv2.imshow("Both",mergedImg)
cv2.imwrite("two_catsEdge.jpg",mergedImg)
cv2.waitKey(0)
cv2.destroyAllWindows()
