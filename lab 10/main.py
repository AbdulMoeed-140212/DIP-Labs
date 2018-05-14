import cv2 as cv
import numpy as np


img = cv.imread("img.png",0)
img =  cv.GaussianBlur(img,(9,9),10)
th2 , ret2 = cv.threshold(img,0,255,cv.THRESH_BINARY + cv.THRESH_OTSU)

kernel = np.ones((5,5))
ret2 = cv.morphologyEx(ret2, cv.MORPH_OPEN, kernel)
ret2 = cv.dilate(ret2 , kernel,50)
cv.imshow("the",ret2)


label, ret = cv.connectedComponents(ret2)

# Map component labels to hue val
label_hue = np.uint8(179*ret/np.max(ret))
blank_ch = 255*np.ones_like(label_hue)
labeled_img = cv.merge([label_hue, blank_ch, blank_ch])
print("Number of Objects "+str(label))
# cvt to BGR for display
labeled_img = cv.cvtColor(labeled_img, cv.COLOR_HSV2BGR)

# set bg label to black
labeled_img[label_hue==0] = 0

cv.imshow('labeled.png', labeled_img)
cv.waitKey()
cv.imwrite("result.png",labeled_img)


raw = cv.imread("img.png")
#height , width , depth = raw
#for