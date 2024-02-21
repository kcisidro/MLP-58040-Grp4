import cv2
import matplotlib.pyplot as plt
import numpy as np

cap = cv2.VideoCapture(0)

ret, frame = cap.read()

if ret:
    # Convert the original frame to grayscale
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    blur_img = cv2.GaussianBlur(gray_frame, (5, 5), 0)

    # Apply Laplacian edge detection
    laplacian = cv2.Laplacian(blur_img, cv2.CV_64F)
    filtered_image = cv2.convertScaleAbs(laplacian)

    plt.figure(figsize=(20, 20))

    plt.subplot(221)
    plt.imshow(gray_frame, cmap='gray')
    plt.title('Original Image')
    plt.axis("off")

    plt.subplot(222)
    plt.imshow(filtered_image, cmap='gray')
    plt.title('Laplacian Edge Detection')
    plt.axis("off")

    plt.show()

# Release the camera
cap.release()

# Close all OpenCV windows
cv2.destroyAllWindows()