import cv2
from matplotlib import pyplot as plt

# Task 1  Function
def ConvertTobinary(img_name , extension, thresh ):
    image = cv2.imread(img_name+extension) # read image
    image_grey = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) # convert to grey scale
    ret, thresh_img = cv2.threshold(image_grey, thresh, 255, cv2.THRESH_BINARY)# cv.threshold(	src, thresh, maxval, type[, dst]	)
    cv2.imwrite(img_name+"Binary"+extension,thresh_img) # save

# Task 2 Function
def PlotHistogram(name):
    img = cv2.imread(name, 0)# 0  converts image to greyscale
    plt.hist(img.ravel(), 256, [0, 256])
    plt.show()

# Task 1
ConvertTobinary("B1", ".png",160)
ConvertTobinary("B2", ".jpg",140)
ConvertTobinary("B3", ".jpg",150)
ConvertTobinary("XY-cutss", ".png",127)

#Task 2
PlotHistogram("B1.png")
PlotHistogram("B2.jpg")
PlotHistogram("B3.jpg")

#Task 3

def findpercent(obt , total): # get percentage
    return (obt*1.0/total) * 100


def partition(imageName): # partiton image
    img = cv2.imread(imageName) # read image
    height, width, depth = img.shape
    for i in range(0, height): # traverse coloumn
        count =0
        for j in range(0, (width)): # traverse Row
            if (img[i,j][0] <=10) and  (img[i,j][1] <=10) and (img[i,j][2] <=10):
                count = count + 1
        if findpercent(count,width) < 0.8: # Repaint Row
            for k in range(0,(width)):
                img[i,k] = [154,128,205]

    cv2.imwrite("NewImg.png" ,img )

partition("XY-cutss.png")