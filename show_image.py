import cv2

# read the image using imread() method
img = cv2.imread('image-cropped-8x10.jpg', 1)

# show the image using imshow() method 
cv2.imshow('Dog image', img)

cv2.waitKey(0)
