import cv2
import numpy as np

new_height = 300
new_width =  300


# 이미지를 불러오는 명령어
image = cv2.imread('../img/like_lenna.png')

# 이미지를 변환하는 명령어
image_small = cv2.resize(image, (100, 100))

dst = np.zeros((new_height, new_width), dtype = np.uint8)
dst = cv2.resize(image_small, (new_width, new_height), dst = dst)
# 이미지를 보여주는 명령어
# cv2.imshow('Image Window', image)
cv2.imshow('resized Image', dst)
# cv2.imshow('Image Window', image_small)

# 창을 유지시키는 명령어
cv2.waitKey(0)
cv2.destroyAllWindows()