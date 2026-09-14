import cv2
import matplotlib.pyplot as plt
import numpy as np
# Load the image
image = cv2.imread('download.jfif')
#Plot the original image
plt.subplot(1, 2, 1)
plt.title("Original")
plt.imshow(image)
# Remove noise using a median filter
filtered_image = cv2.medianBlur(image, 11)
#Save the image
cv2.imwrite('Median Blur.jpg', filtered_image)
import matplotlib.pyplot as plt
import numpy as np
# Load the image
image = cv2.imread('download.jfif')
#Plot the original image
plt.subplot(1, 2, 1)
plt.title("Original")
plt.imshow(image)
# Remove noise using a median filter
filtered_image = cv2.medianBlur(image, 11)
#Save the image
cv2.imwrite('Median Blur.jpg', filtered_image)
plt.subplot(1,2,1)
plt.title("Median Blur")
plt.imshow(filtered_image)
plt.show()