import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread('Resources/Photos/Park.jpg')
cv.imshow('Park', img)

#Using matplotlib to display image with RGB color format instead of BGR(default color format of OpenCV)
# plt.imshow(img)
# plt.show()



# 1. BGR to Grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray',gray)

# 2. BGR to HSV
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow('HSV',hsv)

# 3. BGR to L*a*b
lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
cv.imshow('LAB',lab)

# 4. BGR to RGB
rgb = cv.cvtColor(img,cv.COLOR_BGR2RGB)
cv.imshow('RGB',rgb)

plt.imshow(rgb)
plt.show()

# 5. HSV to BGR
hsv_bgr = cv.cvtColor(hsv,cv.COLOR_HSV2BGR)
cv.imshow('HSV-->BGR',hsv_bgr)

# 6. LAB to BGR
lab_bgr = cv.cvtColor(lab,cv.COLOR_LAB2BGR)
cv.imshow('LAB-->BGR',lab_bgr)


cv.waitKey(0)