import cv2
#from random import randrange

# Load some pre-trained data on face frontals from opencv (haar cascade algorithm)
# trained_face_data = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Choose an image to detect face in
img = cv2.imread('TomBrady.jpg')

# Display the image
cv2.imshow("Face Detected", img)

# Wait a bit
cv2.waitKey()

print("Code Completed")