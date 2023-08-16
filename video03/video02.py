import cv2

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if ret:
        frame = cv2.resize(frame, (0, 0), fx=1.0, fy=1.0)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faceCascade = cv2.CascadeClassifier('face_detect.xml')
        faceRect = faceCascade.detectMultiScale(gray, 1.1, 6)

        for(x, y, w, h)in faceRect:
            cv2.rectangle(frame, (x, y), (x+w, y+h),(0, 255, 0), 2)

        cv2.imshow('video', frame)
    else:
        break
    if cv2.waitKey(10) == ord('q'):
        break
