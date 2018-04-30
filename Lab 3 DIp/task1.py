import cv2
import numpy
import numpy as np

def ConvertTobinary(img_name , extension, thresh ):
    image = cv2.imread(img_name+extension) # read image
    image_grey = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) # convert to grey scale
    ret, thresh_img = cv2.threshold(image_grey, thresh, 255, cv2.THRESH_BINARY)# cv.threshold(	src, thresh, maxval, type[, dst]	)
    return thresh_img
#   Start Main Code -------------------------------------------------------------------------
#  get binary image
image = ConvertTobinary("Lab4-image" , ".png" , 100); # enter image file name and extension separately

# detect objects that are black!!!!
# Zero is black
#==========================================
# First Pass
currentlabel = 1

height , width =  image.shape
replacePointer = []
matrixNew  = numpy.zeros((height, width))
upAssigned = False
for i  in range(0 , height -1):
    for j in range(0 , width -1):
        if image[i,j] == 255:
            matrixNew[i, j] = 500;
        elif image[i,j] == 0:
            if i-1 > 0 :  # check if there is a pixel before p
                if matrixNew[i-1, j] != 500 : # if not white
                    upAssigned = True
                    matrixNew[i,j] = matrixNew[i-1,j] # assign
            if j-1 > 0 :# check if there is a pixel on top of p
                if matrixNew[i,j-1] != 500: # if not white
                    if upAssigned == True and matrixNew[i-1, j] < matrixNew[i , j-1]: # pointers for second pass
                        if [matrixNew[i-1, j] , matrixNew[i , j-1]] not in replacePointer:
                            replacePointer.append([matrixNew[i-1, j] , matrixNew[i , j-1]]) # add new pointer
                        upAssigned = False
                        continue
                    matrixNew[i, j] = matrixNew[i, j - 1]
            if i-1> 0 and j-1 >0: # if both top and left pixels are white
                if matrixNew[i-1,j] == 500 and matrixNew[i,j-1] ==500:
                    currentlabel = currentlabel +1; # new label
                    matrixNew[i, j] = currentlabel; # assign new Label
        upAssigned = False
        # else:
#=============================================
# secondPass
for _pair in reversed(replacePointer):  # replace redundant labels
    for i  in range(0 , height -1):
        for j in range(0 , width -1):
            if(matrixNew[i,j] == _pair[1]):
                matrixNew[i, j] = _pair[0]

#=============================================
blank_image = np.zeros((height,width,3), np.uint8) # empty array
# check All labels in image
# numbersRange = []
# for i  in range(0 , height -1):
#     for j in range(0 , width -1):
#         if(matrixNew[i,j] not  in numbersRange):
#             numbersRange.append(matrixNew[i,j])
# print  numbersRange
# print len(numbersRange)  44 labels were generated

# createing new image
for i  in range(0 , height -1):
    for j in range(0 , width -1):
        if(matrixNew[i,j] < 500 ):
            if(matrixNew[i,j]%5):
                blank_image[i, j] = [matrixNew[i,j],50,220]

            elif(matrixNew[i,j]%7):
                blank_image[i, j] = [20, matrixNew[i, j], 220]

            elif(matrixNew[i,j]%11):
                blank_image[i, j] = [220, 50, matrixNew[i, j] + 5]

        else:
            blank_image[i, j] = [255, 255, 255]

# save image
cv2.imwrite("Labeled image.png" , blank_image)