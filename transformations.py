import cv2 as cv
import numpy as np

img = cv.imread('Resources/Photos/Park.jpg')
cv.imshow('Park',img)

# 1. Translation
# Translation is shifting an image along the X and Y axis
def translate(img, x, y):
    transMatrix = np.float32([[1,0,x],[0,1,y]])
    dimensions = (img.shape[1], img.shape[0])#img.shape[1] is the width and img.shape[0] is the height
    return cv.warpAffine(img,transMatrix, dimensions)
# -x ---> Left # -y ---> UP #  x ---> Right #  y ---> Down

# translated = translate(img,-100,-100)
# cv.imshow('Translate',translated)

# 2. Rotation
# Rotate image by an angle
def rotate(img, angle, rotPoint=None):
    (height,width) = img.shape[:2]

    if rotPoint is None:
        rotPoint = (width//2, height//2)

    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
    dimensions = (width,height)

    return cv.warpAffine(img, rotMat, dimensions)

# rotated = rotate(img,45)
# cv.imshow('Rotate',rotated)

# rotate the rotated image

# rotated_rotated = rotate(rotated,45)
# cv.imshow('Rotated Rotated', rotated_rotated)


# 3. Resizing
resized = cv.resize(img, (500,500), interpolation= cv.INTER_CUBIC)
cv.imshow('Resized',resized)
cv.waitKey(0)