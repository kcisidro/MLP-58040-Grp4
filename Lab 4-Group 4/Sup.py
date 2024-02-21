import cv2
import numpy as np
import matplotlib.pyplot as plt

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    if not ret:
        break

    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    blur_img = cv2.GaussianBlur(gray_frame, (5, 5), 0)

    sobelxy = cv2.Sobel(gray_frame, cv2.CV_64F, 1, 1, ksize=5)
    filtered_image_sobelxy = np.abs(sobelxy).astype(np.uint8)

    edges = cv2.Canny(gray_frame, 100, 200, apertureSize=5)

    laplacian = cv2.Laplacian(gray_frame, cv2.CV_64F)
    filtered_image_laplacian = np.abs(laplacian).astype(np.uint8)

    # Create a 2x2 subplot
    plt.subplot(2, 2, 1)
    plt.imshow(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
    plt.axis('off')
    plt.text(225, 50, 'Original', color='white')

    plt.subplot(2, 2, 2)
    plt.imshow(filtered_image_sobelxy, cmap='gray')
    plt.axis('off')
    plt.text(225, 50, 'Sobel', color='white')

    plt.subplot(2, 2, 3)
    plt.imshow(edges, cmap='gray')
    plt.axis('off')
    plt.text(225, 50, 'Canny', color='white')

    plt.subplot(2, 2, 4)
    plt.imshow(filtered_image_laplacian, cmap='gray')
    plt.axis('off')
    plt.text(225, 50, 'Laplacian', color='white')

    # Show the plots
    plt.show(block=False)
    plt.pause(0.1)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the capture
cap.release()
cv2.destroyAllWindows()
plt.close('all')
