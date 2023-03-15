import sys
import os
import cv2
import easygui
import numpy as np
import matplotlib.pyplot as plt


ImagePath=easygui.fileopenbox()
img=cv2.imread(ImagePath)
if img is None:
    print("cannot find any image. upload an image")
    sys.exit()

    #Converting the BGR format to RGB format
img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    #Converting the RGB to grayscale
img_grey=cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
plt.imshow(img_grey)
plt.axis("off")
plt.title(" GREY SCALE")
plt.show()

#median blurring
# img_blur=cv2.medianBlur(img_grey,3)
# plt.imshow(img_blur)
# plt.axis("off")
# plt.title("after median blurring")
# plt.show()

# #creating edge mask
# edges=cv2.adaptiveThreshold(img_blur,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,3,3)
# plt.imshow(edges)
# plt.axis("off")
# plt.title("Edge mask")
# plt.show()

# #removing unwanted details of the image (bilateral blurring)
# img_bb=cv2.bilateralFilter(img_blur,15,17,75)
# plt.imshow(img_bb)
# plt.axis("off")
# plt.title("after bilateral blurring")
# plt.show()

# #Eroding and Dilating
# kernel=np.ones((1,1),np.uint8)
# img_erode=cv2.erode(img_bb,kernel,iterations=3)
# img_dilate=cv2.erode(img_erode,kernel,iterations=3)
# plt.imshow(img_dilate)
# plt.axis("off")
# plt.title("After eroding and dilating")
# plt.show()





#styling of the image 

img_style=cv2.stylization(img, sigma_s=150,sigma_r=0.25)
plt.imshow(img_style)
plt.axis("off")
plt.title("CARTOON")
plt.show()


