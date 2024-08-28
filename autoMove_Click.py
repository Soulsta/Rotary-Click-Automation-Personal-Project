import time
import math
import ctypes

stop_flag = False

def is_s_key_pressed():
    global stop_flag
    if ctypes.windll.user32.GetAsyncKeyState(ord('s')):
        stop_flag = True

        

screen_width = ctypes.windll.user32.GetSystemMetrics(0)
screen_height = ctypes.windll.user32.GetSystemMetrics(1)
center_x = screen_width // 2
center_y = screen_height // 2
radius = 100  # Specify the circle radius

while not stop_flag:
    for angle in range(0, 360, 10):
        x = int(center_x + radius * math.cos(math.radians(angle)))
        y = int(center_y + radius * math.sin(math.radians(angle)))

        ctypes.windll.user32.SetCursorPos(x, y)
        ctypes.windll.user32.mouse_event(2, 0, 0, 0, 0)  # Left mouse button down
        ctypes.windll.user32.mouse_event(4, 0, 0, 0, 0)  # Left mouse button up
        # Delay after each movement (in seconds)=
        # If you want to perform the click only once, remove this dely
        # Delay to prevent high CPU usage, ran into an error where it crashed
        time.sleep(1)