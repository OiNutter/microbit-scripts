from microbit import *
import random

letters = ['A', 'B']

def get_letter():
    return random.choice(letters)

display.scroll("RAINMAN")

display.scroll('Press any button to play', wait=False, loop=True)
while True:
    if button_a.is_pressed() or button_b.is_pressed():
        print("start playing")
        break

display.clear()

seq_length = 3
round = 1
pause = 500
correct = True

def init():
    global seq_length, round, pause, correct
    seq_length = 3
    round = 1
    pause = 500
    correct = True
    display.clear()

init()

while True:

    # Draw seperator
    for y in range(0, 5):
        display.set_pixel(2, y, 5)

    # Get sequence
    sequence = []
    for i in range(0, seq_length):
        # Clear previous
        for x in range(0, 5):
            if x != 2:
                for y in range(0, 5):
                    display.set_pixel(x, y, 0)
        sleep(pause)

        letter = get_letter()
        sequence.append(letter)

        print(letter)

        if letter == 'A':
            for x in range(0, 2):
                for y in range(0, 5):
                    display.set_pixel(x, y, 9)
        elif letter == 'B':
            for x in range(3, 5):
                for y in range(0, 5):
                    display.set_pixel(x, y, 9)

        sleep(500)

    display.clear()

    # Await input
    correct = True
    reset = False
    print("ENTERED:");
    for letter in sequence:
        while correct:
            entered = ""
            if button_a.is_pressed() or button_b.is_pressed():
                if button_a.is_pressed():
                    while button_a.is_pressed():
                        continue
                    entered = "A"
                else:
                    while button_b.is_pressed():
                        continue
                    entered = "B"

                print ("%s:%s" % (letter, entered))
                if entered != letter:
                    correct = False
                else:
                    break

        if not correct:
            display.scroll("X")
            display.scroll("You reached level: %d" % round, wait=False, loop=True)

            while True:
                if button_a.is_pressed() or button_b.is_pressed():
                    init()
                    reset = True
                    break

        if reset:
            break

    round += 1
    seq_length += 1
