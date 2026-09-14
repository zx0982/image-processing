import cv2
import matplotlib.pyplot as plt

# Read image in grayscale
img = cv2.imread("noise image1.png", cv2.IMREAD_GRAYSCALE)

# Apply Gaussian Blur
restored = cv2.GaussianBlur(img, (5, 5), 0)

# Show results
plt.subplot(1, 2, 1)
plt.imshow(img, cmap='gray')
plt.title("Gaussian Noisy")
plt.axis("off")

plt.subplot(1, 2, 2)
plt.imshow(restored, cmap='gray')
plt.title("Restored (Gaussian Blur)")
plt.axis("off")

plt.show()