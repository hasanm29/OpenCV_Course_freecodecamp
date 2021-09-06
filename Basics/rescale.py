import cv2 as cv



# Will work for Images, Videos and Live Videos
def rescaleFrame(frame, scale=0.75):#scale=0.75 is by default
    
    width  = int(frame.shape[1]* scale)# frame.shape[1] is width of the frame/image. we r converting float to int as height & width are int
    height = int(frame.shape[0]* scale)# frame.shape[0] is height of the frame/image

    dimensions = (width,height)
    return cv.resize(frame,dimensions,interpolation=cv.INTER_AREA)

# Only works on Live Video
def changeRes(width,height):
    capture.set(3,width)
    capture.set(4,height)

# Reading Images
# img = cv.imread('Resources/Photos/cat.jpg')
# cv.imshow('Cat',img)
# resized_image = rescaleFrame(img)
# cv.imshow('Resized Image',resized_image)
# cv.waitKey(0)


#Reading Videos
capture = cv.VideoCapture('Resources/Videos/dog.mp4')

while True:
    isTrue, frame = capture.read() #reading video frame by frame; isTrue boolean saying file successfully read or not
    # frame_resized = rescaleFrame(frame)
    frame_resized = rescaleFrame(frame,scale=.2)

    cv.imshow('Video',frame)#display individual fram
    cv.imshow('Video Resized',frame_resized)
    if cv.waitKey(20)& 0xFF==ord('d'): #0xFF==ord('d')--> means if letter d is pressed break the loop
        break

capture.release()
cv.destroyAllWindows()