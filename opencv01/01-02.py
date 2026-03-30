import cv2
import sys

# 이미지 불러오기 (넘파이 배열)
img = cv2.imread(r'C:\python-opencv\lena.jpg')

if img is None:
    print("이미지를 찾을 수 없습니다.")

cv2.imshow("lena Noona", img)


# 키 입력 기다리기... 키 입력 없으면 현 상태로 유지됨
cv2.waitKey(0)
cv2.destroyAllWindows()