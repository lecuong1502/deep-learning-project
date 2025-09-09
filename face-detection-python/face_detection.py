import cv2

# Load the pre-trained Haar Cascade classifiers for face and eye detection
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')

# Capture frames from the default camera (0)
cap = cv2.VideoCapture(0)

while 1:
    ret, img = cap.read()  # Read a frame from the camera
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # Convert the frame to grayscale
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)  # Detect faces in the grayscale frame

    for (x, y, w, h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,255,0),2) 
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]

        # Detect eyes within the region of interest (the detected face)
        eyes = eye_cascade.detectMultiScale(roi_gray)
        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,127,255),2)

    cv2.imshow('img',img)  # Display the frame with detected faces and eyes

    k = cv2.waitKey(30) & 0xff
    if k == 27:  # Exit the loop if the 'Esc' key is pressed
        break

# Close the window
cap.release()
cv2.destroyAllWindows()