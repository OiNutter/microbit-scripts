# Add your Python code here. E.g.
from microbit import *
import neopixel
import random

np = neopixel.NeoPixel(pin1, 60)

ROWS = 60
COLS = 1
pos = 0
color = 50

def get_rand_color():
    return (
        random.randint(0, 255),
        random.randint(0, 255),
        random.randint(0, 255)
        )
        

while color <= 255:
    pos = 0
    for row in range(0, ROWS):
        for col in range(0, COLS):
            np[pos] = (0, color, 0)
            np.show()
            pos += 1
            
        sleep(50)
    color += 50
