import cv2
import sys
import numpy as np

input_path = sys.argv[1]
output_path = sys.argv[2]

img = cv2.imread(input_path)

kernel_size = 5
kernel = np.ones((kernel_size, kernel_size), np.uint8)

eroded_img = cv2.erode(img, kernel, iterations=1)

cv2.imwrite(output_path, eroded_img)
