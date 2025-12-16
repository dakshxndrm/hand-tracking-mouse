import math
import time
from config import LEFT_CLICK_DIST, RIGHT_CLICK_DIST, CLICK_COOLDOWN

last_click = 0

scroll_active = False
last_scroll_y = None

def distance(p1, p2):
    return math.hypot(p1[0] - p2[0], p1[1] - p2[1])

def can_click():
    global last_click
    if time.time() - last_click > CLICK_COOLDOWN:
        last_click = time.time()
        return True
    return False

def left_click(index, thumb):
    return distance(index, thumb) < LEFT_CLICK_DIST and can_click()

def right_click(index, middle):
    return distance(index, middle) < RIGHT_CLICK_DIST and can_click()

def scroll_control(index, middle):
    """
    Returns integer scroll value:
    +ve → scroll up
    -ve → scroll down
    0 → no scroll
    """
    global scroll_active, last_scroll_y

    d = distance(index, middle)

    # Enter scroll mode
    if d < 30 and not scroll_active:
        scroll_active = True
        last_scroll_y = index[1]
        return 0

    # Exit scroll mode
    if d > 45 and scroll_active:
        scroll_active = False
        last_scroll_y = None
        return 0

    # Scroll while active
    if scroll_active:
        delta = last_scroll_y - index[1]
        last_scroll_y = index[1]

        # Sensitivity threshold
        if abs(delta) > 5:
            return int(delta)

    return 0
import math
import time
from config import CLICK_COOLDOWN

# Tuned thresholds (very important)
LEFT_CLICK_DIST = 28
RIGHT_CLICK_DIST = 35

last_click_time = 0

def distance(p1, p2):
    return math.hypot(p1[0] - p2[0], p1[1] - p2[1])

def click_allowed():
    global last_click_time
    now = time.time()
    if now - last_click_time > CLICK_COOLDOWN:
        last_click_time = now
        return True
    return False

def left_click(index, thumb):
    """
    Thumb + Index pinch
    """
    if distance(index, thumb) < LEFT_CLICK_DIST and click_allowed():
        return True
    return False

def right_click(index, middle):
    """
    Index + Middle pinch
    """
    if distance(index, middle) < RIGHT_CLICK_DIST and click_allowed():
        return True
    return False
