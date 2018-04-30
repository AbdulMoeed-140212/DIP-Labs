from PIL import Image
import  numpy as np
img = Image.open("Lab4-image.png")
pixels = img.load()
##print pixels
for i in range(img.size[0]):
    for j in range(img.size[1]):
        r, g, b = img.getpixel((i, j))
        a = (r + g + b)/3
        if a < 100:
                pixels[i, j] = (0, 0, 0)
        else:
                pixels[i, j] = (255, 255, 255)

# img.show()

# list = [[1, 1, 0, 1, 1, 1, 0, 1], [2, 1, 0, 1, 0, 1, 0, 1], [1, 1, 1, 1, 0, 0, 0, 1], [0, 0, 0, 0, 0, 0, 0, 1],
#         [1, 1, 1, 1, 0, 1, 0, 1], [0, 0, 0, 1, 0, 1, 0, 1], [1, 1, 1, 1, 0, 0, 0, 1], [1, 1, 1, 1, 0, 1, 1, 1]]
# list2 = [[1, 1, 0, 1, 1, 1, 0, 1], [3, 0, 0, 1, 0, 1, 0, 1], [1, 1, 1, 1, 0, 0, 0, 1], [0, 0, 0, 0, 0, 0, 0, 1],
#          [1, 1, 1, 1, 0, 1, 0, 1], [0, 0, 0, 1, 0, 1, 0, 1], [1, 1, 1, 1, 0, 0, 0, 1], [1, 1, 1, 1, 0, 1, 1, 1]]
list1 = np.asarray(img) # image to array
list2 = list1  # copy
dict = {}
y1 = 0
current = 1;
for i in range(list1.shape[0]):
    for j in range(0, list1.shape[1]):
        if i == 0 and j == 0:
            if list[i,j] != 0:
                list2[i,j] = current;
        elif i == 0 and j > 0:
            if list[i,j] != 0:
                if list2[i,j - 1] == current:
                    list2[i,j] = current;
                if list2[i,j - 1] != current:
                    current = current + 1
                    list2[i,j] = current
        elif i > 0 and j == 0:
            if list[i,j] != 0:
                if list2[i - 1,j] == 0:
                    current = current + 1
                    list2[i,j] = current
                if list2[i - 1,j] == current:
                    list2[i,j] = current
                elif list2[i - 1,j] != current and list2[i - 1,j] != 0:
                    list2[i,j] = list2[i - 1,j]
        else:
            if list[i,j] != 0:
                if list2[i - 1,j] == list2[i,j - 1]:
                    if list2[i - 1,j] == 0 and list2[i,j - 1] == 0:
                        ##                        print list2[i-1][j]
                        ##                        print list2[i][j-1]
                        ##                        print current
                        current = current + 1;
                        list2[i,j] = current
                    ##                        print list2[i][j]
                    else:
                        list2[i,j] = list2[i - 1,j]
                elif list2[i - 1,j] != list2[i,j - 1]:
                    if list2[i - 1,j] == 0:
                        list2[i,j] = list2[i,j - 1];
                    elif list2[i,j - 1] == 0:
                        list2[i,j] = list2[i - 1,j];
                    else:

                        list2[i,j] = min(list2[i - 1,j], list2[i,j - 1])
                        dict1 = {min(list2[i - 1,j], list2[i,j - 1]): max(list2[i - 1,j], list2[i,j - 1])}
                        dict.update(dict1)

##print list
##print list2
##print dict
for i in range(len(list)):
    for j in range(0, len(list[i])):
        for k in dict:
            ##            print list2[i][j]
            ##            print dict[k]
            if list2[i,j] == dict[k]:
                list2[i,j] = k

img = Image.fromarray(list2)
img.save("some.png","png")



