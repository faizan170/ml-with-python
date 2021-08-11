import cv2
import numpy as np
image = cv2.imread("imgs/one.png")

image = cv2.resize(image, None, fx=0.5, fy=0.5)

#h, w, c = image.shape
#image = cv2.resize(image, (int(w/2), int(h/2)))

h, w, _ = image.shape
fx = 100
fy = 50
M = np.float32([
    [1, 0.1, fx],
    [0.1, 1, fy]
])
image1 = cv2.warpAffine(image, M, (w + fx, h + fy))


fx, fy = -50, -150
M = np.float32([
    [1, 0, fx],
    [0, 1, fy]
])
image2 = cv2.warpAffine(image, M, (w, h + fy))


# Translation of images
cv2.imshow("image", image1)
cv2.imshow("image2", image2)
cv2.waitKey(0)
cv2.destroyAllWindows()