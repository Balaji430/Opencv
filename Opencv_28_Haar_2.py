import cv2

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
# Read the input image
img = cv2.imread('media/balu_f.jpg')
img = cv2.resize(img,(960,540))

#gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(img, 1.1, 4)

for (x, y , w ,h) in faces:
    cv2.rectangle(img, (x,y), (x+w, y+h), (255, 0 , 0), 3)

# Display the output
    cv2.imshow('img', img)

cv2.waitKey(0)
cv2.destroyAllWindows()

