import cv2
from matplotlib import pyplot as plt

img = cv2.imread(r"C:\Users\STUDENT\Downloads\dragon2.jpg")


bgr_image = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)


blur = cv2.GaussianBlur(bgr_image, (5, 5),0)


plt.subplot(121), plt.imshow(bgr_image), plt.title('Original')
plt.xticks([]), plt.yticks([])

plt.subplot(122), plt.imshow(blur), plt.title('Gaussian Blur')
plt.xticks([]), plt.yticks([])

plt.show()