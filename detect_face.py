import os
import cv2

def detect_face(imagePath):

    # Get user supplied values
    cascPath = os.path.join(os.path.dirname(__file__), "haarcascade_frontalface_default.xml")

    # Create the haar cascade
    faceCascade = cv2.CascadeClassifier(cascPath)

    # Read the image
    image = cv2.imread(imagePath)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Detect faces in the image
    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30)
        # flags = cv2.CV_HAAR_SCALE_IMAGE
    )

    for (x, y, w, h) in faces:
        y = y - (h * 0.3)
        h = h * 1.6
        x = x - (w * 0.3)
        w = w * 1.6
        return (x, y, x + w, y + h)

    return None