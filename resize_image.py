import cv2
import numpy as np

img = cv2.imread('image-cropped-8x10.jpg')

resize = cv2.resize(img,(250, 250))

cv2.imshow('re-size', resize)
cv2.imshow('image', img)

cv2.waitKey(0)