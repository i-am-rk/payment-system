import cv2 as cv 
import numpy as np 
import random
import sys

red = (0, 0, 255)
green = (0, 255, 0)
blue = (255, 0, 0)
randomColor = (random.randint(0, 255), 
               random.randint(0, 255),
               random.randint(0, 255))



img = cv.imread('binary.jpg')
img = cv.resize(img, (500, 300))
img2 = img.copy()

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
ret, thresh = cv.threshold(gray, 100, 255, cv.THRESH_BINARY_INV)
contours, hierarchy = cv.findContours(thresh, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
cv.drawContours(img2, contours, -1, blue, 2)

cv.imshow('original Image', img)
cv.imshow('Gray Image', gray)
cv.imshow('Thresh Image', thresh)
cv.imshow('contours Image',img2)

print(hierarchy)

cv.waitKey(0) 
cv.destroyAllWindows()
