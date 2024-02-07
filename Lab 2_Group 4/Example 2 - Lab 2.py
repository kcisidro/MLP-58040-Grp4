import cv2 as cv

cap = cv.VideoCapture(r"C:\Users\STUDENT\PycharmProjects\pythonProject8\output.avi")

while cap.isOpened():
    ret, frame = cap.read()

    if not ret:
        print("Can't receive frame (stream end?). Exiting....")
        break

    cv.imshow('frame', frame)

    if cv.waitKey(30) == ord('q'):
        break

cap.release()
cv.destroyAllWindows()
