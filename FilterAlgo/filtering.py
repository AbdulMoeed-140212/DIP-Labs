import  cv2
import numpy as np

def avgfillter(img):
    height, width = img.shape
    newImg = img.copy()
    for i in range(3):
        for j in range(3):
            fillValues = []
            fillValues.append(img[i, j])
            if ( i != 0):
                fillValues.append(img[i - 1, j])
                if(j != 0):
                    fillValues.append(img[i-1 , j-1])

                if(j != width-1):
                    fillValues.append(img[i - 1, j+1])
            if( j != 0):
                fillValues.append(img[i, j - 1])
            if(j != width -1):
                fillValues.append(img[i, j + 1])
            if(i != height-1):
                fillValues.append(img[i + 1, j])
                if(j != 0):
                    fillValues.append(img[i + 1, j - 1])
                if(j != width -1):
                    fillValues.append(img[i + 1, j + 1])
            fillValues.sort()
            newImg[i,j] = fillValues[int(len(fillValues)/2)]

    return newImg

img = cv2.imread("Lab4-image.png",0)

img1 = avgfillter(img)

cv2.imwrite("avg.png", img1)
