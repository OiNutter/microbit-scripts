from microbit import *

display.scroll("I am the Knight Industries 2000")

MAX_ROWS = 4
MAX_BRIGHTNESS = 9
MIN_BRIGHTNESS = 2

def scan(reverse=False):

    for i in range(0, 9):
        brightness = MAX_BRIGHTNESS

        row_range = range(0, i+1) if not reverse else range(i, -1, -1)

        counter = 0
        for j in row_range:
            x = i - j if not reverse else MAX_ROWS - j
            light_level = max(MIN_BRIGHTNESS, brightness) if counter >= 2 else MAX_BRIGHTNESS - counter
            print (x, light_level)
            if x <= MAX_ROWS and x >= 0:
                display.set_pixel(x, 2, light_level)
                counter += 1

            #if i >= 2:
            brightness -= 1

        print("-")
        if i < 8:
            sleep(100)

for x in range(0, MAX_ROWS+1):
    display.set_pixel(x, 2, MIN_BRIGHTNESS)

while True:

    scan()
    scan(reverse=True)
