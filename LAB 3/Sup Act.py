import cv2
from matplotlib import pyplot as plt

# Load the original image
img = cv2.imread(r"C:\Users\STUDENT\Downloads\dragon2.jpg")
bgr_image = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)

# Apply different blurs
blur_averaging = cv2.blur(bgr_image, (5, 5))
blur_gaussian = cv2.GaussianBlur(bgr_image, (5, 5), 0)
blur_median = cv2.medianBlur(bgr_image, 5)
blur_bilateral = cv2.bilateralFilter(bgr_image, 9, 75, 75)

# Create a 3x3 grid plot
plt.figure(figsize=(6, 6))

plt.subplot(331), plt.imshow(blur_averaging)
plt.text(10, 10, 'Averaging', color='black', fontsize=11, ha='left', va='top')
plt.xticks([]), plt.yticks([])

plt.subplot(333), plt.imshow(blur_gaussian)
plt.text(10, 10, 'Gaussian Blur', color='black', fontsize=11, ha='left', va='top')
plt.xticks([]), plt.yticks([])

plt.subplot(337), plt.imshow(blur_median)
plt.text(10, 10, 'Median Blur', color='black', fontsize=11, ha='left', va='top')
plt.xticks([]), plt.yticks([])

plt.subplot(339), plt.imshow(blur_bilateral)
plt.text(10, 10, 'Bilateral Filtering', color='black', fontsize=11, ha='left', va='top')
plt.xticks([]), plt.yticks([])

plt.subplot(335), plt.imshow(bgr_image)
plt.text(10, 10, 'Original', color='black', fontsize=11, ha='left', va='top')
plt.xticks([]), plt.yticks([])

plt.tight_layout()
plt.show()
