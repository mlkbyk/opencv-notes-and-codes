import cv2  # Import OpenCV library
import numpy as np

# Start the webcam capture
capture = cv2.VideoCapture(0)

# Check if the webcam is accessible, otherwise exit the program
if not capture.isOpened():
    print("Unable to access webcam.")  # Error message in case webcam can't be accessed
    exit()

# Get the resolution of the webcam feed
width = int(capture.get(cv2.CAP_PROP_FRAME_WIDTH))  # Frame width
height = int(capture.get(cv2.CAP_PROP_FRAME_HEIGHT))  # Frame height

# Start an infinite loop to process the video stream
while True:
    isTrue, frame = capture.read()

    # If the frame can't be fetched, print an error message and exit the loop
    if not isTrue:
        print("Unable to fetch the frame from the camera!")
        break

    # Draw a line from top-left to bottom-right
    img = cv2.line(frame, (0, 0), (width, height), (252, 15, 192), 10)  # Initial point (0, 0), Final point (width, height)
    
    # Draw a rectangle that covers the entire frame
    img = cv2.rectangle(img, (0, 0), (width, height), (200, 162, 200), 15)  # Top-left (0, 0), Bottom-right (width, height)
    
    # Draw a circle in the center of the frame
    img = cv2.circle(img, (int(width / 2), int(height / 2)), 60, (255, 209, 223), -1)  # Center (width/2, height/2), Radius 60

    # Add text to the frame (font style, font size, color, thickness)
    font = cv2.FONT_HERSHEY_SIMPLEX  # Font style selection
    img = cv2.putText(img, 'Lovely Day Lovely Person', (200, height - 10), font, 1.0, (0, 0, 0), 5)  # Add text

    # Display the modified frame
    cv2.imshow('Webcam', img)

    # Exit the loop if 'a' key is pressed
    if cv2.waitKey(1) == ord('a'):
        break

# Release the webcam and close all OpenCV windows
capture.release()
cv2.destroyAllWindows()
