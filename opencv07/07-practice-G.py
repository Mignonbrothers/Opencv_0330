import cv2
import numpy as np
import random


def main():
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("웹캠 열기 실패 ㅠ.ㅠ")
        return

    ret, frame = cap.read()
    if not ret:
        print("첫 프레임 읽기 실패 ㅠ.ㅠ")
        return

    canvas = np.zeros_like(frame)  # 실제 그림이 그려질 이미지

    prev_center = None  # 이동할 때마다 위치를 백업하여 시작점을 갱신

    # 빨간색 검출하는 범위
    lower_b = np.array([0, 100, 100])
    upper_b = np.array([10, 255, 255])

    kernel = np.ones((5, 5), np.uint8)

    print("키 입력 가이드 : 펜 지우기는 c, 펜 색상 바꾸기는 p, 종료는 q")

    # 순수하게 랜덤한 색상 선정
    pen_color = [random.randint(0, 255) for i in range(3)]

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        frame = cv2.flip(frame, 1)  # 좌우 반전 (거울 효과)

        # 색상 검출에 유리한 색상 표현법으로 변환하기
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        # 원하는 색상 검출 후 노이즈 제거 및 객체 강조
        mask = cv2.inRange(hsv, lower_b, upper_b)
        mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel, iterations=1)
        mask = cv2.morphologyEx(mask, cv2.MORPH_DILATE, kernel, iterations=1)

        contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        center = None

        if contours:
            # 경계 영역의 면적이 가장 큰 경계(컨투어)를 찾는다
            largest = max(contours, key=cv2.contourArea)
            area = cv2.contourArea(largest)  # 면적 구함

            if area > 700:
                M = cv2.moments(largest)  # 중심좌표를 구하기 위해 행렬구함
                if M["m00"] != 0:
                    cx = int(M["m10"] / M["m00"])
                    cy = int(M["m01"] / M["m00"])
                    center = (cx, cy)

                    # 점을 따라 그리기
                    cv2.circle(frame, center, 7, (255, 0, 0), -1)
                    cv2.circle(canvas, center, 7, pen_color, -1)

                    # 선을 따라 그리기
                    # if prev_center is not None:
                    # cv2.line(canvas, prev_center, center, pen_color, 5)

        prev_center = center

        # 중심점만 추적하는 원본 영상 frame
        # 실제로 그림을 그려나가는 복사 영상 canvas
        # 둘을 합치는 작업!
        output = cv2.addWeighted(frame, 0.8, canvas, 0.8, 0)

        cv2.imshow("Output", output)

        key = cv2.waitKey(1) & 0xFF
        if key == ord('q'):
            break
        elif key == ord('c'):
            canvas[:] = 0
            prev_center = None
        elif key == ord('p'):
            pen_color = [random.randint(0, 255) for i in range(3)]

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()