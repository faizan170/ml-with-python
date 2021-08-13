import cv2

image = cv2.imread("images/base.png")
template = cv2.imread("images/template.png")
h, w, _ = template.shape

response = cv2.matchTemplate(image, template, cv2.TM_CCOEFF_NORMED)

_, _, min_loc, max_loc = cv2.minMaxLoc(response)


bottom_right = (max_loc[0] + h, max_loc[1] + w)

cv2.rectangle(image, max_loc, bottom_right, (255, 0,0), 4)

cv2.imshow("image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()

