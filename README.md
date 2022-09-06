# Eye-Tracker-Research

This is Lap Doan's Psych 196B project, working as a research assistant under Maggie Yeh and Professor Zili Liu.

The purpose of this project is to be played in the background of a video game, using an iViewRED camera to track the participant's gaze. If the participant's gaze leaves a specified rectangular area, the program sends a keypress to pause the game; once their gaze returns to the area, the program sends a keypress to unpause the game.

# Contact

Please contact me at lapdoan01@gmail.com if you have any questions about this project.

# Current Issues

As of right now, when tested on hardware in the UCLA Psychology lab, the program stops recording after a while. This is likely due to iViewRED being finicky with its connection. The proposed solution is to attempt to reconnect to the camera using ConnectLocal() if a disconnection is detected (currently eye_track.py is set to print "WARNING: Connection lost with iViewRED" without attempting to reconnect).

The program does not function properly when the game window is not active, such as when Alt-Tab is pressed to switch the current window. The proposed solution is to have the program check the name of the current active window and compare it against CONST_GAME_WINDOW_NAME.

This repository includes a canary build eye_track_canary.py which attempts to implement both of these solutions. They have not been tested on UCLA Psychology lab hardware.

# How to use

1. Refer to the constants below in order to customize the behavior of the program. To modify these constants, open eye_track.py in a text editor.

2. Set up the iViewRED camera first. Run the calibration and validation sequences as normal.

3. Set up the game such that it is currently paused.

4. Run eye_track.py. It will print, "Will unpause the game and begin tracking gaze in [number] seconds..."

5. Minimize eye_track.py, letting it run in the background of the game. After CONST_SETUP_TIME_SECONDS seconds have passed, the game will unpause, and the study will begin.

# Troubleshooting

If eye_track.py is crashing immediately, make sure that iViewXAPI64.dll, iViewXAPI.dll, and directkeys.py are in the same directory as eye_track.py. Also check if the following libraries are installed: ctypes, time, tkinter

If eye_track.py is printing "WARNING: [number] consecutive failed readings", then it is failing to receive data from the iViewRED camera. Make sure that the camera is properly configured, and that the iViewRED camera is still running. This warning can also occur if the participant looks away from the screen or closes their eyes for an extended period of time.

# Customizable Constants:

The constants in eye_track.py can be changed. Below is a list of their uses:

CONST_SAMPLING_RATE_HZ: the sampling rate of the eye-tracking camera, in Hz.

CONST_TIME_AWAY_SECONDS: the amount of time a participant can look away from the intended area before pausing, in seconds.

CONST_LEFT_BORDER: A number from 0.0 to 1.0*, indicating the left border of the rectangle the participant is supposed to look at. This should be LESS than CONST_RIGHT_BORDER.

CONST_RIGHT_BORDER: A number from 0.0 to 1.0*, indicating the right border of the rectangle the participant is supposed to look at. This should be GREATER than CONST_LEFT_BORDER.

CONST_TOP_BORDER: A number from 0.0 to 1.0*, indicating the top border of the rectangle the participant is supposed to look at. This should be LESS than CONST_BOTTOM_BORDER.

CONST_BOTTOM_BORDER: A number from 0.0 to 1.0*, indicating the bottom border of the rectangle the participant is supposed to look at. This should be LESS than CONST_TOP_BORDER.

CONST_BUTTON_CODE: The button code of the key to be pressed. At the time of release, this is set to the 'Esc' key. Refer to: https://web.archive.org/web/20190801085838/http://www.gamespp.com/directx/directInputKeyboardScanCodes.html

CONST_BUTTON_PRESS_TIME_SECONDS: The amount of time, in seconds, that the button is pushed down before being released.

CONST_SETUP_TIME_SECONDS: The amount of time that the program will wait before tracking eye movement.

CONST_IS_64_BIT: True if the computer the program is running on is 64-bit; False if 32-bit. This determines whether iViewXAPI64.dll or iViewXAPI.dll is loaded.

