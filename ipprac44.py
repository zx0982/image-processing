import numpy as np
import cv2 as cv
img = cv.imread('download.jpg', 0)
cropped_img = img[100:300, 100:300]
cv.imwrite('Divyani Karadbhajne.jpg',cropped_img)
cv.waitKey(0)
cv.destroyAllWindows()