from microbit import *

def loop(min_coord, max_coord, brightness):
    x = min_coord
    y = min_coord
    while x <= max_coord:

        display.set_pixel(x, y, brightness)
        x += 1
        sleep(150)

    x -= 1
    y += 1
    while y <= max_coord:
        display.set_pixel(x, y, brightness)
        y += 1
        sleep(150)

    x -= 1
    y -= 1
    while x >= min_coord:
        display.set_pixel(x, y, brightness)
        x -= 1
        sleep(150)

    x += 1
    y -= 1

    while y >= (min_coord + 1):
        display.set_pixel(x, y, brightness)
        y -= 1
        sleep(150)


def do_fade(brightness_range):
    for brightness in brightness_range:
        start = 0
        fin = 4
        while start <= fin:
            loop(start, fin, max(0, min(9, brightness)))
            start += 1
            fin -= 1

do_fade(range(9, -1, -3))

while True:

    do_fade(range(3, 10, 3))
    do_fade(range(6, -1, -3))
