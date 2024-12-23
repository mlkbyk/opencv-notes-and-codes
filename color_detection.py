import numpy as np
import cv2 as cv

# Initialize the video capture (0 for the default camera)
capture = cv.VideoCapture(0)

while True:
    # Read a frame from the video source
    isTrue, frame = capture.read()
    if not isTrue:  # Break if no frame is captured
        break

    # Convert the frame from BGR to HSV color space
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

    # Define the lower and upper ranges for the red color (1st range)
    lower_red_1 = np.array([0, 50, 50])
    upper_red_1 = np.array([10, 255, 255])

    # Define the lower and upper ranges for the red color (2nd range)
    lower_red_2 = np.array([170, 50, 50])
    upper_red_2 = np.array([180, 255, 255])

    # Create masks for the two red color ranges
    mask1 = cv.inRange(hsv, lower_red_1, upper_red_1)
    mask2 = cv.inRange(hsv, lower_red_2, upper_red_2)

    # Combine the two masks to cover the entire red range
    red_mask = mask1 | mask2

    # Apply the mask to the original frame to extract the red areas
    result = cv.bitwise_and(frame, frame, mask=red_mask)

    # Display the result in a window
    cv.imshow('Frame', result)

    # Break the loop if the 'q' key is pressed
    if cv.waitKey(1) == ord('q'):
        break

# Release the video capture object and close all OpenCV windows
capture.release()
cv.destroyAllWindows()
