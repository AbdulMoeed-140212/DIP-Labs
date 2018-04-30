import cv2
import numpy as np
#load image
img = cv2.imread("Camerica.jpg" , 0)

height , width= img.shape
#count number of colors
color = []

for i in range(height):
    for j in range(width):
        if(img[i,j] not in color):
            color.append(img[i,j])

color.sort()
print color
print len(color)

replacement=[[29, 41, 81],[ 0, 49, 82] , [14, 77 ,146] , [16 ,52 ,166] , [0,128 ,255], [15 ,82 ,186], [ 76, 81, 109],[114 ,133 ,165]]

replacement.sort()
dict = {}
j=0;k=0
for i in range(len(color)):
    dict[color[i]] = replacement[j]
    if not (i%2):
        j= j +1
    if j >= len(replacement):
        j = j - 1;
print dict


coloredImg = cv2.imread("Camerica.jpg")
for i in range(height):
    for j in range(width):
        coloredImg[i,j]= dict[img[i,j]]

print coloredImg[0,9]
cv2.imshow("final" , coloredImg)
cv2.waitKey(0)
cv2.destroyAllWindows()