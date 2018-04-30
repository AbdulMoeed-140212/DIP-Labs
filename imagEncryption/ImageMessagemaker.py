import cv2

def numtoBinary( n , b):
    a = bin(n)
    if(b == 1):
        c = a[:len(a) - 1] + "1"
    else:
        c = a[:len(a) - 1] +"0"
    return int(c , 2)


def convertBAck(imgname):
    img = cv2.imread(imgname)
    for i in range(height - 1):
        for j in range(width - 1):
            binary  = bin(img[i,j][2])
            if binary[len(binary)-1] == "1":
                img[i, j] = [255 , 255, 255];
            else:
                img[i, j] = [0 ,0 ,0];

    cv2.imwrite("decoded.png", img)


newImage = cv2.imread("Lab4-image.png")
msgImage = cv2.imread("msg.png")
msgImage = cv2.cvtColor( msgImage, cv2.COLOR_RGB2GRAY )
cImage = newImage
height , width ,s= newImage.shape

cblack =0
cwhite =0
for i in  range(height-1 ):
    for j in range(width-1):
        if msgImage[i , j]== 0:
            cblack = cblack +1
            cImage[i,j] = [newImage[i,j][0] , newImage[i,j][1] ,  numtoBinary(newImage[i,j][2] ,0)]
        else:
            cwhite = cwhite +1
            cImage[i, j] = [newImage[i, j][0], newImage[i, j][1], numtoBinary(newImage[i, j][2], 1)]


print "black"
print cblack
print "white"
print cwhite
cv2.imwrite("new.png", cImage)

convertBAck("new.png")

print numtoBinary(5, 1)