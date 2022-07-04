# Eye-Tracker-Research
This is Lap Doan's Psych 196B project, working as a research assistant under Maggie Yeh and Professor Zili Liu.

This project builds on Daniel's code.

# How to use

Run the calibration process on iViewRED first. Then run eye_track.py.

# Daily progress
6/26
Downloaded the necessary modules to get GazeTracking.py to work: CMake, dlib, and pynput.

Created a github repository to track changes.

Tested GazeTracking.py, defaults to computer camera instead of eye tracking camera.

Tested simple_tracker_experiment.py. Window generated is too large to fit on the screen, won't get any smaller. The program appears to not work.

7/3
After reading over the User manual and SDK manual, I was able to get eye_track.py to print out data for the X location for the gaze of the left eye at a rate of 30 Hz, which is the rate that the eye tracker works at.

# Resources Used
For basic iView API code:
https://github.com/esdalmaijer/PyGaze/blob/master/pygaze/_eyetracker/iViewXAPI.py
