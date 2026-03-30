import cv2
import sys

def mouse_callback(event, x, y, flags, param):
    if event == cv2.EVENT_RBUTTONDBLCLK:
        print("오른쪽 버튼 더블 클릭:", x, y)


img = cv2.imread(r'C:\python-opencv\lena.jpg')

if img is None:
    print("이미지를 찾을 수 없습니다.")

cv2.namedWindow('WindowName')

cv2.imshow("Lena", img)
cv2.setMouseCallback('WindowName', mouse_callback)


cv2.waitKey(0)
cv2.destroyAllWindows()