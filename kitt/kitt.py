# Add your Python code here. E.g.
from microbit import *

MAX_ROWS=4

def scan(level,pause=500, reverse=False):
    for i in range(0,10):
        x = 0
        rows = i
        cols = i
        while x <= i:
            for y in range(0,rows+1):
                if x <= MAX_ROWS and y <= MAX_ROWS:
                    coord_x = MAX_ROWS-x if reverse else x
                    coord_y = MAX_ROWS-y if reverse else y
                    display.set_pixel(coord_x,coord_y,max(0,level-((rows-y)*2)))
            x = x+1
            rows = rows-1


        sleep(pause)

display.scroll("I am the Knight Industries 2000")

while True:

    scan(9,150)
    scan(150,True)
