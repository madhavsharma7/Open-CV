#face Track
import numpy as np
import cv2
face_cascade = cv2.CascadeClassifier ('E:\\Python codes\\OpenCV\\haarcascade_frontalface_default.xml')
img=cv2.imread('man.jfif')
gray = cv2.cvtColor (img, cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale (gray, scaleFactor=1.1,minNeighbors=5)
for (x,y,w,h) in faces:
    roi_gray=gray [y:y+h, x:x+w]
    roi_color= img [y:y+h, x:x+w]
cv2.imshow('img', img)
cv2.imshow('img1',roi_gray)
cv2.imshow('img2', roi_color)
cv2.waitKey(0)
cv2.destroyAllWindows()
