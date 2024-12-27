import cv2 as cv
import numpy as np
import mediapipe as mp
import uuid

# Initialize drawing utilities and hand tracking solutions
mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands

cap = cv.VideoCapture(0)  # Open the webcam

# Property of drawing landmarks and connections
landmark_drawing_spec = mp_drawing.DrawingSpec(color=(255, 0, 255), thickness=5, circle_radius=2)  # for dots
connection_drawing_spec = mp_drawing.DrawingSpec(color=(255, 182, 193), thickness=2)  # for connection lines

with mp_hands.Hands(min_detection_confidence=0.8, min_tracking_confidence=0.5) as hands:  # Initialize hand tracking
    while cap.isOpened():  # Run the webcam feed
        ret, frame = cap.read()  # Read each frame
        if not ret:
            break

        # Convert BGR image to RGB for processing
        image = cv.cvtColor(frame, cv.COLOR_BGR2RGB)

        # Set the flag to False to disable writeable mode (needed for Mediapipe processing)
        image.flags.writeable = False

        # Process the image and detect hand landmarks
        result = hands.process(image)
        if result.multi_hand_landmarks:  # If hands are detected
            for hand_landmarks in result.multi_hand_landmarks:
                for landmark in hand_landmarks.landmark:
                    print(landmark)  # Print landmark coordinates

                # Draw landmarks and connections on the frame
                mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS,
                                          landmark_drawing_spec=landmark_drawing_spec,
                                          connection_drawing_spec=connection_drawing_spec)

        # Set flag to True to enable writeable mode after processing
        image.flags.writeable = True

        # Convert the image back to BGR for display
        image = cv.cvtColor(image, cv.COLOR_RGB2BGR)

        # Display the processed frame
        cv.imshow("Hand Tracking", frame)

        # Break the loop if 'q' key is pressed
        if cv.waitKey(10) & 0xFF == ord('q'):
            break

    cap.release()  # Release the webcam
    cv.destroyAllWindows()  # Close the window
