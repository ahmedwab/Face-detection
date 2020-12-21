import cv2


# Capturing the Video Stream
webcam = cv2.VideoCapture(0)


# Creating the cascade objects
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

while True:
    # Get frame
    _, frame = webcam.read()
    # Covert the frame to grayscale
    image = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
	# Find the faces
    detected = face_cascade.detectMultiScale(image=image, scaleFactor=1.3, minNeighbors=4)
    for (x, y, width, height) in detected:
        cv2.rectangle(frame,(x, y),(x + width, y + height),(52, 235, 149),thickness=3)
    
    # Display amount of faces
    text ='Faces:'+str(len(detected))
    cv2.putText(frame, text, (00, 185) , cv2.FONT_HERSHEY_PLAIN, 4, (0, 0, 0) , 2, cv2.LINE_AA, False) 


    # Display the frame
    cv2.imshow('Body and Face Detection', frame)

    #close upon escape
    if cv2.waitKey(1) == 27:
        webcam.release()
        cv2.destroyAllWindows()
        break

