import cv2
import numpy as np
import face_recognition

imgCeo = face_recognition.load_image_file('TrainingImageLabel/ceo.jpg')
imgCeo = cv2.cvtColor(imgCeo, cv2.COLOR_BGR2RGB)
imgTest = face_recognition.load_image_file('TrainingImageLabel/julie.jpg')
imgTest = cv2.cvtColor(imgTest, cv2.COLOR_BGR2RGB)

faceLoc = face_recognition.face_locations(imgCeo)[0]
encodeCeo = face_recognition.face_encodings(imgCeo)[0]
cv2.rectangle(imgCeo,(faceLoc[3], faceLoc[0], faceLoc[1], faceLoc[2]), (255,0, 255), 2)

faceLocTest = face_recognition.face_locations(imgTest)[0]
encodeTest = face_recognition.face_encodings(imgTest)[0]
cv2.rectangle(imgTest,(faceLoc[3], faceLoc[0], faceLoc[1], faceLoc[2]), (255,0, 255), 2)

results = face_recognition.compare_faces([encodeCeo], encodeTest)
faceDis = face_recognition.face_distance([encodeCeo], encodeTest)
print(results, faceDis)
cv2.putText(imgTest, f'{results}{round(faceDis[0], 2)}', (50,50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 2)


cv2.imshow('Sundar Pichai', imgCeo)
cv2.imshow('Sundar Pichai test', imgTest)
cv2.waitKey(0)