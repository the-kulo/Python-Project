import cv2
import numpy as np

kernel = np.ones((3, 3), np.uint8)

img = cv2.imread('dog.jpg')
img = cv2.resize(img, (0, 0), fx=1, fy=1)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(img, (11, 11), 10)
canny = cv2.Canny(img, 150, 200)
dilate = cv2.dilate(canny,  kernel, iterations=1)

cv2.imshow('img', img)
cv2.imshow('gray', gray)
cv2.imshow('blur', blur)
cv2.imshow('canny', canny)
cv2.imshow('dilate', dilate)

cv2.waitKey(0)
