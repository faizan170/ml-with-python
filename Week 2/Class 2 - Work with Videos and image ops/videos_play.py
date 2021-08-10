# Read Images

# Read Videos
# Webcam
#  Video Stream

import cv2

cap = cv2.VideoCapture("first.mp4")

# FPS
print("FPS:", cap.get(cv2.CAP_PROP_FPS))

# FPS * TOTAL_SECONDS
print("Total No Frame:", int(cap.get(cv2.CAP_PROP_FRAME_COUNT)))

# FRAME_HEIGHT AND FRAME_WIDTH
print("Width:", int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)))
print("Height:", int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))

counter = 0
while True:

    ret, frame = cap.read()
    if ret == False:
        break
    counter += 1
    frame2 = cv2.rectangle(frame.copy(), (50, 50), (300, 300), (255, 55, 0), 2)

    cv2.imwrite(f"frames/frame_{counter}.jpg", frame2)


    cv2.imshow("frame", frame)
    cv2.imshow("frame 2", frame2)

    if cv2.waitKey(25) & 0xFF == ord('r'):
        break


cv2.destroyAllWindows()