import cv2
img = cv2.imread('lena.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

template = gray[180:290, 200:360]


res = cv2.matchTemplate(gray, template, cv2.TM_CCOEFF_NORMED)
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

# max_loc이 매칭된 위치의 좌상단 좌표
top_left = max_loc

print(top_left)

gray = cv2.circle(gray, top_left, 5, (0, 0, 0), -1)

cv2.imshow("gray", gray)
cv2.imshow("template", template)
cv2.waitKey(0)
cv2.destroyAllWindows()