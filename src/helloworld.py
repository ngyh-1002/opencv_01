import cv2

# 이미지를 불러오는 명령어
image = cv2.imread('../img/like_lenna.png')

# 이미지를 변환하는 명령어
image_small = cv2.resize(image, (100, 100))

# 이미지를 보여주는 명령어
# cv2.imshow('Image Window', image)
cv2.imshow('Image Window', image_small)

# 창을 유지시키는 명령어
cv2.waitKey(0)
cv2.destroyAllWindows()