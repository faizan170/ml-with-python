import cv2
import numpy as np
image = cv2.imread("imgs/two.png")

image = cv2.resize(image, None, fx=0.5, fy=0.5)

image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

                                            #image #thresh, #
thres, image_thresh_binary = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)

th2 = cv2.adaptiveThreshold(image, 255, cv2.ADAPTIVE_THRESH_MEAN_C,
            cv2.THRESH_BINARY,19,2)

th3 = cv2.adaptiveThreshold(image,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
            cv2.THRESH_BINARY,11,2)


print("Threshold value:", thres)

cv2.imshow("image", image)
cv2.imshow("image_thresh_binary", image_thresh_binary)
cv2.imshow("th2", th2)
cv2.imshow("th3", th3)
cv2.waitKey(0)
cv2.destroyAllWindows()