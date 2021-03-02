import numpy as np
import cv2

img = cv2.imread('media/messi5.jpg')
img3 = cv2.imread('media/balu.jpg')
#cv2.imshow('Image', img)

face =img[60:140,200:270]
ball = img[286:400,330:400]
img2 = img.copy()
img2[270:326, 119:189] = ball
img2[200:280, 145:215] = face
img3 = cv2.resize(img3,(960,540))

print(ball.shape)
print(face.shape)
print(img3.shape)
print(img3.shape[1]/img3.shape[0])
cv2.imshow('Image', img3)
#cv2.imshow('Face', face)

cv2.waitKey(0)
cv2.destroyAllWindows()