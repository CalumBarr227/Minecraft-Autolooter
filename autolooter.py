import keyboard
import time
import sys
import win32api, win32con
import pyautogui

def click(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

print("started press b to start")

def loot_single_chest():
    chest_location = pyautogui.locateOnScreen("chest.png", confidence=0.8)
    if chest_location is None:
        print("cant find word on screen")
        return

    h_offset_x = chest_location.width // 3
    offset_left = 8
    offset_up = 3
    start_x = chest_location.left + h_offset_x - offset_left
    start_y = chest_location.top + 47 - offset_up

    rows, cols = 3, 9
    slot_size = 36
    slot_center_offset = 12

    first_x = start_x + slot_center_offset
    first_y = start_y + slot_center_offset
    win32api.SetCursorPos((first_x, first_y))
    time.sleep(0.01)

    win32api.keybd_event(0x10, 0, 0, 0)

    screen_width, screen_height = pyautogui.size()
    slot_number = 1

    for row in range(rows):
        for col in range(cols):
            x = min(start_x + col * slot_size + slot_center_offset, screen_width - 1)
            y = min(start_y + row * slot_size + slot_center_offset, screen_height - 1)

            if row == rows - 1 and col == cols - 1:
                x -= 1
                y -= 1
                click(x, y)
                time.sleep(0.02)
                click(x, y)
            else:
                click(x, y)
                time.sleep(0.006)

            print(f"clicked slot {slot_number} at ({x}, {y})")
            slot_number += 1

    win32api.keybd_event(0x10, 0, win32con.KEYEVENTF_KEYUP, 0)
    print("looted chest")

while True:
    if keyboard.is_pressed("b"):
        loot_single_chest()
        time.sleep(0.1)
    if keyboard.is_pressed("`"):
        print("exiting")
        sys.exit()
