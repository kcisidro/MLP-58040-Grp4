import cv2

path = r'C:\\Users\\STUDENT\\Downloads\\asdasd.jpg'

img = cv2.imread("C:\\Users\\STUDENT\\Downloads\\asdasd.jpg", cv2.IMREAD_GRAYSCALE)

cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
