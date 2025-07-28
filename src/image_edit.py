import cv2
import numpy as np
import random

new_height = 600
new_width = 600

# 이미지 불러오기 및 리사이즈
image = cv2.imread('../img/like_lenna.png')
dst = cv2.resize(image, (new_width, new_height))

# 랜덤 원 20개 그리기
for _ in range(50):
    i = random.randint(0, new_width - 1)
    j = random.randint(0, new_height - 1)
    R = random.randint(0, 255)
    G = random.randint(0, 255)
    B = random.randint(0, 255)
    dst = cv2.circle(dst, (i, j), 10, (B, G, R), 4, lineType=1)  # OpenCV는 BGR 순서

# 결과 출력
cv2.imshow('Image Window', dst)
cv2.waitKey(0)
cv2.destroyAllWindows()