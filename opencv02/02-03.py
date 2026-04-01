import cv2

src1 = cv2.imread("lena.jpg", cv2.IMREAD_GRAYSCALE)

# 임계점
ret, src2 = cv2.threshold(src1, 160, 255, cv2.THRESH_BINARY)
dst = cv2.bitwise_and(src1, src2)


cv2.imshow("src1", src1)
cv2.imshow("src2", src2)
cv2.imshow("dst", dst)
cv2.waitKey(0)
cv2.destroyAllWindows()

#print(src.shape)