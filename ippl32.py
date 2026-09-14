import cv2
img = cv2.imread('batman.jfif')
t_lower = 100
t_upper = 200
aperture_size = 5
edge = cv2.Canny(img, t_lower, t_upper,
                 apertureSize=aperture_size)
cv2.imshow('original CS24203', img)
cv2.imshow('edge CS24203', edge)
cv2.waitKey(0)
cv2.destroyAllWindows()
