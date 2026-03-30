import cv2
import numpy as np

# 흰 도화지 이미지 만들기
canvas = np.full((512, 512, 3), 255, dtype=np.uint8)


# 왼쪽 버튼 클릭한 상태로 마우스 움직이면 검은색 점이 이어 그려진다
def mouse_callback(event, x, y, flags, param):
    if event == cv2.EVENT_MOUSEMOVE:
        if flags == cv2.EVENT_FLAG_LBUTTON:
            cv2.circle(canvas, (x, y), 3, (0, 0, 0), -1)


while True:
    cv2.imshow('Canvas', canvas)
    cv2.setMouseCallback('Canvas', mouse_callback)
    key = cv2.waitKey(10)  # 10ms 만큼 키 입력을 기다린다
    if key == ord('c'):
        canvas = np.full((512, 512, 3), 255, dtype=np.uint8)
    elif key == ord('q') or key == 27:  # 27은 ESC 의 코드
        break

cv2.destroyAllWindows()