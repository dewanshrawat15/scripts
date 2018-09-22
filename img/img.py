import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('img.jpg')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

corners = cv2.goodFeaturesToTrack(gray,25,0.01,10)
corners = np.int(corners)

for i in corners:
    x,y = i.ravel()
    cv2.circle(img,(x,y),3,255)

plt.imshow(img),plt.show()