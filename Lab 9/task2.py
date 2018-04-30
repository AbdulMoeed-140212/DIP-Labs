import cv2
import numpy as np
import math

def readImg(name):
    img = cv2.imread(name, 0)
    (thresh, im_bw) = cv2.threshold(img, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
    return  im_bw

def erosion(img , structure):
    fsize = int(math.floor(math.sqrt(len(structure))/2))
    limit = sum(structure)
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
            if(score != limit):
                erodedimg[i,j] = 1
    return erodedimg
def dialation(img , structure):
    fsize = int(math.floor(math.sqrt(len(structure))/2))
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

def extractForeground(original , mask):
    height , width , depth = original.shape

    for i in range(height):
        for j in range(width):
            if(mask[i,j] != 0):
                original[i,j] = [255,255,255]
    return  original
def main():
    bw_img = readImg("img2.png")
    cv2.imshow("original",bw_img)
    st_element = [0, 0, 1, 0, 0,
                  0, 1, 1, 1, 0,
                  1, 1, 1, 1, 1,
                  0, 1, 1, 1, 0,
                  0, 0, 1, 0, 0,]
    st_element_small = [0, 0, 0,
                        1, 1, 1,
                        0, 0, 0]
    # Erode
    eimg = erosion(bw_img,st_element_small)
    eimg = erosion(eimg , st_element)
    eimg = dialation(eimg , st_element)
    eimg = openingM(eimg, st_element)
    # extracting bg
    original_img = cv2.imread("img2.png")
    extracted_img = extractForeground(original_img.copy(),eimg)
    # show
    cv2.imshow("original Coloured" , original_img)
    cv2.imshow("Mask",eimg)
    cv2.imshow("extracted", extracted_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

main();