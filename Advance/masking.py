import cv2 as cv
import numpy as np

img = cv.imread('Resources/Photos/cats.jpg')
cv.imshow('Cats',img)
# Masking allows to focus on wherever we want to

blank = np.zeros(img.shape[:2],dtype='uint8')#dimension of the mask has to be same as that img
cv.imshow('Blank Image',blank)

mask = cv.circle(blank,(img.shape[1]//2,img.shape[0]//2),100,255,-1)
cv.imshow('Mask',mask)

#Masked Image
masked = cv.bitwise_and(img,img,mask=mask)
cv.imshow('Masked Image',masked)

cv.waitKey(0)