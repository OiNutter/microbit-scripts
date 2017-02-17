from microbit import *
import math

min_tilt = -256
max_tilt = 256
tilt_range = max_tilt - min_tilt
mode = "crosshair"

while True:

    tilt_x = accelerometer.get_x()
    tilt_x = min(max(min_tilt, tilt_x), max_tilt)

    tilt_y = accelerometer.get_y()
    tilt_y = min(max(min_tilt, tilt_y), max_tilt)

    if mode == "crosshair":
        tilt_x = ((tilt_x-min_tilt)/tilt_range) * 5
        tilt_x = min(max(0, tilt_x), 4)
        tilt_x = int(tilt_x)

        tilt_y = ((tilt_y-min_tilt)/tilt_range) * 5
        tilt_y = min(max(0, tilt_y), 4)
        tilt_y = int(tilt_y)
    else:
        start_x = 5+((abs(tilt_x)/max_tilt)*4)
        finish_x = 5-((abs(tilt_x)/max_tilt)*4)
        step_x = (finish_x - start_x)/4
        brightness_range_x = []

        start_y = 5+((abs(tilt_y)/max_tilt)*4)
        finish_y = 5-((abs(tilt_y)/max_tilt)*4)
        step_y = (finish_y - start_y)/4
        brightness_range_y = []

        i = 0
        while i < 5:
            brightness_range_x.append(start_x + (step_x*i))
            brightness_range_y.append(start_y + (step_y*i))
            i += 1

    for x in range(0, 5):
        for y in range(0, 5):
            if mode == "flow":

                x_coord = x if tilt_x <= 0 else 4 - x
                y_coord = y if tilt_y <= 0 else 4 - y
                brightness = round((brightness_range_x[x] + brightness_range_y[y])/2)

            else:

                brightness = 9 if x == tilt_x or y == tilt_y else 3
                x_coord = x
                y_coord = y

            display.set_pixel(x_coord, y_coord, min(max(0, brightness), 9))

    if button_a.is_pressed():
        mode = "crosshair"

    if button_b.is_pressed():
        mode = "flow"
