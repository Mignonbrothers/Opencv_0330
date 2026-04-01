import cv2
import numpy as np

# Define various colors
colors = [(255, 0, 0), (255, 0, 255), (0, 255, 0), (0, 0, 255), (0, 255, 255)]

# Select a default color
color_index = 0
color = colors[color_index]

# Minimum allowed area for the contour
min_area = 1000

# Create videocapture object
cap = cv2.VideoCapture(0)

# Create a blank canvas
canvas = np.zeros((480, 640, 3), dtype="uint8")
#canvas = np.zeros((500, 660, 3), dtype="uint8")

# Color range for detecting Blue color
lower_blue = np.array([100, 150, 50])
upper_blue = np.array([140, 255, 255])

previous_center_point = 0

if cap.isOpened():
    print("카메라가 잡혔어요!")
else:
    print("카메라가 안 잡혔어요 ㅠㅠ")



while True:
    # Read each frame from webcam
    ret, frame = cap.read()

    if not ret:
        break

    # Flip the frame
    frame = cv2.flip(frame, 1)

    # Convert the frame BGR to HSV color space
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Create a binary segmented mask of green color
    mask = cv2.inRange(hsv, lower_blue, upper_blue)

    # Add some dialation to increase segmented area
    mask = cv2.dilate(mask, None, iterations=2)

    # Show the mask
    cv2.imshow("mask", mask)

    # Use bitwise
    result = cv2.bitwise_and(frame, frame, mask = mask)

    cv2.imshow("RESULT", result)

    # Find all the contours of the segmented mask
    contours, h = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # Checking if any contour is detected then run the following statements
    if len(contours) > 0:

        # Get the biggest contour from all the detected contours
        cmax = max(contours, key=cv2.contourArea)

        # Find the area of the contour
        area = cv2.contourArea(cmax)

        if area > min_area:
            # Find center point of the contour
            M = cv2.moments(cmax)
            cX = int(M["m10"] / M["m00"])
            cY = int(M["m01"] / M["m00"])

            # Drawing a circle in the center of the contour area
            cv2.circle(frame, (cX, cY), 10, (0, 0, 255), 2)

            if previous_center_point == 0:
                if cY < 65:
                    # Clear all
                    if cX > 20 and cX < 120:
                        canvas = np.zeros((height, width, 3), np.uint8)

                    elif cX > 140 and cX < 220:
                        color = colors[0]
                    elif cX > 240 and cX < 320:
                        color = colors[1]

                    elif cX > 340 and cX < 420:
                        color = colors[2]

                    elif cX > 440 and cX < 520:
                        color = colors[3]

                    elif cX > 540 and cX < 620:
                        color = colors[4]

            # If drawing is started then draw a line between each frames detected contour center point
            if previous_center_point != 0:
                cv2.line(canvas, previous_center_point, (cX, cY), color, 2)

            # Update the center point
            previous_center_point = (cX, cY)

        else:
            previous_center_point = 0

    # Adding the canvas mask to the original frame
    canvas_gray = cv2.cvtColor(canvas, cv2.COLOR_BGR2GRAY)

    _, canvas_binary = cv2.threshold(canvas_gray, 20, 255, cv2.THRESH_BINARY_INV)

    canvas_binary = cv2.cvtColor(canvas_binary, cv2.COLOR_GRAY2BGR)
    frame = cv2.bitwise_and(frame, canvas_binary)
    frame = cv2.bitwise_or(frame, canvas)


    cv2.imshow("frame", frame)

    cv2.imshow("Canvas", canvas)

    # Selecting the color for drawing in the canvas

    # Adding the colour buttons to the live frame for colour access

    #cv2.putText(frame, "YELLOW", (555, 33), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA)

    # 프레임당 딱 한 번만 키 입력을 받아서 key 변수에 저장 (비트 연산 & 0xFF는 오류 방지용)
    key = cv2.waitKey(30) & 0xFF

    if key == ord('c'):
        canvas = np.zeros((480, 640, 3), dtype="uint8")
        print("Canvas cleared")

    elif key == ord('p'):
        # 인덱스를 1 증가시키고, colors 리스트의 길이(5)로 나눈 나머지를 구합니다.
        # 이렇게 하면 0 -> 1 -> 2 -> 3 -> 4 -> 다시 0으로 빙글빙글 돕니다!
        color_index = (color_index + 1) % len(colors)

        # 바뀐 인덱스를 적용해서 진짜 색상을 바꿔줍니다.
        color = colors[color_index]
        print(f"Color changed! Current index: {color_index}")

    elif key == 27:  # ESC 키
        break

cap.release()
cv2.destroyAllWindows()