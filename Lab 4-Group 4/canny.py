import cv2
import matplotlib.pyplot as plt
import numpy as np

cap = cv2.VideoCapture(0)

ret, frame = cap.read()

if ret:
    # Convert the original frame to grayscale
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    blur_img = cv2.GaussianBlur(gray_frame, (5, 5), 0)

    # Apply the Canny edge detector
    edges = cv2.Canny(blur_img, 100, 200, apertureSize=5)

    plt.figure(figsize=(20, 10))

    plt.subplot(121)
    plt.imshow(gray_frame, cmap='gray')
    plt.title('Original Image')
    plt.axis("off")

    plt.subplot(122)
    plt.imshow(edges, cmap='gray')
    plt.title('Canny Edges')
    plt.axis("off")

    plt.show()

# Release the camera
cap.release()

# Close all OpenCV windows
cv2.destroyAllWindows()