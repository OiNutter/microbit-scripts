# Import required modules
from microbit import compass, display, accelerometer, sleep, button_a, button_b, running_time, Image
import random

commands = ["bop it", "twist it", "shake it", "tilt it"]
score = 0
WAIT_TIME = 2000

if not compass.is_calibrated():
    compass.calibrate()

#display.scroll("BOP IT")

display.scroll('Press any button to play', wait=False, loop=True)
while True:
    if button_a.is_pressed() or button_b.is_pressed():
        display.clear()
        while button_a.is_pressed() or button_b.is_pressed():
            sleep(0.1)
        break

while True:

    while True:
        command = random.choice(commands)
        display.scroll(command[:2])

        start = running_time()
        diff = 0
        correct = False

        # Get current state for comparison
        start_bearing  = compass.heading()
        start_x = accelerometer.get_x()
        start_y = accelerometer.get_y()
        while diff < WAIT_TIME:

            if command == "bop it":
                if button_a.is_pressed() and button_b.is_pressed():
                    correct = True
                    break
            elif command == "twist it":
                print (abs(compass.heading() - start_bearing))
                if abs(compass.heading() - start_bearing) >= 90:
                    correct = True
                    break
            elif command == "shake it":
                if accelerometer.current_gesture() == "shake":
                    correct = True
                    break
            elif command == "tilt it":
                if abs(start_x - accelerometer.get_x()) >= 100 or abs(start_y - accelerometer.get_y()) >= 100:
                    correct = True
                    break

            diff = running_time() - start

        if correct:
            display.show(Image.HAPPY)
            score += 1

            if score % 5 == 0:
                WAIT_TIME *= 0.9

            sleep(1000)
        else:
            display.show(Image.SAD)
            sleep(1000)
            break

    display.scroll("Score: %d" % score, wait=False, loop=True)

    while True:
        if button_a.is_pressed() or button_b.is_pressed():
            while button_a.is_pressed() or button_b.is_pressed():
                sleep(0.1)
            display.clear()
            score = 0
            break
