Certainly! Here's the updated markdown code with the code explanation part included:


# ROBOgames Project

## Overview
This project was developed as part of the ROBOgames competition organized by the Computer Science Engineering Department of the University of Moratuwa in collaboration with SLT Mobitel. The competition consisted of three stages: 

1. **Elimination Stage**: Participants designed a robot using the Webots simulator to pick red and blue balls and place them in a basket in a specific pattern.
2. **Final Competition**: Participants used a Kobuki robot equipped with an Xbox Kinect camera to identify red and blue balls and push them into corresponding holes. This stage involved the first approach to machine vision for many participants.

## Key Features
- **Ball Detection**: Using computer vision techniques to identify and distinguish between red and blue balls.
- **Blob Detection**: Implementing blob detection to locate the balls in the frame.
- **Kobuki Robot Control**: Interfacing with the Kobuki robot to maneuver and interact with the environment.
- **Kinect Camera Integration**: Utilizing the Kinect camera for depth and RGB data acquisition.
- **Automated Ball Handling**: Programming the robot to pick up balls and place them in specific locations based on their color.

## Code Location
The code for the project is located in the following directory: 
```
/Final codes/TO upload/final_code.py
```

## Dependencies
- Python 3.x
- OpenCV
- NumPy
- Freenect
- KobukiDriver

## How it Works
The code consists of several functions for various tasks:

1. **Depth and RGB Acquisition**:
   - The `get_depth_and_rgb()` function retrieves depth and RGB frames from the Kinect camera.
   
2. **Blob Detection**:
   - The `blob_detect()` function detects blobs (balls) in the image within the specified HSV range.

3. **Drawing and Visualization**:
   - Functions like `draw_keypoints()`, `draw_window()`, and `draw_frame()` are used for drawing keypoints, search windows, and frames, respectively.

4. **Robot Control**:
   - Functions such as `push()`, `grab_ball()`, `carry_ball()`, and `search()` control the Kobuki robot's movements to manipulate the balls.

## Code Explanation
The code is well-commented and organized. Here's a brief explanation of key functions:
- **`get_depth_and_rgb()`**: Retrieves depth and RGB frames.
- **`blob_detect()`**: Detects blobs (balls) in the image using HSV thresholding and blob detection.
- **Drawing Functions**: `draw_keypoints()`, `draw_window()`, and `draw_frame()` are used for visualization.
- **Robot Control Functions**: `push()`, `grab_ball()`, `carry_ball()`, and `search()` control the Kobuki robot's movements.

## Contributing
Feel free to fork this repository and contribute by submitting a pull request. For major changes, please open an issue first to discuss what you would like to change.
