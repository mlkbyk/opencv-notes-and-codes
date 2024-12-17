import cv2 as cv

img_path="resources/kitty2.png"
img=cv.imread(img_path)
dimensions=(500,600)
img=cv.resize(img,dimensions)
cv.imshow('Kitty',img)
cv.waitKey(0)
cv.destroyAllWindows()




