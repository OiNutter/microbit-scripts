# Import required modules
from microbit import *
import random

# Initialise global vars
player = None
old_player = None
num_holes = 4
current_hole = None
holes = []
counters = []
score = 0


def init():
    global player, holes, counters, score
    display.clear()
    holes = []
    counters = []
    current_hole = None
    score = 0
    player = (2, 2)
    move_player(old_player, player)

    for i in range(0, num_holes):
        new_hole = (get_rand_coord(), get_rand_coord())
        while new_hole in holes or new_hole == player:
            new_hole = (get_rand_coord(), get_rand_coord())
        holes.append(new_hole)
        counters.append(0)

    draw_holes()


def move_player(old_player, new_player):
    if old_player and old_player not in holes:
        display.set_pixel(old_player[0], old_player[1], 0)
    elif old_player and old_player in holes:
        display.set_pixel(old_player[0], old_player[1], 5)
    display.set_pixel(new_player[0], new_player[1], 9)


def validate_coord_range(coord):
    return min(max_coord, max(min_coord, coord))


def validate_coord(coord):
    return int(min(4, max(0, coord)))


def get_rand_coord():
    return random.randint(0, 4)


def draw_holes():
    for i in range(0, len(holes)):
        display.set_pixel(holes[i][0], holes[i][1], 5)


def detect_collision(player):
    global holes, counters, current_hole
    if player in holes:
        hole = holes.index(player)
        if current_hole and hole != current_hole:
            counters[current_hole] = 0

        current_hole = hole
        counters[current_hole] += 1

        if counters[current_hole] == 8:
            for i in range(0, 10):
                display.set_pixel(holes[current_hole][0], holes[current_hole][1], 9-i)
                sleep(50)

            counters.pop(current_hole)
            holes.pop(current_hole)
            current_hole = None

    else:
        if current_hole:
            counters[current_hole] = 0
            current_hole = None

display.scroll("MARBLES")

display.scroll('Press any button to play', wait=False, loop=True)
while True:
    if button_a.is_pressed() or button_b.is_pressed():
        break

init()

while True:
    sleep(250)

    old_player = player

    # find new x coord
    x = accelerometer.get_x()

    if x > 100:
        x = old_player[0] + 1
    elif x < -100:
        x = old_player[0] - 1
    else:
        x = old_player[0]

    x = validate_coord(x)

    # find new y coord
    y = accelerometer.get_y()

    if y > 100:
        y = old_player[1] + 1
    elif y < -100:
        y = old_player[1] - 1
    else:
        y = old_player[1]

    y = validate_coord(y)

    player = (x, y)

    detect_collision(player)

    if len(holes) == 0:
        display.clear()
        display.show(Image.YES)
        sleep(2000)
        display.scroll("Time: %ds" % int(score/1000), wait=False, loop=True)

        while True:
            if button_a.is_pressed() or button_b.is_pressed():
                init()
                break
    else:
        move_player(old_player, player)
        score += 250

    if button_a.is_pressed() or button_b.is_pressed():
        init()
