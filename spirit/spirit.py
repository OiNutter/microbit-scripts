from microbit import *

min_tilt = -512
max_tilt = 512
tilt_range = max_tilt - min_tilt
mode = "crosshair"

while True:

    tilt_x = accelerometer.get_x()
    tilt_x = min(max(min_tilt, tilt_x), max_tilt)

    tilt_x = ((tilt_x-min_tilt)/tilt_range) * 5
    tilt_x = min(max(0, tilt_x), 4)
    tilt_x = int(tilt_x)

    tilt_y = accelerometer.get_y()
    tilt_y = min(max(min_tilt, tilt_y), max_tilt)

    tilt_y = ((tilt_y-min_tilt)/tilt_range) * 5
    tilt_y = min(max(0, tilt_y), 4)
    tilt_y = int(tilt_y)

    for x in range(0, 5):
        for y in range(0, 5):
            if mode == "flow":
                brightness = int(min((9 - (abs(x-tilt_x)*3)), (9-(abs(y-tilt_y)*3))))
            else:
                brightness = 9 if x == tilt_x or y == tilt_y else 3

            display.set_pixel(x, y, min(max(0, brightness), 9))

    if button_a.is_pressed():
        mode = "crosshair"

    if button_b.is_pressed():
        mode = "flow"
