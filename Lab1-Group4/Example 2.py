import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("C:\\Users\\STUDENT\\Downloads\\asdasd.jpg", cv2.IMREAD_COLOR)

plt.imshow(img)

plt.waitforbuttonpress()
plt.close('all')
