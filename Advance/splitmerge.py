import cv2 as cv
import numpy as np
img = cv.imread('Resources/Photos/Park.jpg')
cv.imshow('Park',img)

blank = np.zeros(img.shape[:2],dtype='uint8')

b,g,r = cv.split(img)
# cv.imshow('Blue',b)
# cv.imshow('Green',g)
# cv.imshow('Red',r)

blue = cv.merge([b,blank,blank]) #Blue Color chanel
green = cv.merge([blank,g,blank])#Green Color chanel
red = cv.merge([blank,blank,r])#Red Color chanel

cv.imshow('Blue',blue)
cv.imshow('Green',green)
cv.imshow('Red',red)

print("Shape of img:",img.shape)
print("Shape of Blue:",b.shape)
print("Shape of Green",g.shape)
print("Shape of Red:",r.shape)

merged = cv.merge([b,g,r])
cv.imshow('Merged Image',merged)

cv.waitKey(0)