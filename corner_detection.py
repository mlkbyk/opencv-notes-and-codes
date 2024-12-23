import numpy as np
import cv2 as cv

# Load the image from the specified path
img = cv.imread('resources/chess_board.png')

# Resize the image by scaling it 2 times in both x and y directions
img = cv.resize(img, (0, 0), fx=2.0, fy=2.0)

# Convert the image to grayscale for corner detection
gray_scaled_pic = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# Detect up to 50 corners using Shi-Tomasi corner detection method
corners = cv.goodFeaturesToTrack(gray_scaled_pic, 50, 0.1, 10)

# Convert the detected corners to integer values for easier usage
corners = corners.astype(int)

# Draw circles at the detected corner points
for corner in corners:
    x, y = corner[0]  # Extract x, y coordinates from the corner array
    cv.circle(img, (x, y), 5, (255, 0, 0), -1)  # Draw a blue circle with radius 5

# Draw lines connecting each pair of detected corners
for i in range(len(corners)):
    for j in range(i + 1, len(corners)):
        corner1 = tuple(corners[i][0])  # Convert corner1 to tuple (x, y)
        corner2 = tuple(corners[j][0])  # Convert corner2 to tuple (x, y)
        cv.line(img, corner1, corner2, (53, 94, 59), 1)  # Draw a green line

# Display the image with the detected corners and lines
cv.imshow('Pic', img)

# Wait for any key press to close the window
cv.waitKey(0)
cv.destroyAllWindows()
