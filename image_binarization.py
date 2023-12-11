import cv2
import sys

input_path = sys.argv[1]
output_path = sys.argv[2]

img = cv2.imread(input_path, 0)
ret, thresh = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)

cv2.imwrite(output_path, thresh)
