#PLOT IMAGE on page
#1
import cv2
from matplotlib import pyplot as plt
img=cv2.imread('photo path')
plt.imshow(img,cmap='Greens')
plt.xticks([0]),plt.yticks([])
plt.show()




















