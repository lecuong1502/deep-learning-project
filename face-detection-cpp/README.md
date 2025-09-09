- I use the OpenCV library to detect faces in a live stream from webcam or in a video file stored in the local machine. This program detects faces in real time and tracks it. It uses pre-trained XML classifiers for the same.
- Requirements for running the program:
    + OpenCV must be installed on the local machine.
    + Paths to the classifier XML files must be given before the execution of the program.
    + Use 0 in capture.open(0) to play webcam feed.
    + For detection in a local video provide the path to the video.(capture.open(“path_to_video”))