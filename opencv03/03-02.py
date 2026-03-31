# 평균 필터 직접 구현한 버전
import cv2
import numpy as np

def mean_blur(img):
    dst = np.zeros(img.shape, dtype=np.uint8)
    height, width = img.shape

    for y in range(1, height - 1):
        for x in range(1, width - 1):
            region = img[y-1:y+2, x-1:x+2]
            value = np.mean(region)
            dst[y, x] = int(value)

    return dst

lena_gray = cv2.imread("lena.jpg", cv2.IMREAD_GRAYSCALE)
cv2.imshow("Lena", lena_gray)
cv2.imshow("Mean Blur", mean_blur(lena_gray))
cv2.waitKey()
cv2.destroyAllWindows()