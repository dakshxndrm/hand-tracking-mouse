import cv2
from hand_tracker import HandTracker
from mouse_controller import move_mouse, left_click, right_click
from gestures import left_click as lc, right_click as rc

# Camera
cap = cv2.VideoCapture(0)
tracker = HandTracker()

while True:
    success, frame = cap.read()
    if not success:
        break

    frame = cv2.flip(frame, 1)
    h, w, _ = frame.shape

    result = tracker.process(frame)

    if result.multi_hand_landmarks:
        for hand in result.multi_hand_landmarks:
            tracker.draw(frame, hand)

            lm = hand.landmark

            index = (lm[8].x * w, lm[8].y * h)
            thumb = (lm[4].x * w, lm[4].y * h)
            middle = (lm[12].x * w, lm[12].y * h)

            # Always move mouse
            move_mouse(index[0], index[1], w, h)

            # ---- CLICK LOGIC ----
            if lc(index, thumb):
                left_click()

            elif rc(index, middle):
                right_click()

    cv2.imshow("Hand Tracking Mouse Controller", frame)

    # ESC to exit
    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
