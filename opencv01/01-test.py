import cv2
import numpy as np
import sys

# 이미지의 크기를 설정임
canvas = np.full((512, 512, 3), 255, dtype=np.uint8)

# 그림판을 여는 함수
cv2.imshow('Canvas', canvas)


def onMouse(event, x, y, flags, param):


    global oldx, oldy

    # 왼쪽 마우스 버튼을 누르면서 기록되는 좌표
    if event == cv2.EVENT_LBUTTONDOWN:
        oldx, oldy = x, y
        print('EVENT_LBUTTONDOWN: %d, %d' % (x, y))

    # 왼쪽 마우스 버튼을 때면 기록되는 좌표
    elif event == cv2.EVENT_LBUTTONUP:
        print('EVENT_LBUTTONUP: %d, %d' % (x, y))

    # 왼쪽 마우스를 움직이면서 기록되는 좌표
    elif event == cv2.EVENT_MOUSEMOVE:
        if flags & cv2.EVENT_FLAG_LBUTTON:
            cv2.line(canvas, (oldx, oldy), (x, y), (0, 0, 0), 4, cv2.LINE_AA)
            cv2.imshow('Canvas', canvas)
            oldx, oldy = x, y

cv2.setMouseCallback('Canvas', onMouse) # 마우스 콜백 함수를 GUI 윈도우에 등록


while True:
    # 그림판 초기화
    if cv2.waitKey() == ord('c'):
        canvas[:] = (255, 255, 255)

    # 강제 종료
    elif cv2.waitKey(0) & 0xff == 27:
        break

    # 강제 종료
    elif cv2.waitKey() == ord('q'):
        break

    # 그 이외 키인 경우 메시지 작성
    else:
        print("다시")


# 그림판 종료 함수
cv2.destroyAllWindows()