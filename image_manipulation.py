# This code provides basic information about images and demonstrates simple image manipulation.
import cv2

# Load an image from the specified path
img = cv2.imread('resources/kitty2.png')

# Printing the image's pixel data as a matrix. Each element in the matrix represents a pixel in the image.
# For a color image, each pixel contains three values (B, G, R) corresponding to its Blue, Green, and Red intensity levels.
print(img)

# Display the type of the image object. OpenCV stores images as NumPy arrays.
# NumPy is a Python library used for numerical computations and supports efficient operations on multi-dimensional arrays.
print(type(img))  # Output: <class 'numpy.ndarray'>

# Print the shape of the image array.
# The shape returns three values:
# - Number of rows (height of the image in pixels)
# - Number of columns (width of the image in pixels)
# - Number of channels (color information: e.g., 3 for a BGR color image)
print(img.shape)

# Explanation of the shape:
# Rows = Height of the image in pixels
# Columns = Width of the image in pixels
# Channels = Color space of the image (e.g., 3 for RGB/BGR)

# You can modify pixel values in the image, which effectively changes the image itself.
# For example, let's select a rectangular region of the image and copy it to another location.

# Selecting a small region (from row 131 to 150 and column 71 to 85).
# This region is stored in the variable 'tag'.
tag = img[131:150, 71:85]

# Overwriting another region (from row 50 to 69 and column 10 to 24) with the selected region.
img[50:69, 10:24] = tag

# Display the modified image in a window.
cv2.imshow('Kit', img)

# Wait indefinitely for a key press before closing the window.
cv2.waitKey(0)

# Close all OpenCV windows.
cv2.destroyAllWindows()
