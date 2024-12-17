import cv2 as cv
img_path="resources/images.png"
img=cv.imread(img_path,1)
img=cv.resize(img,(0,0),fx=2,fy=2)

cv.imshow('Kitty',img)
cv.waitKey(0)
cv.destroyAllWindows()
