# eyeMouse

This Python script uses the Mediapipe library to track your eye movement and control the mouse cursor accordingly. It utilizes your left eye's position to move the cursor and allows for clicking with a blink.

## Instructions

### Install the required libraries:

`pip install opencv-python mediapipe pyautogui`

### Run the script using a Python interpreter:

`python eyeMouse.py`

### Tweaking Left Eye Size:

- Open the eye_controlled_mouse.py file.
- Look for the le variable representing the landmarks of the left eye: le = [lm[145], lm[159]].
- You can adjust the landmarks indices [145, 159] to fine-tune the area considered as your left eye for cursor control.

### Closing the Program:

While the script is running and the OpenCV window is active, you can press the 'q' key or the 'Esc' key to terminate the program and close the OpenCV window.

Enjoy controlling the mouse with your eye movements!
