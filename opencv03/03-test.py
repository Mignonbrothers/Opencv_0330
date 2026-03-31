# 3, 4번은 GEMINI 참조


import cv2
import numpy as np

pts = []


def mouse_handler(event, x, y, flags, param):
    global pts, dst, rows, cols

    if event == cv2.EVENT_LBUTTONUP:
        print('클릭한 좌표: %d, %d' % (x, y))
        pts.append([x, y])

        # 클릭한 곳에 빨간 점 그리기
        cv2.circle(dst, (x, y), 5, (0, 0, 255), -1)
        cv2.imshow('src', dst)

        # 점이 딱 4개가 모였을 때 투시 변환 실행 (GEMINI)
        if len(pts) == 4:
            print("4개의 점이 모두 선택되었습니다. 이미지를 변환합니다.")

            # 1. 클릭한 4개의 좌표 (arr1) - 리스트를 numpy 배열로 변환
            arr1 = np.float32(pts)

            # 2. 변환될 결과물 이미지의 4개 좌표 (arr2)
            # 순서는 클릭하는 순서와 동일하게 매칭되어야 합니다.
            # (좌측 상단 -> 우측 상단 -> 우측 하단 -> 좌측 하단 순서로 클릭한다고 가정)
            arr2 = np.float32([[0, 0], [cols, 0], [cols, rows], [0, rows]])

            # 3. 변환 행렬 구하기
            matrix = cv2.getPerspectiveTransform(arr1, arr2)

            # 4. 이미지 펴기 (결과를 result 변수에 저장)
            result = cv2.warpPerspective(dst, matrix, (cols, rows))

            # 결과 출력
            cv2.imshow("result", result)


img = cv2.imread("screen.jpg")

dst = cv2.resize(img, (512, 512))
rows, cols, channels = dst.shape

cv2.imshow("src", dst)

# 마우스 콜백 함수 등록
cv2.setMouseCallback('src', mouse_handler)

print("이미지에서 4개의 점을 '좌상 -> 우상 -> 우하 -> 좌하' 순서로 클릭하세요.")

cv2.waitKey(0)
cv2.destroyAllWindows()