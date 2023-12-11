import cv2
import sys

input_path = sys.argv[1]
output_path = sys.argv[2]

img = cv2.imread(input_path, 0)
edges = cv2.Canny(img, 100, 200)

cv2.imwrite(output_path, edges)
