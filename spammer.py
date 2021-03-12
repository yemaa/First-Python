import pyautogui, time

time.sleep(5)
f = open("spam.txt")

for word in f:
    pyautogui.typewrite(word)
