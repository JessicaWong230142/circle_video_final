import cv2
import numpy as np
from image_processing import image_processing

#reads img file in full color
video = cv2.VideoCapture('circle1.MOV')

#runs the image_processing function and breaks out of it if error
while True:
    image_processing(video)

#makes each frame appear and then destroys
video.release()
cv2.destroyAllWindows()
