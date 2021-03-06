import os
import cv2 as cv
import numpy as np

#Create list of people manually
people = ['Ben Afflek','Elton John', 'Jerry Seinfield','Madonna','Mindy Kaling'] 
DIR = r'C:\Users\naimu\Desktop\OpenCV_Course_freecodecamp\Resources\Faces\train'
haar_cascade = cv.CascadeClassifier('haar_face.xml')
#Create the list using code
# p = []
# for i in os.listdir(r'Resources\Faces\train'):
#     p.append(i)
# print(p) #This gives the same list as people

features = []
labels = []


def create_train():
    for person in people:
        path = os.path.join(DIR,person)
        label = people.index(person)

        for img in os.listdir(path):
            img_path = os.path.join(path,img)

            img_array = cv.imread(img_path)
            gray = cv.cvtColor(img_array,cv.COLOR_BGR2GRAY)

            faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=4)

            for (x,y,w,h ) in faces_rect:
                faces_roi = gray[y:y+h, x:x+w] #roi-->region of interest
                features.append(faces_roi)
                labels.append(label)

create_train()
print('Training done ---------------------')
# print(f'Length of the featrues =  {len(features)}')
# print(f'Length of the labels =  {len(labels)}'

# convert features and labels list to numpy arrays
features = np.array(features, dtype= 'object')
labels = np.array(labels)
face_recognizer = cv.face.LBPHFaceRecognizer_create()

#Trian the Recognizer on the features list and the labels list
face_recognizer.train(features,labels)

face_recognizer.save('face_trained.yml')
np.save('features.npy',features)
np.save('labels.npy',labels)