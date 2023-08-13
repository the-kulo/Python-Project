import cv2

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if ret:
        frame = cv2.resize(frame, (0, 0), fx=1.0, fy=1.0)
        canny = cv2.Canny(frame, 100, 200)
        cv2.imshow('video', canny)
    else:
        break
    if cv2.waitKey(10) == ord('q'):
        break
        