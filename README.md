# Eye-Tracker-Research
This is Lap Doan's Psych 196B project, working as a research assistant under Maggie Yeh and Professor Zili Liu.

# How to use

Run the calibration process on iViewRED first. Then run eye_track.py.
If eye_track.py does not run, make sure that directkeys.py and the appropriate iViewXAPI.dll file are in the same directory.
When eye_track.py is run, it will display a message stating "Tracking gaze in [number] seconds..."

# Customizable Constants:

The constants in eye_track.py can be changed. Below is a list of their uses:

CONST_SAMPLING_RATE_HZ: the sampling rate of the eye-tracking camera, in Hz.
CONST_TIME_AWAY_SECONDS: the amount of time a participant can look away from the intended area before pausing, in seconds.

CONST_LEFT_BORDER: A number from 0.0 to 1.0, indicating the left border of the rectangle the participant is supposed to look at. This should be LESS than CONST_RIGHT_BORDER.
CONST_RIGHT_BORDER: A number from 0.0 to 1.0, indicating the right border of the rectangle the participant is supposed to look at. This should be GREATER than CONST_LEFT_BORDER.
CONST_TOP_BORDER: A number from 0.0 to 1.0, indicating the top border of the rectangle the participant is supposed to look at. This should be LESS than CONST_BOTTOM_BORDER.
CONST_BOTTOM_BORDER: A number from 0.0 to 1.0, indicating the bottom border of the rectangle the participant is supposed to look at. This should be LESS than CONST_TOP_BORDER.

CONST_BUTTON_CODE: The button code of the key to be pressed. Refer to: https://web.archive.org/web/20190801085838/http://www.gamespp.com/directx/directInputKeyboardScanCodes.html
CONST_BUTTON_PRESS_TIME_SECONDS: The amount of time, in seconds, that the button is pushed down before being released.

CONST_SETUP_TIME_SECONDS: The amount of time that the program will wait before tracking eye movement.

CONST_DEBUG: If set to True, the program will print live information on the participant's gaze and whether the game is paused or not.


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

7/17
Tested the program 

# Resources Used
For basic iView API code:
https://github.com/esdalmaijer/PyGaze/blob/master/pygaze/_eyetracker/iViewXAPI.py

ScanCodes for keyboard inputs:
https://stackoverflow.com/questions/14489013/simulate-python-keypresses-for-controlling-a-game

Getting screen monitor resolution:
https://stackoverflow.com/questions/3129322/how-do-i-get-monitor-resolution-in-python

Keyboard scan codes:
https://web.archive.org/web/20190801085838/http://www.gamespp.com/directx/directInputKeyboardScanCodes.html