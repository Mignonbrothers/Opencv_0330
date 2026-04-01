import cv2
import numpy as np

src = cv2.imread('lena.jpg')
val = 100

dst1 =  cv2.add(src, (val, val, val, 0))

dst2 = src + val

cv2.imshow('OpenCV Add', dst1)
cv2.imshow('Numpy Add', dst2)
cv2.waitKey(0)
cv2.destroyAllWindows()