import numpy as np
import cv2 as cv

# Resize and load the main image
img = cv.resize(cv.imread('resources/nhback1.jpeg'), (0, 0), fx=0.5, fy=0.5)

# Resize and load the template image
template = cv.resize(cv.imread('resources/templete.png'), (0, 0), fx=0.5, fy=0.5)

# Get height and width of the template
h, w = template.shape[:2]

# List of template matching methods
methods = [cv.TM_CCOEFF, cv.TM_CCOEFF_NORMED, cv.TM_CCORR,
           cv.TM_CCORR_NORMED, cv.TM_SQDIFF, cv.TM_SQDIFF_NORMED]

for method in methods:
    img2 = img.copy()  # Create a copy of the main image

    # Apply the template matching algorithm
    result = cv.matchTemplate(img2, template, method)

    # Get minimum and maximum values and their locations in the result
    min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)

    # Select the best match location based on the method
    if method in [cv.TM_SQDIFF, cv.TM_SQDIFF_NORMED]:
        location = min_loc  # For these methods, the best match is at the minimum value
    else:
        location = max_loc  # For other methods, the best match is at the maximum value

    # Calculate the bottom-right corner of the rectangle
    bottom_right = (location[0] + w, location[1] + h)

    # Draw a rectangle around the detected template
    cv.rectangle(img2, location, bottom_right, 255, 5)

    # Display the result
    cv.imshow("Match", img2)
    cv.waitKey(0)
    cv.destroyAllWindows()
