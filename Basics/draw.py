import cv2 as cv
import numpy as np

# img = cv.imread('Resources/Photos/cat.jpg')
# cv.imshow('Cat',img)

#Create a blank image
blank = np.zeros((500,500,3),dtype='uint8') # uint8 is a data type of an image. np.zeros((height,width,number_of_color_channels))
# cv.imshow('Blank',blank)

# 1. Paint the image a color
# blank[:] = 0,255,0
# blank[200:300, 300:400] = 0,0,255
# cv.imshow('Red',blank)

# 2. Draw a Rectangle
# cv.rectangle(blank,(0,0), (250,250),(255,0,0), thickness=2)
# cv.rectangle(blank,(0,0), (250,250),(255,0,0), thickness=-1) #WE Can do this to fill the rectangle intead of cv.FILLED as following
# cv.rectangle(blank,(0,0), (250,400),(255,0,0), thickness=cv.FILLED)
# cv.rectangle(blank,(0,0), (blank.shape[1]//2,blank.shape[0]//2),(255,0,0), thickness=-1)
# cv.imshow('Rectangle',blank)

# 3. Draw a Circle
# cv.circle(blank,(blank.shape[1]//2, blank.shape[0]//2), 40, (0,0,255),thickness= 3)
# cv.imshow('Circle',blank)

# 4. Draw a Line
# cv.line(blank,(0,0), (blank.shape[1]//2, blank.shape[0]//2),(0,0,255),thickness=3)
# cv.imshow('Line',blank)

# 5. Write Text on Image
cv.putText(blank,'Hello, My name is Naimul',(0,255), cv.FONT_HERSHEY_TRIPLEX, 1.0, (0,255,0),2)
cv.imshow('Text',blank)

cv.waitKey(0)