import numpy as np
import cv2
import os



for image_name in os.listdir("images"):
    image = cv2.imread(f"images/{image_name}", cv2.IMREAD_GRAYSCALE)
    ret, image = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)


    # Erode
    kernel = np.ones((11,11), np.uint8)
    image_erode = cv2.erode(image, kernel)


    # Dilation
    kernel = np.ones((9, 9), np.uint8)
    image_dilate = cv2.dilate(image, kernel)

    cv2.imwrite(f"output/{image_name}.jpg", image)
    cv2.imwrite(f"output/erode_{image_name}.jpg", image_erode)
    cv2.imwrite(f"output/dilate_{image_name}.jpg", image_dilate)


    cv2.imshow("image", image)
    cv2.imshow("image_erode", image_erode)
    cv2.imshow("image_dilate", image_dilate)
    cv2.waitKey(0)
cv2.destroyAllWindows()
