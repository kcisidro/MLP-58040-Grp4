import cv2
from matplotlib import pyplot as plt

img = cv2.imread(r"C:\Users\STUDENT\Downloads\dragon2.jpg")
bgr_image = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)

blur = cv2.bilateralFilter(bgr_image, 9, 75, 75)


plt.subplot(121), plt.imshow(bgr_image), plt.title('Original')
plt.xticks([]), plt.yticks([])

plt.subplot(122), plt.imshow(blur), plt.title('Bilateral Filtering')
plt.xticks([]), plt.yticks([])
plt.show()