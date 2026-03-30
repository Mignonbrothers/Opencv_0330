import cv2
import numpy as np

# 사이즈가 다르면 연산 시 오류가 발생할 수 있다.
img = cv2.imread("clapped.jpg")
img = cv2.resize(img, (512, 512))
img1 = cv2.imread("lena.jpg")

cv2.imshow("Original", img)

cv2.imshow("Original1", img1)

# 초록 배경에 해당하는 영역만 누끼딴다
mask = cv2.inRange(img, (0, 120, 0), (100, 255, 100))
mask_inv = cv2.bitwise_not(mask)

cv2.imshow("Modify", mask)
cv2.imshow("Modify2", mask_inv)

op = cv2.copyTo(img, mask_inv, img1)

cv2.imshow("Result", op)

cv2.waitKey(0)
cv2.destroyAllWindows()