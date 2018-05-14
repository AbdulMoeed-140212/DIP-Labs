import cv2
import numpy as np
#AbdulMoeed
# task 1 (thumb print)
img = cv2.imread('thumb.png',0)
size = np.size(img)
skel = np.zeros(img.shape,np.uint8)
# Black and white
ret,img = cv2.threshold(img,127,255,0)
# set structure element
element = cv2.getStructuringElement(cv2.MORPH_CROSS,(3,3))
done = False
# skeletonize
img = 255 - img
while( not done):
    eroded = cv2.erode(img,element)
    temp = cv2.dilate(eroded,element)
    temp = cv2.subtract(img,temp)
    skel = cv2.bitwise_or(skel,temp)
    img = eroded.copy()

    zeros = size - cv2.countNonZero(img)
    if zeros==size:
        done = True
itt = 1
kernel = np.ones((9,9))
# close
skel = cv2.morphologyEx(skel, cv2.MORPH_CLOSE, kernel)
skel = cv2.morphologyEx(skel, cv2.MORPH_CLOSE, kernel)
#AbdulMoeed
kernel = np.ones((3,3))
# dilate
skel = cv2.dilate(skel , kernel , itt)
# blur salt and pepper noise
skel = cv2.medianBlur(skel ,5)
# invert
skel = 255 - skel
# save
cv2.imwrite("thumbResult2.png",skel)
cv2.imshow("Thumb",skel)
cv2.waitKey(0)
cv2.destroyAllWindows()
#AbdulMoeed