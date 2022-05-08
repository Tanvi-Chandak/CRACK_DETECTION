from matplotlib import pyplot as plt
import cv2
import numpy as np
from cv2 import imshow
cam = cv2.VideoCapture(0)
image = cam.read()
# img = np.ar
a=[]
for item in image:
   a.append(np.asarray(item))
# print(a)
img = a[1]
img = np.array(img,dtype=np.uint8)
# print(img)
# type(img)
cv2.imwrite('sample.jpg', img)
print(img)
plt.imshow(img)