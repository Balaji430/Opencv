import cv2
import matplotlib.pyplot as plt

img = cv2.imread('media/balu_f.jpg', -1)
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

plt.imshow(img)
plt.xticks([]), plt.yticks([])
plt.show()
cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()