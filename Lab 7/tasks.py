import cv2
import numpy as np
from matplotlib import pyplot as plt

histograms = 'Histogram'
results = "Results"
# ----------------------------------------------------------
# Equilize function
def  Equilize_image(img):
    height, width = img.shape
    pixelcount = height * width
    f_array = np.zeros((256))
    # frecquency distribution
    for i in range(height):
        for j in range(width):
            f_array[img[i, j]] = f_array[img[i, j]] + 1
    # probability distribution
    for i in range(len(f_array)):
        f_array[i] = f_array[i] / pixelcount
    # commulative count
    for i in range(1, len(f_array)):
        f_array[i] = f_array[i] + f_array[i - 1]
    nf_array = [np.math.floor(x * 255) for x in f_array]
    # replacementn
    ContrastCorrected = img
    for i in range(height):
        for j in range(width):
            ContrastCorrected[i, j] = nf_array[img[i, j]]
    return ContrastCorrected

# ----------------------------------------------------------
# slice function
def slice_tile(img , x_start , y_start , x_end , y_end):
    nArray = np.zeros((x_end-x_start , y_end - y_start))
    nArray = img[x_start:x_end , y_start :y_end]
    return nArray

# ----------------------------------------------------------
# sliding approach
def slidingPixel(windowSize, image):

    height , width = image.shape
    tempImage = np.zeros((height , width))
    for i in range(0,height-windowSize):
        print i
        for j in range(0 , width - windowSize):
            tempImage[i:windowSize+i , j:windowSize+j] = Equilize_image(slice_tile(image , i,j,windowSize+i , windowSize+j))
    return  tempImage
# ----------------------------------------------------------

# main Start ===============================================

# load Image
img = cv2.imread("lab07.jpg", 0)
# original histogram
plt.hist(img.ravel() , 255 , (0,  255))
plt.savefig(histograms+"Original.png")
plt.clf()
# Task 1    =================================
# Global Equalization
gEqimage = Equilize_image(img)
# save image
cv2.imwrite(results + "OriginalGlobalEqImage.jpg",gEqimage)
# plot histogram
plt.hist(gEqimage.ravel() , 255 , (0,  255))
plt.savefig(histograms+"OriginalGlobalEquilized.png")
plt.clf()
# ============================================

# Task 2 =====================================
# --------------------------------------------
#       Part (a) -----------------------------
# Tile
t1 = Equilize_image(slice_tile(img,0,0,256,256))
plt.hist(t1.ravel(),255,(0,255))
plt.savefig(histograms + "t1.png")
plt.clf()
t2 = Equilize_image(slice_tile(img,0,256,256,512))
plt.hist(t1.ravel(),255,(0,255))
plt.savefig(histograms + "t2.png")
plt.clf()
t3 = Equilize_image(slice_tile(img,256,0,512,256))
plt.hist(t1.ravel(),255,(0,255))
plt.savefig(histograms + "t3.png")
plt.clf()
t4 = Equilize_image(slice_tile(img,256,256,512,512))
plt.hist(t1.ravel(),255,(0,255))
plt.savefig(histograms + "t4.png")
plt.clf()
fullJoint = np.vstack((np.hstack((t1 , t2)),np.hstack((t3 , t4))))
cv2.imwrite(results + "joint.jpg" , fullJoint)
plt.hist(fullJoint.ravel(),255,(0,255))
plt.savefig(histograms + "TiledHistogram.png")
plt.clf()
# --------------------------------------------
#       Part (b) -----------------------------
# Sliding
res = cv2.resize(img, (50, 50), interpolation=cv2.INTER_CUBIC) # resizing
cv2.imwrite(results + "OriginalSmall.jpg" ,res)     # saving
plt.hist(res.ravel(),255,(0,255))
plt.savefig(histograms + "ShrinkedOriginalHistogram.png")
plt.clf()
eqImage = Equilize_image(res) # global equalization

plt.hist(eqImage.ravel(),255,(0,255))
plt.savefig(histograms + "ShrinkedEqHistogram.png")
plt.clf()
slidedimg = slidingPixel(25 , res)      #
cv2.imwrite(results+ "slidedEq.jpg", slidedimg)
plt.hist(slidedimg.ravel(),255,(0,255))
plt.savefig(histograms+"Slided Histogram.png")
plt.clf()
# --------------------------------------------
