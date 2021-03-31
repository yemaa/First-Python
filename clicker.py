from pynput.mouse import Button, Controller
import time
mouse = Controller()
time.sleep(1)
for j in range(10000):
    mouse.press(Button.left)
