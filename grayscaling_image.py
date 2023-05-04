import cv2

# Using the cv2.imread() function with flag = zero 
image = 'image-cropped-8x10.jpg'

img = cv2.imread(image, 0)
cv2.imshow('gray_scale', img)

original = cv2.imread(image)
cv2.imshow('original', original)

cv2.waitKey(0)
