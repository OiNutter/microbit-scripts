# Import required modules
from microbit import *

MAX_ROWS = 4
MAX_BRIGHTNESS = 9

while True:

    i = 0
    while i < 18:
        brightness = 9
        rows = i
        for x in range(0, 10):
            for y in range(0, rows):
                if x >= 0 and x <= MAX_ROWS and y >= 0 and y <= MAX_ROWS:
                    brightness = max(0, MAX_BRIGHTNESS-((rows-y)*2))
                    display.set_pixel(x, MAX_ROWS - y, brightness)

            rows -= 1

        i += 1
        sleep(150)
