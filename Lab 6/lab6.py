import cv2
import numpy as np
from matplotlib import pyplot as plt

# load Image
img = cv2.imread("hist2.tiff", 0)
# ----------------------------------------------------------
#Task (a)

plt.hist(img.ravel(),256,[0,256])
plt.show()
# ----------------------------------------------------------
height , width = img.shape # 500 * 500
pixelcount = height * width # 250000

# Task (b)
# frecquency
frecquency_dist = np.zeros((256))
for i in range(height):
    for j in range(width):
        frecquency_dist[img[i,j]] = frecquency_dist[img[i,j]] + 1

# probability
probability_array = np.zeros(len(frecquency_dist))
for i in range (len(probability_array)):
    probability_array[i] = frecquency_dist[i] /pixelcount

# comulative
commulative_freq = np.zeros(len(frecquency_dist))
commulative_freq[0] = probability_array[0]
for i in range(1 , len(commulative_freq)):
    commulative_freq[i] = probability_array[i]  + commulative_freq[i-1]

# multiply by L - 1 = 256 -1 = 255
xMultiplied = [np.math.floor(x * 255)  for x in commulative_freq]
print xMultiplied
# replace values
ContrastCorrected = img
for i in range(height):
    for j in range(width):
        ContrastCorrected[i , j ] = xMultiplied[img[i,j]]

#---------------- Showing New Histogram ----------------------------
# Task (c)
plt.hist(ContrastCorrected.ravel() , 255 , (0,  255))
plt.show()
# Save Image
cv2.imwrite("CorrectedImage.png" , ContrastCorrected)