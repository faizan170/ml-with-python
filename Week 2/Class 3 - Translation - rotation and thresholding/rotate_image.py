import cv2
import numpy as np
image = cv2.imread("imgs/one.png")



image = cv2.resize(image, (800, 500))
h, w, _ = image.shape

M = cv2.getRotationMatrix2D(((w-1)/2.0, (h-1)/2.0), 10, 1)

image1 = cv2.warpAffine(image, M, (w, h))


cv2.imshow("image", image)
cv2.imshow("image1", image1)
cv2.waitKey(0)
cv2.destroyAllWindows()