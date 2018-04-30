import cv2
import numpy as np


def readImg(name):
    img = cv2.imread(name, 0)
    (thresh, im_bw) = cv2.threshold(img, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
    return  im_bw

def erosion(img , structure):
    fsize = 1
    height,width = img.shape
    erodedimg = np.zeros((height,width))
    for i in range(height):
        for j in range(width):
            listofValues = []
            for x in range(-fsize, fsize + 1):
                for y in range(-fsize, fsize + 1):
                    i_n = i + x
                    j_n = j + x
                    if (i_n >= 0 and i_n < height and j_n >= 0 and j_n < width):
                        listofValues.append(img[i_n, j_n])
                    else:
                        listofValues.append(-1)
            score =0
            for l in range(len(structure)):
                if(structure[l]==1):
                    if(listofValues[l] == 0):
                        score+=1
            if(score != 5):
                erodedimg[i,j] = 1
    return erodedimg
def dialation(img , structure):
    fsize = 1
    height,width = img.shape
    dialateimg = np.zeros((height,width))
    for i in range(height):
        for j in range(width):
            listofValues = []
            for x in range(-fsize, fsize + 1):
                for y in range(-fsize, fsize + 1):
                    i_n = i + x
                    j_n = j + x
                    if (i_n >= 0 and i_n < height and j_n >= 0 and j_n < width):
                        listofValues.append(img[i_n, j_n])
                    else:
                        listofValues.append(-1)
            score =0
            for l in range(len(structure)):
                if(structure[l]==1):
                    if(listofValues[l] == 0):
                        score+=1
            if(score == 0):
                dialateimg[i,j] = 1
    return dialateimg
def openingM(img , structure):
    eimg = erosion(img , structure)
    dimg = dialation(eimg,structure)
    return dimg
def closingM(img , structure):
    dimg = dialation(img, structure)
    eimg = erosion(dimg , structure)
    return eimg

def main():
    bw_img = readImg("img1.png")
    st_element = [0,1,0,1,1,1,0,1,0]
    eimg =  erosion(bw_img,st_element)
    eimg2 = dialation(bw_img,st_element)
    openedImg = openingM(bw_img, st_element)
    closedImg = closingM(bw_img, st_element)
    # show
    cv2.imshow("eroded",eimg)
    cv2.imshow("dialated", eimg2)
    cv2.imshow("opened", openedImg)
    cv2.imshow("closed", closedImg)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

main();