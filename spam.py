from timeit import repeat
import pyautogui, time
time.sleep(this is the time you will define to open another tab.)
f = open("zort", 'r')
for word in f:
    pyautogui.typewrite(word)
    time.sleep(time between each messages)
    pyautogui.press("enter")