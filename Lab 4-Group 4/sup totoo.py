import cv2
import matplotlib.pyplot as plt
import numpy as np

cap = cv2.VideoCapture(0)

ret, frame = cap.read()

if ret:

    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    blur_img = cv2.GaussianBlur(gray_frame, (5, 5), 0)

    sobelxy = cv2.Sobel(gray_frame, cv2.CV_64F, 1, 1, ksize=5)
    filtered_image_sobelxy = cv2.convertScaleAbs(sobelxy)

    edges = cv2.Canny(gray_frame, 100, 200, apertureSize=5)

    laplacian = cv2.Laplacian(gray_frame, cv2.CV_64F)
    filtered_image_laplacian = cv2.convertScaleAbs(laplacian)

    plt.figure(figsize=(20, 20))

    plt.subplot(221)
    plt.imshow(gray_frame, cmap='gray')
    plt.title('Original Image')
    plt.axis("off")

    plt.subplot(222)
    plt.imshow(filtered_image_sobelxy, cmap='gray')
    plt.title('Sobel')
    plt.axis("off")

    plt.subplot(223)
    plt.imshow(filtered_image_laplacian, cmap='gray')
    plt.title('Laplacian')
    plt.axis("off")

    plt.subplot(224)
    plt.imshow(edges, cmap='gray')
    plt.title('Canny')
    plt.axis("off")



    plt.show()

cap.release()

cv2.destroyAllWindows()