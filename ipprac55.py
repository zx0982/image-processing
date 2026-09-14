import cv2

# Read the noisy image
img = cv2.imread("noise image1.png")

# Apply Median Blur
median = cv2.medianBlur(img, 5)   # Kernel size = 5

# Display images
cv2.imshow("Original Image", img)
cv2.imshow("Median Blur Image", median)

# Save the output
cv2.imwrite("car_median_blur.jpg", median)

cv2.waitKey(0)
cv2.destroyAllWindows()