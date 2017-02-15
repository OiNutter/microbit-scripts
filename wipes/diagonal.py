# Add your Python code here. E.g.
from microbit import *

MAX_ROWS=4
reverse = False

def scan(level,pause=500):
    global reverse
    i = 0
    while i < 10:
        x = 0
        rows = i
        cols = i

        if button_a.is_pressed():
            reverse = False if reverse else True

        while x <= i:

            for y in range(0,rows+1):
                if x <= MAX_ROWS and y <= MAX_ROWS:
                    x_coord = MAX_ROWS - x if reverse else x
                    y_coord = MAX_ROWS - y if reverse else y

                    display.set_pixel(x_coord,y_coord,level)
            x = x+1
            rows = rows-1

        i+=1
        sleep(pause)

while True:

    scan(9,150)
    scan(0,150)
