import numpy as np
import cv2

img = cv2.imread('media/messi5.jpg')
img2 = cv2.imread('media/opencv-logo.png')

print(img.shape)
print(img.size)
print(img.dtype)

b,g,r = cv2.split(img)
img = cv2.merge((b,g,r))

ball = img[280:340, 330:390]
img[273:333, 100:160] = ball

img = cv2.resize(img, (512,512))
#img2 = cv2.resize(img2, (512,512))

#dst = cv2.add(img, img2) #Calculates the per-element sum of two arrays or an array and a scalar.
#dst = cv2.addWeighted(img, .1, img2, .9, 0) #Calculates the weighted sum of two arrays.

cv2.imshow('Image', img2)
cv2.waitKey(0)
cv2.destroyAllWindows()