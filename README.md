# Eye-Tracker-Research
This is Lap Doan's Psych 196B project, working as a research assistant under Maggie Yeh and Professor Zili Liu.

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

7/10
eye_track.py now prints location for the average gaze between left and right eyes. Also introduced some rudimentary pause logic.

7/16
Initially looked into controller.Controller() for keyboard presses, which was from the previous RA's code. This could produce key presses in Notepad, but not Pokemon Reborn.
Created directkeys.py, derived from ScanCodes, in order to do keyboard presses. This produces unfilterable key presses, as opposed to controller.Controller. This works for Pokemon Reborn.
Added logic to pause the game when the gaze is in the desired area.

# Resources Used
For basic iView API code:
https://github.com/esdalmaijer/PyGaze/blob/master/pygaze/_eyetracker/iViewXAPI.py

ScanCodes for keyboard inputs:
https://stackoverflow.com/questions/14489013/simulate-python-keypresses-for-controlling-a-game

Getting screen monitor resolution:
https://stackoverflow.com/questions/3129322/how-do-i-get-monitor-resolution-in-python