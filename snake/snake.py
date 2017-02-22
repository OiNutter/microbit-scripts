# Import modules
from microbit import *
import random

MAX_ROWS = 4

directions = ["up", "right", "down", "left"]
direction = "up"
pixels = []
start = (2, 2)
marker = None
score = 0
marker_counter = 0


def init():
    global direction, pixels, start, marker, score, marker_counter
    direction = "up"
    pixels = []
    start = (2, 2)
    marker = None
    score = 0
    marker_counter = 0

    display.set_pixel(start[0], start[1], 9)
    pixels.append(start)


def get_rand_coord():
    return random.randint(0, 4)


def valid_coord(pixel):
    return pixel[0] >= 0 and pixel[0] <= MAX_ROWS and pixel[1] >= 0 and pixel[1] <= MAX_ROWS

display.scroll("SNAKE")

display.scroll('Press any button to play', wait=False, loop=True)
while True:
    if button_a.is_pressed() or button_b.is_pressed():
        display.clear()
        while button_a.is_pressed() or button_b.is_pressed():
            sleep(0.1)
        break

while True:

    init()

    while True:
        new_pixel = None

        now = running_time()
        diff = 0

        while diff <= 500:

            # Replace 1 with commented block if you want left and right to
            # switch when moving down
            mod = 1  # -1 if direction == "down" else 1

            if button_a.is_pressed():
                while button_a.is_pressed():
                    sleep(0.1)

                index = directions.index(direction) - (1*mod)
                direction = directions[index]
            elif button_b.is_pressed():
                while button_b.is_pressed():
                    sleep(0.1)
                index = directions.index(direction) + (1*mod)
                if index >= len(directions):
                    index = 0

                direction = directions[index]

            diff = running_time() - now

        if direction == "up":
            new_pixel = (start[0], start[1]-1)
        elif direction == "down":
            new_pixel = (start[0], start[1]+1)
        elif direction == "left":
            new_pixel = (start[0]-1, start[1])
        elif direction == "right":
            new_pixel = (start[0]+1, start[1])

        if valid_coord(new_pixel) and new_pixel not in pixels:

            if new_pixel == marker:
                print ("HIT MARKER")
                pixels.insert(0, marker)
                score += 10
                marker = None
                marker_counter = 1

            old_pixel = pixels.pop()
            display.set_pixel(old_pixel[0], old_pixel[1], 0)
            pixels.insert(0, new_pixel)
            start = new_pixel
        else:
            break

        print (len(pixels))

        i = 0
        for pixel in pixels:
            brightness = round(9 - ((i/len(pixels))*8))
            display.set_pixel(pixel[0], pixel[1], brightness)
            i += 1

        if not marker:
            if marker_counter == 0:
                marker = (get_rand_coord(), get_rand_coord())
                while marker in pixels:
                    marker = (get_rand_coord(), get_rand_coord())

                display.set_pixel(marker[0], marker[1], 5)
            else:
                marker_counter -= 1

    display.scroll("Score: %d" % score, wait=False, loop=True)

    while True:
        if button_a.is_pressed() or button_b.is_pressed():
            while button_a.is_pressed() or button_b.is_pressed():
                sleep(0.1)
            display.clear()
            init()
            break
