AI-GYM Trainer Documentation

Project Name: AI-GYM Trainer

1. Overview

AI-GYM Trainer is a Python-based application that utilizes computer vision and pose estimation to assist users in tracking their exercise progress. The application captures real-time video input from the user's webcam, detects their body pose, and calculates the angle of specific joints during exercise. The program tracks repetitions and displays the count on the screen, allowing users to monitor their performance.

2. Modules and Dependencies

AI-GYM Trainer relies on the following modules and libraries:

- OpenCV (cv2): For video processing and rendering.
- NumPy (np): For numerical operations.
- time: For calculating the frame rate (fps).
- Mediapipe (mp): For pose estimation and landmark detection.
- math: For calculating the angle between joints.

3. Files and Classes

The project is divided into two files:

- AITrainer.py: The main file that captures video input, processes it, and displays the results.
- PoseDetector.py: Contains the `poseDetector` class that detects and processes the user's body pose.

4. AITrainer.py

The AITrainer.py file captures video input from the user's webcam and processes it using the `poseDetector` class from PoseDetector.py. It calculates the angle between specific joints and displays the repetition count on the screen.

Key features:
- Captures video input from the user's webcam
- Initializes the `poseDetector` class
- Processes each frame to detect the user's body pose
- Calculates the angle between joints 11, 13, and 15
- Tracks and displays the repetition count

5. PoseDetector.py

The PoseDetector.py file contains the `poseDetector` class, which detects and processes the user's body pose using the Mediapipe library.

Key features:
- Initializes the Mediapipe pose estimation model
- Finds and processes the user's body pose in a given image
- Locates and returns the coordinates of specific body landmarks
- Calculates the angle between three given landmarks
- Visualizes the results on the input image

6. Usage

To run the AI-GYM Trainer, execute the AITrainer.py file:

```
python AITrainer.py
```

Once the program is running, perform the exercise in front of the webcam. The application will detect the user's body pose, calculate the angle between specific joints, and track the repetitions. The repetition count will be displayed on the screen.

7. Customization

The AI-GYM Trainer can be customized to track different exercises by changing the joint indices in the `findAngle()` function call within the AITrainer.py file. For more information on the available landmarks and their indices, refer to the Mediapipe documentation: https://developers.google.com/mediapipe/solutions/vision/pose_landmarker/

8. License

AI-GYM Trainer is an open-source project. Feel free to use, modify, and distribute the code as needed, following the terms and conditions of the license.
