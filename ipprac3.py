import cv2
import numpy as np
img1 = cv2.imread('download.jpg')
img2 = cv2.imread('images.jpg')
dest_or = cv2.bitwise_or(img2, img1, mask = None)
cv2.imshow('Bitwise OR',dest_or)
if cv2.waitKey(0) & 0xff == 27:
    cv2.destroyAllWindows()