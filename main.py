import mediapipe as mp
import cv2


if __name__=="__main__":
    cam = cv2.VideoCapture(0)
    mp_hands = mp.solutions.hands
    hands = mp_hands.Hands()
    while True:
        _,frame = cam.read()
        rgb_frame = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
        results = hands.process(rgb_frame)
        cv2.imshow("frame",frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cam.release()
    cv2.destroyAllWindows()

