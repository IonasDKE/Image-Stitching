import numpy as np
!pip install opencv-python
import cv2
import skimage as sk

# Load the 2 images
left_img = cv2.imread('leftImage.png')
right_img = cv2.imread('rightImage.png')

# harrys corner detection
features_left = sk.feature.corner_harris(left_img)
features_right = sk.feature.corner_harris(right_img)

print(features_left, features_right)