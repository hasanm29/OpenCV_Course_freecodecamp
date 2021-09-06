import cv2 as cv

img = cv.imread('Resources/Photos/cats.jpg')
cv.imshow('Cats',img)
# We smooth an image when it has a lot of noise
# reduce noise / smooth the image using blur technique
# kernel size is number of rows and columns

# 1. Averaging
average = cv.blur(img, (3,3)) # The more the kernel size the more blur the image will be 
cv.imshow('Average Blur',average)

# 2. Gaussian Blur
gaussian = cv.GaussianBlur(img,(3,3),0) # 0 is the sigmaX or Standard Diviation in the X direction
cv.imshow('Gaussian Blur',gaussian)

# 3. Median Blur
median = cv.medianBlur(img,3)
cv.imshow('Median Blur',median)

# 4. Bilateral Blur
bilateral = cv.bilateralFilter(img,5,15,15)
cv.imshow('Bilateral Blur',bilateral)


cv.waitKey(0)