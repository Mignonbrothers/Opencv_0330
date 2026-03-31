# 아핀 변환
import cv2

img = cv2.imread("lena.jpg")
rows, cols, channels = img.shape

# 중심좌표, 회전각도, 확대축소비
arr1 = cv2.getRotationMatrix2D((rows/2, cols/2), 45, 0.5)
arr2 = cv2.getRotationMatrix2D((rows/2, cols/2), -45, 1.2)

# 변환행렬을 이미지에 적용하기 함수
dst1 = cv2.warpAffine(img, arr1, (cols, rows))
dst2 = cv2.warpAffine(img, arr2, (cols, rows))

cv2.imshow("dst1", dst1)
cv2.imshow("dst2", dst2)
cv2.waitKey(0)
cv2.destroyAllWindows()


