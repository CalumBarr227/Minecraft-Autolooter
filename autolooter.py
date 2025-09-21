import pyautogui
import keyboard
import time
import sys

print("started press b to start")

def loot_single_chest():
    chest_location = pyautogui.locateOnScreen("chest.png", confidence=0.8)
    if chest_location is None:
        print("cant find word on screen")
        return
    
    start_x = chest_location.left + 36
    start_y = chest_location.top + chest_location.height + 10

    rows, cols = 3, 9
    slot_size = 36

    pyautogui.keyDown("shift")
    for row in range(rows):
        for col in range(cols):
            x = start_x + col * slot_size
            y = start_y + row * slot_size
            pyautogui.click(x, y)
            time.sleep(0.05)
    pyautogui.keyUp("shift")

while True:
    if keyboard.is_pressed("b"):
        loot_single_chest()
        time.sleep(1)
    if keyboard.is_pressed("`"):
        print("exiting")
        sys.exit()
