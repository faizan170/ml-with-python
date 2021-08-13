import cv2

face_cascade = cv2.CascadeClassifier("haarcascades/haarcascade_frontalface_default.xml")
haarcascade_eye = cv2.CascadeClassifier("haarcascade/haarcascade_eye.xml")

image = cv2.imread("images/group2.jpg")

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(gray)
print(faces)
for (x,y,w,h) in faces:
    cv2.rectangle(image, (x, y), (x + w, y + h), (127, 0, 255), 2)

    sub_image = image[y:y+h, x:x+w]
    eyes = haarcascade_eye.detectMultiScale(sub_image)

    for (x, y, w, h) in eyes:
        cv2.rectangle(sub_image, (x, y), (x + w, y + h), (0, 0, 255), 2)

cv2.imshow("image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
