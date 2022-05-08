from turtle import end_fill
import numpy as np
import cv2
from matplotlib import pyplot as plt

# read a cracked sample image
img = cv2.imread('sample.jpg')

# Convert into gray scale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Image processing ( smoothing )
# Averaging
blur = cv2.blur(gray,(3,3))

# Apply logarithmic transform
img_log = (np.log(blur+1)/(np.log(1+np.max(blur))))*255

# Specify the data type
img_log = np.array(img_log,dtype=np.uint8)
# Image smoothing: bilateral filter
bilateral = cv2.bilateralFilter(img_log, 5, 75, 75)

# Canny Edge Detection
edges = cv2.Canny(bilateral,100,200)

# Morphological Closing Operator
kernel = np.ones((5,5),np.uint8)
closing = cv2.morphologyEx(edges, cv2.MORPH_CLOSE, kernel)

cv2.imwrite('detected.jpg', closing)

plt.subplot(121),plt.imshow(img)
plt.title('Original'),plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(closing,cmap='gray')
plt.title('Output Image'),plt.xticks([]), plt.yticks([])
plt.show()

k=0
for item in closing:
#     print(item)
    for i in item:
        if i==255:
            k=k+1
# print(k)            

if k>1000:
    m=True
else:
    m=False
if m==True:
    ii = np.where(closing==255)
    a = np.array(ii)
# print(a)
#     print(a.shape)
#     h1 = a[0][0]
#     h2 = a[0][k-1]
#     l1 = a[1][0]
#     l2 = a[1][k-1]
#     h = h2-h1
#     l = l2-l1
#     print(h1,h2,l1,l2,h,l)