import dlib
import cv2

detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

cap = cv2.VideoCapture(0)  # zero for the first web cam
while True:
    _, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = detector(gray)
    for face in faces:
        x1 = face.left()
        y1 = face.top()
        x2 = face.right()
        y2 = face.bottom()
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 3)
        landmarks = predictor(gray, face)
        for n in range(0, 68):
            x = landmarks.part(n).x
            y = landmarks.part(n).y
            print(x, y)
            cv2.circle(frame, (x, y), 3, (0, 255, 0), -1)

    cv2.imshow("my face", frame)
    key = cv2.waitKey(1)
    if key == 27:  # ESC key
        break  # Proper indentation here

cap.release()
cv2.destroyAllWindows()