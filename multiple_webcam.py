import cv2
import numpy as np

# Start the camera
capture = cv2.VideoCapture(0)
if not capture.isOpened():
    print("Unable to access the camera!")
    exit()

# Get frame width and height from the camera
width = int(capture.get(cv2.CAP_PROP_FRAME_WIDTH)) #these 2 lines come from chatgpt update 3=width ,4=height you can choose one of them 
height = int(capture.get(cv2.CAP_PROP_FRAME_HEIGHT)) 

while True:
    # Read a frame from the camera
    isTrue, frame = capture.read()
    if not isTrue:
        print("Unable to fetch the frame from the camera!")
        break

    # Create a blank image with the same dimensions as the frame
    image = np.zeros(frame.shape, np.uint8)

    # Resize the frame to half its size
    smaller_frame = cv2.resize(frame, (0, 0), fx=0.5, fy=0.5)

    # Assign the resized frame to four quadrants of the blank image
    image[:height // 2, :width // 2] = smaller_frame  # Top-left
    image[:height // 2, width // 2:] = smaller_frame  # Top-right
    image[height // 2:, :width // 2] = smaller_frame  # Bottom-left
    image[height // 2:, width // 2:] = smaller_frame  # Bottom-right

    # Display the resulting image in a window
    cv2.imshow('Multiple camera', image)

    # Check if the 'q' or 'Q' key is pressed, and exit the loop if so
    if cv2.waitKey(1) & 0xFF in [ord('q'), ord('Q')]:
        break

# Release the camera and close all OpenCV windows
capture.release()
cv2.destroyAllWindows()