CONST_GAME_WINDOW_NAME (canary build only): The name of the window that should be active when the program is running. Currently, this is set to "Medal of Honor: Warfighter"; however, testing needs to be conducted to determine if the active window is actually named this when playing the game.

CONST_DEBUG: If set to True, the program will print live information on the participant's gaze and whether the game is paused or not. In the canary build, it will also print out the name of the current active window.

*Regarding border constants, if the boundary is on the screen's border (0.0 or 1.0), it may be better to set the boundary to be slightly less than 0.0 or greater than 1.0 (ie -0.1 or 1.1).

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

Tested the program on both my laptop and PC, playing Pokemon Reborn, Minecraft, and BGB Emulator. I noticed a few concerns:

1. If the 'Esc' button is used for other tasks in game, such as closing out of menus in Minecraft, then the pause/unpause behavior desyncs from the participant's gaze.

2. If the game does not register an 'Esc' press to pause/unpause (present in Pokemon Reborn when the player is walking sometimes), then a similar desync can occur.

3. Running iViewRED concurrently with certain games appears to be impossible, regardless of whether this program is also being run.

The program runs flawlessly on my laptop using the BGB emulator. My PC cannot run iViewRED consistently. Pokemon Reborn on my laptop occasionally does not register 'Esc' presses, but this issue occurs with manually pressed 'Esc' button presses as well, so this is not the fault of the program. Minecraft on my laptop tends to crash iViewRED, likely due to taking up a lot of resources.

7/20

Cleaned up the README and added a conditional for easy loading of the dll file.

7/22

Went on campus and tested the program. I ran into a few issues, but was able to solve them:

I noticed that the Python file was unable to be run as an executable, but could be run from the command line. Investigating further, I realized that Python was not on the computer's PATH variable list, so I added it to there. Furthermore, I had to remove VSCode from the PATH variable list.

I was initially unable to have my program read values from the iViewRED program due to the program being unable to establish a connection with the iViewRED's IP and socket. I attempted to change the iv_ConnectLocal() call to an iv_Connect() call with the IP's and sockets, but was unable to get it to work. Eventually, I just reinstalled iViewRED onto the computer, updating the API from version 4.2.0 to version 4.4.0.

When testing the program with Medal of Honor: Warfighter, the program worked in most cases. However, a problem arose when the player was required to hold down the 'Alt' or 'Ctrl' keys. If one of these keys were held down, and then the 'Esc' key triggered from the player's gaze leaving the required area, a Windows shortcut would be triggered, exiting out of the game and desyncing the pause functionality. This was solved by changing the keybinds for 'Alt' and 'Ctrl' to C and X, respectively.

I believe I have completed this project to the best of my ability. Nevertheless, a few concerns arise:

It is possible for the player to inadvertently desync their gaze from the pause menu if they are clicking to shoot, the pause menu triggers because their gaze left the area, and the player accidentally clicks one of the pause menu options. This did not come up in testing, but I believe this is still possible.

The current parameters of a 5x5 cm square and the pause menu triggering after 0.5 seconds of looking away are extremely punishing. Perhaps this is also due to the fact that I am very bad at the game in question.

# Resources Used

REDn Scientific System User Guide:
http://www.humre.vu.lt/files/doc/Instrukcijos/SMI/REDnScientific.pdf

iView X SDK manual:
https://tsgdoc.socsci.ru.nl/images/c/cb/IView_X_SDK_Manual.pdf

For basic iView API code:
https://github.com/esdalmaijer/PyGaze/blob/master/pygaze/_eyetracker/iViewXAPI.py

ScanCodes for keyboard inputs:
https://stackoverflow.com/questions/14489013/simulate-python-keypresses-for-controlling-a-game

Getting screen monitor resolution:
https://stackoverflow.com/questions/3129322/how-do-i-get-monitor-resolution-in-python

Keyboard scan codes:
https://web.archive.org/web/20190801085838/http://www.gamespp.com/directx/directInputKeyboardScanCodes.html

Getting name of active window:
https://stackoverflow.com/questions/65362756/getting-process-name-of-focused-window-with-python