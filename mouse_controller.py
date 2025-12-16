import pyautogui
from config import SMOOTHING, SCROLL_SPEED

pyautogui.FAILSAFE = False
screen_w, screen_h = pyautogui.size()

prev_x, prev_y = 0, 0

def move_mouse(x, y, cam_w, cam_h):
    global prev_x, prev_y

    screen_x = screen_w / cam_w * x
    screen_y = screen_h / cam_h * y

    curr_x = prev_x + (screen_x - prev_x) / SMOOTHING
    curr_y = prev_y + (screen_y - prev_y) / SMOOTHING

    pyautogui.moveTo(curr_x, curr_y)
    prev_x, prev_y = curr_x, curr_y

def left_click():
    pyautogui.click()

def right_click():
    pyautogui.rightClick()

def scroll(up=True):
    pyautogui.scroll(SCROLL_SPEED if up else -SCROLL_SPEED)
