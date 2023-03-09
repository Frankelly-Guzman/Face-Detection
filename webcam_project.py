# import the opencv library
import cv2
import pathlib

# initialize the classifier
cascade_path = pathlib.Path(cv2.__file__).parent.absolute() / "data/haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(str(cascade_path))

# define a webcameo capture object
webcam = cv2.VideoCapture(0)

while(True):
    
    # Capture the webcam frames
    # by frames
    ret, frames = webcam.read()
    
    gray = cv2.cvtColor(frames, cv2.COLOR_BGR2GRAY)
    
    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
        flags=cv2.CASCADE_SCALE_IMAGE
    )
    
    # Draw a rectangle around the faces
    for (x, y, w, h) in faces:
        cv2.rectangle(frames, (x, y), (x+w, y+h), (0, 255, 0), 2)
    
    # Display the resulting frames
    cv2.imshow('Video', frames)
    
    # the 'q' button is set as the 
    # quitting button you may use any
    # desired button of your choice
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
# After the loop release the cap object
webcam.release()
# Destroy all the windows
cv2.destroyAllWindows()