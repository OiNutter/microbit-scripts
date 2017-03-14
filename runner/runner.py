from microbit import *
import random

MAX_COLS = 5
PAUSE = 500

def init():
    global blocks, wait, player, old_player, jump_counter, start, counter, lives, jump_held, jump_amount, jump_maxed, PAUSE

    blocks = []
    wait = 0
    player = [1, 4]
    old_player = None
    jump_counter = 0
    start = counter = running_time()
    lives = 3
    jump_held = False
    jump_amount = 0
    jump_maxed = False
    PAUSE = 500

def handle_obstacles():
    global blocks, wait

    # Make sure there's been enough times between blocks
    if wait == 0:
        # Do we want to create block?
        if random.choice([True, False]):
            blocks.append(MAX_COLS)
            wait = 2

            # Are we making this a double?
            if random.choice([True, False]):
                blocks.append(MAX_COLS+1)
                wait += 2

    else:
        wait -= 1

    # Draw the blocks
    for i in range(0, len(blocks)):
        if blocks[i] < MAX_COLS:
            # Hide the previous block position
            if player[0] != blocks[i] or player[1] != 4:
                display.set_pixel(blocks[i], 4, 0)

        # Move the block
        blocks[i] -= 1
        if blocks[i] >= 0 and blocks[i] < MAX_COLS:
            display.set_pixel(blocks[i], 4, 3)

    # Clear any blocks that have gone off screen
    while len(blocks) > 0 and blocks[0] == -1:
        blocks.pop(0)

def draw_player ():
    global old_player, player

    # If the player has moved turn off the old position
    if old_player is not None:
        display.set_pixel(old_player[0], old_player[1], 0)
        old_player = None

    # display the player
    display.set_pixel(player[0], player[1], 9)


def jump():
    global player, jump_counter, old_player

    # Create a ref to the old position
    old_player = player[:]

    # Change the y position by the current jump amount
    player[1] = 4 - (jump_amount)
    jump_counter += 1

def check_collision():
    global lives

    # Check the player isn't jumping
    if player[1] == 4:
        # Is the player in the position of a block?
        if player[0] in blocks:
            # If so remove a life
            display.set_pixel(4-lives+1, 0, 0)
            lives -= 1

def display_lives():

    if lives > 0:
        for i in range(4, 4 - lives, -1):
            display.set_pixel(i, 0, 5)

init()

display.scroll("RUNNER")

display.scroll('Press any button to play', wait=False, loop=True)
while True:
    if button_a.is_pressed() or button_b.is_pressed():
        display.clear()
        while button_a.is_pressed() or button_b.is_pressed():
            sleep(0.1)
        break

while True:

    while True:
        if button_a.is_pressed():

            # Check the button has been released and they're not at the max jump height
            if jump_held == False and jump_maxed == False:
                jump_amount = min(2, jump_amount + 1)
                jump_maxed = jump_amount == 2
                jump_held = True
                jump()
        else:
            jump_held = False

        # Update everything every 500ms (this speeds up as the game goes on)
        if running_time() - counter >= PAUSE:


            if jump_counter == 0:
                # If they've just finished jumping bring them back to the ground
                if jump_amount > 0:
                    jump_amount = max(0, jump_amount - 1)

                    old_player = player[:]
                    player[1] = 4 - jump_amount
                    if player[1] == 4:
                        jump_maxed = False
            else:
                jump_counter -= 1

            draw_player()
            handle_obstacles()
            check_collision()
            display_lives()

            counter = running_time()

        if round(running_time() / PAUSE) % 20 == 0:
            PAUSE -= 50

        if lives == 0:
            break
        else:
            sleep(0.1)

    display.scroll("SCORE: %ds" % round(running_time() - start), wait=False, loop=True)

    sleep(100)
    while True:

        if button_a.is_pressed() or button_b.is_pressed():
            init()
            display.clear()
            break
