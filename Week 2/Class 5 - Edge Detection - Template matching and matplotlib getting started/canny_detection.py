import cv2

image = cv2.imread("images/base.png")


edges = cv2.Canny(image,200,200)


cv2.imshow("image", edges)
cv2.waitKey(0)
cv2.destroyAllWindows()