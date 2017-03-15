Buttons
=======

Detecting whether a button is clicked on the microbit is pretty straightforward.

``` python
from microbit import *

while True:
    if button_a.is_pressed():
        display.show(Image.HAPPY)
    else:
        display.show(Image.SAD)

```

Pretty simple, the display while show a sad face unless we're holding down the A button, but what if we want something a bit more precise?

In our [Reflex](../reflex/README.md) game the player has to click the button as soon as the light appears. Lets give that a try:

``` python
from microbit import *
import random

MAX_PAUSE = 2000 # Max wait of 2 seconds
score = 0

def get_rand_coord(limit=4):
    return random.randint(0, limit)

while True:

    # Get a random time to wait
    wait_time = random.random()*MAX_PAUSE

    # Wait until that time has passed
    start_time = running_time()
    diff = 0
    while diff <= wait_time:

        new_time = running_time()
        diff = new_time - start_time

    # Get a random coordinate for the light
    pixel = (get_rand_coord(), get_rand_coord())

    # Display it
    display.set_pixel(pixel[0], pixel[1], 9)

    # work out how long before the button is pressed
    now = running_time()
    diff = 0

    # Give the player 5 seconds to click the button
    while diff < 5000:
        if button_a.is_pressed():
            score += 10
            display.scroll("%d" % score)
            break

        diff = running_time() - now

    display.clear()

```

This script is a lot more complicated but the main bit we're concerned with is this snippet:

``` python
while diff < 5000:
    if button_a.is_pressed():
        score += 10
        display.scroll("%d" % score)
        break

    diff = running_time() - now
```

If you run that whole script and hold down the a button you'll see your score just keeps on going up. Nice for you but not much of a challenge. So we need to wait until the button is released before letting the script continue. Change that block of code to this and try again:

``` python
while diff < 5000:
    if button_a.is_pressed():
        while button_a.is_pressed():
            continue

        score += 10
        display.scroll("%d" % score)
        break

    diff = running_time() - now
```

Hopefully it should now be waiting until you release the button before giving you your score. So what are we actually doing here? The `while` instructs the program to stay within the enclosed block of code until the given condition, in this case button A being pressed, is no longer `True`. For the purposes of this example we just tell the program to `continue` meaning it will carry on in the loop without doing anything. However we could also use this to do stuff while the button is pressed, like in our morse code script.

Morse code defines letters and numbers as a series of dots and dashes. These can be entered into the program using long and short presses of the button. So lets have a look at how we could do that:

``` python
from microbit import *

message = ""

while True:

    if button_a.is_pressed():

        counter = 0
        while button_a.is_pressed():
            counter += 1
            sleep(1000)

        if counter == 1:
            message += "."
        elif counter >= 1:
            message += "-"


    if button_b.is_pressed():
        break

display.scroll(message)

```

This is a very simple example, and a bit flawed (this would be better accomplished using `running_time()`) but it helps illustrate what we're trying to achieve. While the button is pressed we increase the counter by one for every second it's held. A count of one is a `.` and a count of more than one is a `-`. Click the B button to see what you've entered.

So there you have some basic button interactions, what can you use them for?
