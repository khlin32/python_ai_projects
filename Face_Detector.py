import cv2
#from random import randrange

# Load some pre-trained data on face frontals from opencv (haar cascade algorithm)
trained_face_data = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
#trained_face_data = cv2.CascadeClassifier('haarcascade_smile.xml')

# no of faces detected
numberFaces = 0

# Choose an image to detect face in
#img = cv2.imread('TomBrady.jpg')
#img = cv2.imread('LinFamily_1.png')
img = cv2.imread('Show_1.jpg')

# Convert it to grayscale
grayscaled_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Detech faces
face_coordinates = trained_face_data.detectMultiScale(grayscaled_img)
#print(face_coordinates)

# Draw rectangles around the faces
for (x, y, w, h) in face_coordinates:
    cv2.rectangle(img, (x,y), (x+w, y+h), (0, 255, 0), 2)
    numberFaces += 1

# Display the image
print("There are " + str(numberFaces) + " faces detected.")
cv2.imshow("Face Detected", img)

# Wait a bit
cv2.waitKey()

print("Code Completed")