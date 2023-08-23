# You handle the cursor with your left eye, wink to click

import cv2
import mediapipe as mp
import pyautogui

cap = cv2.VideoCapture(0)
face_mesh = mp.solutions.face_mesh.FaceMesh(refine_landmarks=True)
screen_width, screen_height = pyautogui.size()

while True:
    ret, frame = cap.read()
    if not ret:
        break
    
    frame = cv2.flip(frame, 1)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    output = face_mesh.process(rgb_frame)
    landmark_points = output.multi_face_landmarks
    frame_height, frame_width, _ = frame.shape
    
    if landmark_points:
        landmarks = landmark_points[0].landmark
        
        for idx, landmark in enumerate(landmarks[474:478]):
            x = int(landmark.x * frame_width)
            y = int(landmark.y * frame_height)
            cv2.circle(frame, (x, y), 3, (0, 255, 0))
            if idx == 1:
                screen_x = int(screen_width * landmark.x)
                screen_y = int(screen_height * landmark.y)
                pyautogui.moveTo(screen_x, screen_y)
        
        left_eye_landmarks = [landmarks[145], landmarks[159]]
        for landmark in left_eye_landmarks:
            x = int(landmark.x * frame_width)
            y = int(landmark.y * frame_height)
            cv2.circle(frame, (x, y), 3, (0, 255, 255))
        if abs(left_eye_landmarks[0].y - left_eye_landmarks[1].y) < 0.006:
            pyautogui.click()
            pyautogui.sleep(1)
    
    cv2.imshow('eyeMouse', frame)
    
    key = cv2.waitKey(1)
    if key == ord('q') or key == 27:
        break

cap.release()
cv2.destroyAllWindows()
