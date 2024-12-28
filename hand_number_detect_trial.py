
import cv2 as cv
import numpy as np
import mediapipe as mp

def FingerOpen(tip, pip, hand_size, thres_hold=0.25):
    return distance(tip, pip) / hand_size > thres_hold

def distance(a, b):
    return np.sqrt((a.x - b.x) ** 2 + (a.y - b.y) ** 2)

mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands

cap = cv.VideoCapture(0)

landmark_drawing_spec = mp_drawing.DrawingSpec(color=(255, 0, 255), thickness=5, circle_radius=2)
connection_drawing_spec = mp_drawing.DrawingSpec(color=(255, 182, 193), thickness=2)

with mp_hands.Hands(min_detection_confidence=0.8, min_tracking_confidence=0.5) as hands:
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        image = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
        image.flags.writeable = False
        result = hands.process(image)

        if result.multi_hand_landmarks:
            for hand_landmarks in result.multi_hand_landmarks:
                hand_size = distance(
                    hand_landmarks.landmark[mp_hands.HandLandmark.WRIST],
                    hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_TIP]
                )

                thumb_open = FingerOpen(
                    hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP],
                    hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_IP], hand_size)
                index_open = FingerOpen(
                    hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP],
                    hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_PIP], hand_size)
                middle_open = FingerOpen(
                    hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_TIP],
                    hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_PIP], hand_size)
                ring_open = FingerOpen(
                    hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_TIP],
                    hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_PIP], hand_size)
                pinky_open = FingerOpen(
                    hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_TIP],
                    hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_PIP], hand_size)

                total = thumb_open + index_open + middle_open + ring_open + pinky_open

                cv.putText(frame, str(total), (245, 120), cv.FONT_HERSHEY_SIMPLEX, 2.0, (0, 0, 0))

                mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS,
                                          landmark_drawing_spec=landmark_drawing_spec,
                                          connection_drawing_spec=connection_drawing_spec)

        image.flags.writeable = True
        cv.imshow("Hand Tracking", frame)

        if cv.waitKey(10) & 0xFF == ord('q'):
            break

cap.release()
cv.destroyAllWindows()
