import cv2
import numpy as np
from matplotlib import pyplot as plt
def nothing(i):
    print(i)

cv2.namedWindow("image")
cv2.createTrackbar('x',"image",0,100,nothing)
cv2.createTrackbar('y',"image",0,100,nothing)


while(True):
    img = cv2.imread("media/balu_f.jpg")
    img = cv2.resize(img, (960,540))
    x=cv2.getTrackbarPos('x',"image")
    y=cv2.getTrackbarPos('y',"image")
    canny= cv2.Canny(img,x,y)
    cv2.imshow("image",img)
    cv2.imshow("image",canny)

    k = cv2.waitKey(1)
    if (k == 27):
        break

cv2.destroyAllWindows()