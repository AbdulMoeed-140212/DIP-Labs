import cv2
import numpy as np


def ConvertTobinary(img_name , thresh ):
    image = cv2.imread(img_name) # read image
    image_grey = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) # convert to grey scale
    ret, thresh_img = cv2.threshold(image_grey, thresh, 255, cv2.THRESH_BINARY)# cv.threshold(	src, thresh, maxval, type[, dst]	)
    return thresh_img

def imageInverter(imgname):
    rawimage = cv2.imread(imgname); # load image
    invertedImage = rawimage # copy
    depth = np.array(rawimage).ndim # check depth / number of plans
    # print depth
    if depth == 3:
        height, width , depth = rawimage.shape  # for RGB
    elif depth <=2:
        height, width= rawimage.shape # for Grey Scale
    for i in range(0, height):  # traverse coloumn
        for j in range(0, (width)):  # traverse Row
            if depth == 3: # for RGB
                invertedImage[i, j][0] = 255 - rawimage[i, j][0]
                invertedImage[i, j][1] = 255 - rawimage[i, j][1]
                invertedImage[i, j][2] = 255 - rawimage[i, j][2]
            elif depth == 2: # for Grey Scale
                invertedImage[i, j] = 255 - rawimage[i, j]
    # save and return
    cv2.imwrite("Inverted_"+imgname,invertedImage)
    return  invertedImage


# Task 1
imageInverter("lena_color.png")
imageInverter("greyscale.png")
imageInverter("binary.png")


# Task 2
rawimage = cv2.imread("lena_color.png")
rawimage = cv2.cvtColor(rawimage, cv2.COLOR_RGB2GRAY)
height, width= rawimage.shape
gradientImage = np.zeros((height, width))
vertical = np.zeros((height, width))
horizontal = np.zeros((height, width))

#  Horizontal gradient
for i in range(1, height-1):  # traverse coloumn
    for j in range(1, width-1):  # traverse Row
        horizontal[i,j] = rawimage[i,j+1] - rawimage[i, j]
#  Vertical gradient
for i in range(1, height-1):  # traverse coloumn
    for j in range(1, width-1):  # traverse Row
        vertical[i,j] = rawimage[i+1,j] - rawimage[i-1, j]
# Bot Gradients
for i in range(0, height):  # traverse coloumn
    for j in range(0, width):  # traverse Row
        v = vertical[i,j]
        h = horizontal[i,j]
        gradientImage[i,j] = abs(128 - int(np.emath.sqrt((v * v) + (h * h))))

# Save each Separately
cv2.imwrite("vertical2.png",vertical)
cv2.imwrite("horizontal2.png",horizontal)
cv2.imwrite("both2.png",gradientImage)
