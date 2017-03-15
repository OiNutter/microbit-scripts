from microbit import *
import random

score = 0
pixel = None
fade_step = 300
clicked = False
MAX_PAUSE = 3000


def get_rand_coord(limit=4):
    return random.randint(0, limit)


def get_rand_side():
    return random.choice([-1, 1])


def handle_correct_click(i):
    global score, clicked
    clicked = True
    score += (i+1)*10
    display.set_pixel(pixel[0], pixel[1], 0)
    sleep(1000)

display.scroll("REFLEX")

display.scroll('Press any button to play', wait=False, loop=True)
while True:
    if button_a.is_pressed() or button_b.is_pressed():
        print("start playing")
        break

display.clear()
while True:

    for y in range(0, 5):
        display.set_pixel(2, y, 5)

    for r in range(1, 16):

        print("ROUND %d" % r)
        wait_time = random.random()*MAX_PAUSE
        print ("WAIT %d", wait_time)

        start_time = running_time()
        diff = 0
        while diff <= wait_time:

            new_time = running_time()
            diff = new_time - start_time

        y = get_rand_coord()
        x = (get_rand_side() * (get_rand_coord(1)+1)) + 2

        pixel = (x, y)

        print(pixel)

        clicked = False
        for i in range(9, -1, -1):
            display.set_pixel(pixel[0], pixel[1], i)

            start_time = running_time()
            diff = 0
            while diff <= fade_step and not clicked:
                if x < 2:

                    if button_a.is_pressed():
                        while button_a.is_pressed():
                            continue
                        handle_correct_click(i)
                        break
                    elif button_b.is_pressed():
                        while button_b.is_pressed():
                            continue
                        score -= 10

                elif x > 2:

                    if button_b.is_pressed():
                        while button_b.is_pressed():
                            continue
                        handle_correct_click(i)
                        break
                    elif button_a.is_pressed():
                        while button_a.is_pressed():
                            continue
                        score -= 10

                new_time = running_time()
                diff = new_time - start_time

        pixel = None

        if r % 5 == 0:

            fade_step -= 25
            print ("%d: %d" % (r, fade_step))

    display.scroll("Score: %d" % score, wait=False, loop=True)

    while True:
        if button_a.is_pressed() or button_b.is_pressed():
            display.clear()
            break
