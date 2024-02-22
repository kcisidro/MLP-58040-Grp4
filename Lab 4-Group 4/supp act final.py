import cv2
import numpy as np
import matplotlib.pyplot as plt

cap = cv2.VideoCapture(0)

def camera_filter(frame):
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    blur_img = cv2.GaussianBlur(gray_frame, (5, 5), 0)
    sobelxy = cv2.Sobel(gray_frame, cv2.CV_64F, 1, 1, ksize=5)
    filtered_image_sobelxy = np.abs(sobelxy).astype(np.uint8)
    edges = cv2.Canny(gray_frame, 100, 200, apertureSize=5)
    laplacian = cv2.Laplacian(gray_frame, cv2.CV_64F)
    filtered_image_laplacian = np.abs(laplacian).astype(np.uint8)

    return frame, filtered_image_sobelxy, edges, filtered_image_laplacian

if not cap.isOpened():
    print("Error in Camera")
    exit()

fig, axes = plt.subplots(2, 2, figsize=(10, 8))

filter_names = ['Original', 'Sobel XY', 'Canny Edge', 'Laplacian Edge']

fps = 60
interval = int(1000 / fps)

def plotting(frame):
    filter_frames = camera_filter(frame)

    for ax, img, filter_name in zip(axes.flat, filter_frames, filter_names):
        labeled_image = cv2.putText(img.copy(), filter_name, (225, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 1,
                                   cv2.LINE_AA)

        if labeled_image.shape[-1] == 1:
            ax.imshow(labeled_image, cmap='gray')
        else:
            ax.imshow(cv2.cvtColor(labeled_image, cv2.COLOR_BGR2RGB), cmap='gray')

        ax.axis("off")

def update_frame():
    ret, frame = cap.read()
    if not ret:
        plt.close('all')
        return

    plotting(frame)
    plt.pause(0.001)

while True:
    update_frame()

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()  # Release OpenCV window properly
plt.show()
