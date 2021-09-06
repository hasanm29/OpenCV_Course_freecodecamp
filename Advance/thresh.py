import cv2 as cv


img = cv.imread('Resources/Photos/cats.jpg')
cv.imshow('Cats', img)
# Thresholding is the binarization of an image
# convert an image to binary image that is where pixels of the image are 0/ black and 255/ white

gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('Gray',gray)



# Simple Thresholding
threshold, thresh = cv.threshold(gray, 150, 255,cv.THRESH_BINARY )
cv.imshow('Simple Threshold', thresh)

threshold, thresh_inv = cv.threshold(gray, 150, 255,cv.THRESH_BINARY_INV )
cv.imshow('Simple Threshold Inverse', thresh_inv)



# Adaptive Thresholding

# adaptive_thresh = cv.adaptiveThreshold(gray,255,cv.ADAPTIVE_THRESH_MEAN_C,cv.THRESH_BINARY,11,3)
adaptive_thresh = cv.adaptiveThreshold(gray,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C,cv.THRESH_BINARY_INV,11,9)
cv.imshow('Adaptive Trhesholding',adaptive_thresh)
cv.waitKey(0)