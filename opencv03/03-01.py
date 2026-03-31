import cv2
import numpy as np

src = cv2.imread('lena.jpg')

# 평균 블러 (5x5 커널)
dst_avg = cv2.blur(src, (5, 5))

# 가우시안 블러 (5x5 커널, 표준편차 0=자동)
dst_gaussian = cv2.GaussianBlur(src, (5, 5), 0)

# 미디언 블러 (커널 크기 5)
dst_median = cv2.medianBlur(src, 5)

cv2.imshow('Original', src)
cv2.imshow('Gaussian', dst_gaussian)
cv2.waitKey(0)
cv2.destroyAllWindows()