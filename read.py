import cv2 as cv

#Reading Images


img = cv.imread('Resources/Photos/cat.jpg') #Read image file
# img = cv.imread('Resources/Photos/cat_large.jpg') # It will go off screen as the image file size is too Big
#Display image as a new window. First parameter is name of the window, 2nd parameter is matrix of the image
cv.imshow('Cat',img)
#keyboard binding func. wait for infinite amount of time if value is 0
cv.waitKey(0)

#write a new file
# k = cv.waitKey(0) 
# if k == ord("s"):
#     cv.imwrite("savedCatImage.png",img)

"""
#Reading Videos
capture = cv.VideoCapture('Resources/Videos/dog.mp4')

while True:
    isTrue, frame = capture.read() #reading video frame by frame; isTrue boolean saying file successfully read or not
    cv.imshow('Video',frame)#display individual fram

    if cv.waitKey(20)& 0xFF==ord('d'): #0xFF==ord('d')--> means if letter d is pressed break the loop
        break

capture.release()
cv.destroyAllWindows()
"""

"""
-215:Assertion failed ---> This error in the terminal means openCV couldn't get a media file in the given location
Video is run out of frames.
"""

