import cv2


face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

sticker = cv2.imread("tigermask.png", cv2.IMREAD_UNCHANGED)


cap = cv2.VideoCapture(0)

if cap.isOpened() :
    print("카메라가 잡혔어요!")
else :
    print("카메라가 안 잡혔어요ㅠㅠ")

while True :
    ret, frame = cap.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

    for (x, y, w, h) in faces:
        #cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
        sticker_resized = cv2.resize(sticker, (w, h * 2))

        y_offset = y - h // 3
        if y_offset < 0:
            y_offset = 0

        sticker_h, sticker_w, _ = sticker_resized.shape
        for i in range(sticker_h):
            for j in range(sticker_w):
                if sticker_resized[i, j][3] != 0:
                    frame[y_offset + i, x + j] = sticker_resized[i, j][:3]




    if not ret :
        break

    #cv2.imshow("frame", frame)

    cv2.imshow("frame", frame)

    if cv2.waitKey(30) == 27:
        break


cap.release()
cv2.destroyAllWindows()