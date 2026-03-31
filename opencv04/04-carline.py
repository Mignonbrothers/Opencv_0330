import cv2
import numpy as np

src = cv2.imread('rail.jpg')
#gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)


cv2.imshow('src', src)

pin = cv2.GaussianBlur(src, (3, 3), 0)

cv2.imshow('pin', pin)

# 에지 검출

edges = cv2.Canny(src, 270, 300)

# 직선 성분 검출
lines = cv2.HoughLinesP(edges, 1, np.pi/180, 90, minLineLength=180, maxLineGap=10)

# 컬러 영상으로 변경 (영상에 빨간 직선을 그리기 위해)
dst = cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR) # 컬러로 변환해 그리기


if lines is not None:
    for line in lines:
        x1, y1, x2, y2 = line[0]
        cv2.line(dst, (x1, y1), (x2, y2), (0, 0, 255), 2)


cv2.imshow('dst', dst)

# det = cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)

# cv2.imshow('det', det)
#for sigma in range(1, 4):




cv2.waitKey(0)
cv2.destroyAllWindows()