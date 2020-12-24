# File to test OpenCV functionality, run filters on video and display it

import cv2 as cv
import numpy as np

import utils
import filters

cap = cv.VideoCapture(0)
if not cap.isOpened():
    print("Cannot open camera")
    exit()
while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    # if frame is read correctly ret is True
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    # Our operations on the frame come here
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    fil = filters.central_x()
    gray = utils.apply_filter_intensity(gray,fil)

    # Display the resulting frame
    cv.imshow('frame',gray)
    if cv.waitKey(1) == ord('q'):
        break

# When everything is done, release the capture
cap.release()
cv.destroyAllWindows()