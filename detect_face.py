import os

from cv2.cv2 import CascadeClassifier, imread, cvtColor, COLOR_BGR2GRAY


def detect_face(image_path):
    # Get user supplied values
    casc_path = os.path.join(os.path.dirname(__file__), "haarcascade_frontalface_default.xml")

    # Create the haar cascade
    face_cascade = CascadeClassifier(casc_path)

    # Read the image
    image = imread(image_path)
    gray = cvtColor(image, COLOR_BGR2GRAY)

    # Detect faces in the image
    faces = face_cascade.detectMultiScale(
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
        return x, y, x + w, y + h

    return None
