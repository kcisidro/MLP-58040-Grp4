import cv2 as cv

def record_and_save():
    cap = cv.VideoCapture(0)
    fourcc = cv.VideoWriter_fourcc(*'XVID')
    out = cv.VideoWriter('Merge.avi', fourcc, 30.0, (640, 480))

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            print("Can't receive frame (stream end?). Exiting...")
            break

        cv.imshow('frame', frame)
        out.write(frame)

        key = cv.waitKey(1)
        if key == ord('q'):
            break

    cap.release()
    out.release()
    cv.destroyAllWindows()

def play_saved_video():
    cap = cv.VideoCapture(r"C:\Users\STUDENT\PycharmProjects\pythonProject8\Merge.avi")

    while cap.isOpened():
        ret, frame = cap.read()

        if not ret:
            print("Can't receive frame (stream end?). Exiting....")
            break

        cv.imshow('frame', frame)

        key = cv.waitKey(30)
        if key == ord('q'):
            break

    cap.release()
    cv.destroyAllWindows()

# Main loop
while True:
    print("Press 1 to Record video and press q to save, Press 2 to play saved video, Press 3 to exit.")
    choice = input("Enter your choice: ")

    if choice == '1':
        record_and_save()
    elif choice == '2':
        play_saved_video()
    elif choice == '3':
        break
    else:
        print("Invalid choice. Please enter 1, 2, or q.")
