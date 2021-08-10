import cv2
import numpy as np

# D:/one/two/basic_operation

# D:/one/Screenshot (115).png



image = cv2.imread("Screenshot (115).png")
image2 = cv2.imread("frames/frame_1.jpg")

print(image.shape)

b,g,r = cv2.split(image)

img = cv2.merge((r, g, b))

# Flip
image = cv2.flip(image, 1)



#image = cv2.resize(image, (500, 500))

h,w, c = image.shape
image1 = cv2.resize(image2, (w, h))
# concatenate
resp = np.concatenate((image, image1), axis=1)

cv2.imshow("img", resp)
cv2.waitKey(0)
cv2.destroyAllWindows()
