# Code written by Lap Doan for Psych 196B
#
# Derived from iViewXAPI.py
#
# Demonstrates features of iView X API 
# Defines structures 
# Loads in iViewXAPI.dll
# This script shows how to set up an experiment with Python 2.7.1 (with ctypes Library) 
#
# Author: SMI GmbH
# Feb. 16, 2011

from ctypes import *
import time
import directkeys

import tkinter as tk

#===========================
#        Constants
#===========================

CONST_SAMPLING_RATE_HZ = 30.0
CONST_TIME_AWAY_SECONDS = 0.5

CONST_LEFT_BORDER = 0.0
CONST_RIGHT_BORDER = 0.171
CONST_TOP_BORDER = 0.348
CONST_BOTTOM_BORDER = 0.652

CONST_BUTTON_CODE = 0x01 #esc
CONST_BUTTON_PRESS_TIME_SECONDS = 0.1

CONST_DEBUG = False

#===========================
#        Derived Constants
#===========================

CONST_FRAMES_AWAY_THRESHOLD = CONST_SAMPLING_RATE_HZ * CONST_TIME_AWAY_SECONDS


#===========================
#        Struct Definition
#===========================

class CSystem(Structure):
    _fields_ = [("samplerate", c_int),
    ("iV_MajorVersion", c_int),
    ("iV_MinorVersion", c_int),
    ("iV_Buildnumber", c_int),
    ("API_MajorVersion", c_int),
    ("API_MinorVersion", c_int),
    ("API_Buildnumber", c_int),
    ("iV_ETDevice", c_int)]

class CCalibration(Structure):
    _fields_ = [("method", c_int),
    ("visualization", c_int),
    ("displayDevice", c_int),
    ("speed", c_int),
    ("autoAccept", c_int),
    ("foregroundBrightness", c_int),
    ("backgroundBrightness", c_int),
    ("targetShape", c_int),
    ("targetSize", c_int),
    ("targetFilename", c_char * 256)]

class CEye(Structure):
    _fields_ = [("gazeX", c_double),
    ("gazeY", c_double),
    ("diam", c_double),
    ("eyePositionX", c_double),
    ("eyePositionY", c_double),
    ("eyePositionZ", c_double)]

class CSample(Structure):
    _fields_ = [("timestamp", c_longlong),
    ("leftEye", CEye),
    ("rightEye", CEye),
    ("planeNumber", c_int)]

class CEvent(Structure):
    _fields_ = [("eventType", c_char),
    ("eye", c_char),
    ("startTime", c_longlong),
    ("endTime", c_longlong),
    ("duration", c_longlong),
    ("positionX", c_double),
    ("positionY", c_double)]

class CAccuracy(Structure):
    _fields_ = [("deviationLX",c_double),
                ("deviationLY",c_double),                
                ("deviationRX",c_double),
                ("deviationRY",c_double)]
                
#===========================
#        Loading iViewX.dll 
#===========================

iViewXAPI = windll.LoadLibrary("./iViewXAPI.dll")

#===========================
#        Get screen res
#===========================

root = tk.Tk()

width_px = root.winfo_screenwidth()
height_px = root.winfo_screenheight()

#===========================
#        Initializing Structs
#===========================

systemData = CSystem(0, 0, 0, 0, 0, 0, 0, 0)
calibrationData = CCalibration(5, 1, 0, 0, 1, 20, 239, 1, 15, b"")
leftEye = CEye(0,0,0)
rightEye = CEye(0,0,0)
sampleData = CSample(0,leftEye,rightEye,0)
eventData = CEvent(b'F', b'L', 0, 0, 0, 0, 0)
accuracyData = CAccuracy(0,0,0,0)

ViewXAPI = windll.LoadLibrary("iViewXAPI.dll")
iViewXAPI.iV_ConnectLocal()

# Print Eye location loop
last = time.time()

current_gaze_x = 0.0
current_gaze_y = 0.0
frames_to_transition = 0 # when this hits the threshold, pause/unpause the game
game_paused = False

while True:
    # record every 1 / CONST_SAMPLING_RATE_HZ seconds
    next = last + 1.0 / CONST_SAMPLING_RATE_HZ
    if next > time.time():
        time.sleep(next - time.time())
    last = next
    iViewXAPI.iV_GetSample(byref(sampleData))

    out_of_range = False # out of range in current frame

    # Check the average gaze of left and right eye.
    # If either eye's gaze is 0.0 (outside of screen), treat this as out of range.
    # Otherwise, update current_gaze_x and current_gaze_y.
    if sampleData.leftEye.gazeX == 0.0 or sampleData.rightEye.gazeX == 0.0:
        out_of_range = True
    else:
        current_gaze_x = (sampleData.leftEye.gazeX + sampleData.rightEye.gazeX) / 2.0

    if sampleData.leftEye.gazeY == 0.0 or sampleData.rightEye.gazeY == 0.0:
        out_of_range = True
    else:
        current_gaze_y = (sampleData.leftEye.gazeY + sampleData.rightEye.gazeY) / 2.0

    # regular_x and regular_y range from 0.0 to 1.0.
    regular_x = current_gaze_x / width_px
    regular_y = current_gaze_y / height_px

    if regular_x < CONST_LEFT_BORDER or regular_x > CONST_RIGHT_BORDER or regular_y < CONST_TOP_BORDER or regular_y > CONST_BOTTOM_BORDER:
        out_of_range = True

    # At this point, out_of_range should be accurate for the frame.
    # Update frames_to_transition accordingly.

    if game_paused != out_of_range:
        frames_to_transition += 1

    # If frames_to_transition passes the threshold, toggle game_paused and send a keypress.

    if frames_to_transition >= CONST_FRAMES_AWAY_THRESHOLD:
        frames_to_transition = 0
        game_paused = not game_paused
        directkeys.PressKey(CONST_BUTTON_CODE)
        time.sleep(CONST_BUTTON_PRESS_TIME_SECONDS)
        directkeys.ReleaseKey(CONST_BUTTON_CODE)
        time.sleep(CONST_BUTTON_PRESS_TIME_SECONDS)

    # DEBUG
    if CONST_DEBUG:
        print(str(current_gaze_x) + "," + str(current_gaze_y) + "," + str(game_paused))

iViewXAPI.iV_Disconnect() 