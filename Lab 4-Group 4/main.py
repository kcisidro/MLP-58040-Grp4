import cv2
import matplotlib.pyplot as plt
import numpy as np

cap = cv2.VideoCapture(0)

ret, frame = cap.read()

if ret:
    # Convert the original frame to grayscale
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    blur_img = cv2.GaussianBlur(gray_frame, (5, 5), 0)

    sobelx = cv2.Sobel(src=blur_img, ddepth=cv2.CV_64F, dx=1, dy=0, ksize=5)
    sobely = cv2.Sobel(src=blur_img, ddepth=cv2.CV_64F, dx=0, dy=1, ksize=5)
    sobelxy = cv2.Sobel(src=blur_img, ddepth=cv2.CV_64F, dx=1, dy=1, ksize=5)

    # Scale and convert the Sobel images to uint8
    filtered_image_x = cv2.convertScaleAbs(sobelx)
    filtered_image_y = cv2.convertScaleAbs(sobely)
    filtered_image_xy = cv2.convertScaleAbs(sobelxy)

    plt.figure(figsize=(20, 20))

    plt.subplot(221)
    plt.imshow(gray_frame, cmap='gray')
    plt.title('Original Image')
    plt.axis("off")

    plt.subplot(222)
    plt.imshow(filtered_image_x, cmap='gray')
    plt.title('Sobel X')
    plt.axis("off")

    plt.subplot(223)
    plt.imshow(filtered_image_y, cmap='gray')
    plt.title('Sobel Y')
    plt.axis("off")

    plt.subplot(224)
    plt.imshow(filtered_image_xy, cmap='gray')
    plt.title('Sobel XY')
    plt.axis("off")

    plt.show()

# Release the camera
cap.release()

# Close all OpenCV windows
cv2.destroyAllWindows()