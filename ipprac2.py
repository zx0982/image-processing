import cv2
path = "download.jfif"
img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
cv2.imshow('Divyani Karadbhajne',img)
cv2.waitKey(0)
cv2.destroyAllWindows()