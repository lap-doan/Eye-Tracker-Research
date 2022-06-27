import cv2
from gaze_tracking import GazeTracking
from pynput import mouse, keyboard
from pynput.keyboard import Key, Controller 

gaze = GazeTracking()
webcam = cv2.VideoCapture(0)

while True:
    _, frame = webcam.read()
    gaze.refresh(frame)

    new_frame = gaze.annotated_frame()
    text = ""

    hRatio = gaze.horizontal_ratio();
    vRatio = gaze.vertical_ratio();
    kb = Controller();

    if gaze.is_right():
        text = "Looking right"
    elif gaze.is_left():
        text = "Looking left"
    elif gaze.is_center():
        text = "Looking center"
    
    if hRatio == 1.0 or hRatio == 0:
        print("Gone past horizontal borders");
        kb.tap(Key.esc); #press esc button
    elif vRatio == 1 or vRatio == 0:
        print("Gone past vertical borders");
        kb.tap(Key.esc); #press esc button

    cv2.putText(new_frame, text, (60, 60), cv2.FONT_HERSHEY_DUPLEX, 2, (255, 0, 0), 2)
    cv2.imshow("Demo", new_frame)

    if cv2.waitKey(1) == 27:
        break
