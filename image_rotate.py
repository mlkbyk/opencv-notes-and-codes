import cv2
img_path="resources/kitty2.png"
img=cv2.imread(img_path,1)
img=cv2.rotate(img,cv2.ROTATE_90_COUNTERCLOCKWISE)
cv2.imwrite('new_img.jpg',img) #this line create new file that included edited version.

cv2.imshow('BUNNY',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
