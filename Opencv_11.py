import cv2 as cv
import numpy as np

img = cv.imread('media/sudoku.png',0)
img2 = cv.imread('media/balu_f.jpg')
img2 = cv.resize(img2, (960,540))
img2 = cv.cvtColor(img2, cv.COLOR_BGR2GRAY)

#_, th1 = cv.threshold(img, 127, 255, cv.THRESH_BINARY)
#th2 = cv.adaptiveThreshold(img, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 11, 2);
#th3 = cv.adaptiveThreshold(img, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 11, 2);

_, th1_b = cv.threshold(img2, 127, 255, cv.THRESH_BINARY)
th2_b = cv.adaptiveThreshold(img2, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 11, 2);
th3_b = cv.adaptiveThreshold(img2, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 11, 2);


#cv.imshow("Image", img)
#cv.imshow("THRESH_BINARY", th1)
#cv.imshow("ADAPTIVE_THRESH_MEAN_C", th2)
#cv.imshow("ADAPTIVE_THRESH_GAUSSIAN_C", th3)

cv.imshow("Image", img2)
cv.imshow("THRESH_BINARY", th1_b)
cv.imshow("ADAPTIVE_THRESH_MEAN_C", th2_b)
cv.imshow("ADAPTIVE_THRESH_GAUSSIAN_C", th3_b)


cv.waitKey(0)
cv.destroyAllWindows()