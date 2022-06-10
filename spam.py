from timeit import repeat
import pyautogui, time
time.sleep(5) # is the time you will define to open another tab.
f = open("file name", 'r')
for word in f:
    pyautogui.typewrite(word)
    time.sleep(0.3) # This is the waiting time between 2(two) messages.
    pyautogui.press("enter")
