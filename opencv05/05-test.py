import cv2
import numpy as np

src = cv2.imread('coins.jpg')

cv2.imshow('src', src)

gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
aim, thresh = cv2.threshold(gray, 200, 255, cv2.THRESH_BINARY)

#cv2.imshow('a', a)
cv2.imshow('thresh', thresh)

blur = cv2.GaussianBlur(gray, (5, 5), 0)
bim, thresh = cv2.threshold(blur, 200, 255, cv2.THRESH_BINARY)

cv2.imshow('thresh_mod', thresh)
cv2.imshow('Original', blur)


kernel = np.ones((5, 5), np.uint8)

# 침식
erosion = cv2.erode(blur, kernel, iterations=1)

# 팽창
dilation = cv2.dilate(blur, kernel, iterations=1)

# 열림
result = cv2.morphologyEx(blur, cv2.MORPH_CLOSE, kernel)
result = cv2.dilate(result, kernel, iterations=1)

cv2.imshow("erosion", erosion)
cv2.imshow("dilation", dilation)
cv2.imshow("result", result)


contours, hierarchy = \
cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

result1 = cv2.drawContours(result, contours, -1, (0, 200, 0), 1)

cv2.imshow("result1", result1)

result2 = cv2.drawContours(src, contours, -1, (0, 200, 0), 1)

cv2.imshow("result2", result2)


# cv2.imshow('src', src)
cv2.waitKey(0)
cv2.destroyAllWindows()