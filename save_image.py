import cv2
import os

img = cv2.imread('image-cropped-8x10.jpg')

# path to store image 
directory_path = r'C:\Users\thego\Desktop\picture'

# To change current directory to specified directory

os.chdir(directory_path)

# using imwrite() function to save the image in new directory
cv2.imwrite('Dog.jpg', img)
print(os.listdir(directory_path))
