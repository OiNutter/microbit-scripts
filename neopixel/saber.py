# Add your Python code here. E.g.
from microbit import *
import neopixel
import random

np = neopixel.NeoPixel(pin1, 60)

ROWS = 60
COLS = 1
GAP = 50
pos = 0
color = 85
color_index = 0

def get_next_color():
    foo = [50,50,50]
    foo[color_index] = color
    return tuple(foo)

def get_rand_color():
    return (
        random.randint(0, 255),
        random.randint(0, 255),
        random.randint(0, 255)
        )
        

while color_index < 3:
    while color <= 255:
        pos = 0
        for row in range(0, ROWS):
            for col in range(0, COLS):
                np[pos] = get_next_color()
                np.show()
                pos += 1
                
            sleep(GAP)
        color += 85
    color_index += 1
    color = 85
