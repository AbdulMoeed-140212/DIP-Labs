import numpy as np
import cv2


filterSize = 3
weight = [1,1,1,1,1,1,1,1,1]
rawimg = cv2.imread("unsharpmasking.tif",0)
height , width = rawimg.shape
img = rawimg.copy()

fsize = int(filterSize / 2)
# averaging
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
        b = []
        for k in range(len(weight)):
            b.append(listofValues[k]* weight[k])

        img[i,j] =  sum(b)/ sum(weight)
# subtracting from original
subtracted = rawimg.copy()
for i in range(height):
    for j in range(width):
        subtracted[i,j] = rawimg[i,j] - img[i,j]

# add to original
addtioned = rawimg.copy()
for i in range(height):
    for j in range(width):
        addtioned[i,j] = rawimg[i,j] + subtracted[i,j]

cv2.imshow("original", rawimg)
cv2.imshow("something",addtioned)
cv2.imwrite("unmaskeSharpeneing1.tif",addtioned)
cv2.waitKey(0)
cv2.destroyAllWindows()

