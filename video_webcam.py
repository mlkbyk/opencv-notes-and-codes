import cv2
capture = cv2.VideoCapture(0)
if not capture.isOpened():
    print("Web cam cannot open!")
    exit()

while True:
    isTrue, frame = capture.read()

    if not isTrue:
        print("Frame cannot read !")
        break

    cv2.imshow('Webcam', frame)

    if cv2.waitKey(1) & 0xFF == ord('d'):
        break

capture.release()
cv2.destroyAllWindows()
