import cv2
import numpy as np

#image3 = cv2.imread("Screenshot (115).png", cv2.IMREAD_GRAYSCALE)

image3 = cv2.imread("Screenshot (115).png")

# Resize images
#image3 = cv2.resize(image3, (600, 400))


#image3 = cv2.cvtColor(image3, cv2.COLOR_BGR2GRAY)



# cv2 draw
# rectangle, circle, line, text


# Draw a line
cv2.line(image3, (300, 200), (400, 500), (255, 255, 0), 5)
cv2.arrowedLine(image3, (350, 250), (450, 550), (255, 255, 0), 5)

# Rectangle
cv2.rectangle(image3, (500,100), (800, 300), (255, 0, 0), -1)


# Circle
cv2.circle(image3, (700, 600), 100, (255, 255, 0), -1)


points = np.array([(20, 30), (50, 100), (200, 500), (800, 900)])

points = points.reshape((-1, 1, 2))

cv2.polylines(image3, [points], True, (255, 0, 0), 3)





# Write on images
cv2.putText(image3, "Hello World", (400, 400), cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 0, 0), 4)






cv2.imshow("img", image3)



cv2.imwrite("output.png", image3)


if cv2.waitKey() == 0:
    cv2.destroyAllWindows()