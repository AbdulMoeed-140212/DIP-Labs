import cv2
import numpy as np


def btwTransion(img):
    n =0
    h , w = img.shape
    prev = img[0,0]
    for i in range(1,h):
        for j in range(w):
            curr = img[i,j]
            if(curr == 255 and prev == 0):
                n = n+1
            prev = curr
    return  n


rawImg  = cv2.imread("Signature.png" , 0)
ret,img = cv2.threshold(rawImg,15,255,0)
height , width = img.shape
left = width
right = 0
top = height
bottom = 0

for x in range(height):
    for y in range (width):
        if(img[x,y] == 0):
            if x > right:
                right= x
            if x < left:
                left= x
            if y > bottom:
                bottom= y
            if y < top:
                top= y
boundBox = img[left:right,top:bottom]

height , width= boundBox.shape
cx = 0
cy = 0
n =0
for x in range(height):
    for y in range(width):
        if( boundBox[x,y] == 0):
            cx = cx+ x
            cy = cy +y
            n = n + 1
cx = cx / n
cy = cy / n

print cx , cy

fourSegmented  = boundBox.copy()

for i in range(height):
    fourSegmented[i , cy] = 0
for j in range(width):
    fourSegmented[cx , j] = 0

# black to white transitions
TL = btwTransion(boundBox[0:cx,0:cy])
TR = btwTransion(boundBox[cx:width,0:cy])
BR = btwTransion(boundBox[cx:width,cy:height])
BL = btwTransion(boundBox[0:cx,cy:height])

print "Top - Left"
print TL
print "Top - Right"
print TR
print "Bottom - Left"
print BL
print "Bottom - Right"
print BR

cv2.imwrite("bounded.png",  boundBox)
cv2.imwrite("segmented.png",  fourSegmented)

cv2.imshow("bounded",  boundBox)
cv2.imshow("segmented",  fourSegmented)
cv2.waitKey(0)
cv2.destroyAllWindows()