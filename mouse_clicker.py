from pynput.mouse import Button, Controller
import time

my_mouse = Controller()
loc_start = my_mouse.position

for rep in range(7200):
    my_mouse.click(Button.left,1)
    time.sleep(0.5)
    my_mouse.click(Button.left,1)
    time.sleep(0.5)
    if my_mouse.position != loc_start:
        break
    # print 'reloop'
