import numpy as np
import cv2



ones = np.ones((3,3), np.float32) / 25

image = cv2.imread("images/RtNrs.png")

image_filtered = cv2.filter2D(image, -1, ones)



# Blur Images
ones = np.ones((3,3), np.float32) / 9
blurred_image = cv2.filter2D(image, -1, ones)


blurred_image_2 = cv2.blur(image, (3,3))



cv2.imshow("image", image)
cv2.imshow("image_filtered", image_filtered)

cv2.imshow("blurred_image", blurred_image)
cv2.imshow("blurred_image_2", blurred_image_2)


cv2.waitKey(0)

cv2.destroyAllWindows()