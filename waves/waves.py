# Import required modules
from microbit import *

MAX_ROWS = 4
MAX_BRIGHTNESS = 9
plane="horiz"
reverse=False
iterations = 10

while True:
    i = 0
    while i < iterations:
        brightness = MAX_BRIGHTNESS
        rows = i
        display.clear()

        x_tilt = accelerometer.get_x()
        y_tilt = accelerometer.get_y()

        directions = {"x": "flat", "y": "flat"}

        old_plane = plane
        old_reverse = reverse

        if x_tilt > 100:
            directions['x'] = "left"
        elif x_tilt < -100:
            directions['x'] = "right"

        if y_tilt > 100:
            directions['y'] = "down"
        elif y_tilt < -100:
            directions['y'] = "up"

        if directions['y'] == "flat":
            iterations = 10
            if directions['x'] == "left":
                plane = "horiz"
                reverse = False
            elif directions['x'] == "right":
                plane = "horiz"
                reverse = True
        elif directions['x'] == "flat":
            iterations = 10
            if directions['y'] == "down":
                plane = "vert"
                reverse = False
            elif directions['y'] == "up":
                plane = "vert"
                reverse = True
        else:
            iterations = 18
            if directions['x'] == "left":
                plane = "diagleft"
            elif directions['x'] == "right":
                plane = "diagright"

            if directions['y'] == "down":
                reverse = False
            elif directions['y'] == "up":
                reverse = True

        if plane != old_plane or reverse != old_reverse:
            i = 0

        if plane == "horiz" or plane == "vert":
            row_range = range(0, i+1) if not reverse else range(i, -1, -1)
        elif plane == "diagleft":
            row_range = range(0, 10)
        elif plane == "diagright":
            row_range = range(4, -6, -1)

        for j in row_range:
            if plane == "horiz" or plane == "vert":
                x = i - j if not reverse else MAX_ROWS - j
                col_range = range(0, 5)
            elif plane == "diagleft" or plane == "diagright":
                x = j
                col_range = range(0, rows)

            for n in col_range:

                if x <= MAX_ROWS and x >= 0 and n <= MAX_ROWS and n >= 0:
                    if plane == "horiz" or plane == "vert":
                        brightness = max(0, brightness)
                        pixel = (n, x) if plane == "vert" else (x, n)
                    elif plane == "diagleft" or plane == "diagright":
                        brightness = max(0, MAX_BRIGHTNESS-((rows-n)*2))
                        pixel = (x, n) if not reverse else (x, MAX_ROWS-n)

                    display.set_pixel(pixel[0], pixel[1], brightness)

            rows -= 1
            if plane == "horiz" or plane == "vert":
                brightness -= 2
        i += 1
        sleep(150)
