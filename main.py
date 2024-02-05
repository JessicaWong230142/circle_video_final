import cv2
import numpy as np
from image_processing import image_processing

#reads img file in full color
video = cv2.VideoCapture('circle1.MOV')

while True:
    image_processing(video)

video.release()
cv2.destroyAllWindows()
