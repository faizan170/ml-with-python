import numpy as np
import cv2
import os

image= cv2.imread("images/opening.png", 0)
h,w = image.shape

w = int(w/2)

image = image[:, :w]



kernel = np.ones((5,5), np.uint8)

MORPH_OPEN = cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel)


MORPH_OPEN = np.concatenate((image, MORPH_OPEN), axis=1)

cv2.imshow("image", image)
cv2.imshow("MORPH_OPEN", MORPH_OPEN)
cv2.waitKey(0)
cv2.destroyAllWindows()
