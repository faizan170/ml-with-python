import cv2

cap = cv2.VideoCapture("first.mp4")

fourcc = cv2.VideoWriter_fourcc(*"X264")
fps = cap.get(cv2.CAP_PROP_FPS)

hw = (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)),
      int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))


print(fps, hw, fourcc)

fourcc = cv2.VideoWriter_fourcc(*'X264')
writer = cv2.VideoWriter('output.mp4',fourcc, fps, hw)

counter = 0
while True:

    ret, frame = cap.read()
    if ret == False:
        break
    frame2 = cv2.rectangle(frame.copy(), (50, 50), (300, 300), (255, 55, 0), 2)

    writer.write(frame2)

cap.release()
writer.release()
cv2.destroyAllWindows()
