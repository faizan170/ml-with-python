import cv2
import numpy as np

image = cv2.imread("images/0.jpg")

image2 = cv2.imread("azurem-train-deploy - Copy.jpg")
image3 = cv2.imread("Screenshot (115).png")
# RGB
# OpenCV: BGR

print(image2.shape)

# Change value of a pixel
print(image2[2, 0])
image2[2, 0] = [46, 25, 87]
print(image2[2, 0])


# Crop : array slice

# h, w, c
xmin, ymin, xmax, ymax = 150, 150, 600, 450
sub_image = image2[ymin:ymax, xmin:xmax]
cv2.imshow("img", sub_image)
#  height  width

# Sub chunk dimension = (Same dimensio)

image3[ymin:ymax, 500:950] = sub_image

cv2.imshow("image 3", image3)









#(150, 150, 3)
# h     w    c

#print(image2[:,:,2])
#print(image2[:,:,0])



#data = [[[45, 76, 86], [34, 56, 32]],
#        [[445, 726, 856], [334, 516, 4]]]

#data = np.array(data)
#print(data.shape)

#print(data)

#print(data[:,:, 1])
#cv2.imshow("sjf", image2[:, :, 0])





'''
cv2.imshow("my image", image)
cv2.imshow("second image", image2)
'''
if cv2.waitKey() == 0:
    cv2.destroyAllWindows()