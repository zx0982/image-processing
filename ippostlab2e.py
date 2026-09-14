import cv2

# Reads the image
img = cv2.imread('flower.jfif')

# Converts to HSV color space
img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)



# Shows the image
cv2.imshow('image CS24203', img)

cv2.waitKey(0)
cv2.destroyAllWindows()
