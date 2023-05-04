import cv2
import numpy as np

img = cv2.imread('image-cropped-8x10.jpg')

cv2.imshow('original image', img)


# Gaussian Blur
gaussian = cv2.GaussianBlur(img, (7,7), 0)

# Median Blur
median = cv2.medianBlur(img, 9)

# Bilateral Blur
bilateral = cv2.bilateralFilter(img, 9, 75, 75)
cv2.imshow('Bilateral Blurring', bilateral)
cv2.imshow('gaussian blur', gaussian)
cv2.imshow('median blur', median)
cv2.waitKey(0)