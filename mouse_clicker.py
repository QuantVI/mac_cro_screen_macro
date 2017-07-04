from pynput.mouse import Button, Controller
import time

my_mouse = Controller()
loc_start = my_mouse.position

'''
for rep in range(7200):
    my_mouse.click(Button.left,1)
    time.sleep(0.1)
    my_mouse.click(Button.left,1)
    time.sleep(0.1)
    if my_mouse.position != loc_start:
        break
'''

# from pynput import keyboard
# 43200 = 12 hours if the sleep times sum to 1 second
# 25200 = 7 hours ' ' ' ' ' ' ' '
for rep in range(43200):
    my_mouse.click(Button.left,1)
    time.sleep(0.15)
    my_mouse.click(Button.left,1)
    time.sleep(0.25)
    my_mouse.click(Button.left,1)
    time.sleep(0.3)
    my_mouse.click(Button.left,1)
    time.sleep(0.2)
    my_mouse.click(Button.left,1)
    time.sleep(0.1)
    my_mouse.click(Button.left,1)
    time.sleep(0.1)
    # index 0 is the left-right horizontal position
    # index 1 is the up-down vertical position
    while (abs(my_mouse.position[0]-loc_start[0]) > 25 or
           abs(my_mouse.position[1]-loc_start[1]) > 10):
        None
