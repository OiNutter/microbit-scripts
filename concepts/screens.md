Game Screens
============

If you're writing a game, or any kind of interactive program, with your microbit, at some point you're going to want some kind of continue screen. Most of the games in this repo feature 2 types of screen; the waiting screen and the score screen. Deep down however they are just using the same methodology, just with different text.

How it works
------------

Lets start with a waiting screen as it's the simpler of the two to implement. For this we want to display the name of our game then a repeating message instructing the user to "Press any button to play". Once they press a button we want to start our game.

First up lets get our game name displaying on startup

``` python
from microbit import *
import random

def get_rand_coord(limit=4):
    return random.randint(0, limit)

# Display our game name
display.scroll("Dot")

# Do our "game" stuff
while True:
    display.clear()
    display.set_pixel(get_rand_coord(), get_rand_coord(), 9)
    sleep(1000)
```

If you run this you should see `Dot` scroll across the screen, then our "game" will start. Ok, it's really just lighting up a random led every second but it's doing something. Now we want to make it wait until we're ready to start before it starts the disco.

To do this we're going to pass some extra keyword arguments to our display.scroll method.

* `wait = False` - This will tell the display function not to block the script from continuing, essentially moving the execution into the background and letting us run other code while it scrolls.
* `loop = True` - This tells the scroll function to keep scrolling the text until we start doing something else with the display.

We're then going to start a `while` loop that will keep checking for either button being pressed and once one is pressed, move us on to the next part of our game.

``` python
from microbit import *
import random

def get_rand_coord(limit=4):
    return random.randint(0, limit)

# Display our game name
display.scroll("Dot")

# Display start screen
display.scroll('Press any button to play', wait=False, loop=True)

# Start waiting for buttons to be clicked
while True:
    if button_a.is_pressed() or button_b.is_pressed():
        # Wait until the button is released
        while button_a.is_pressed() or button_b.is_pressed():
            continue
        # Break the loop and continue to the rest of the game
        break

# Do our "game" stuff
while True:
    display.clear()
    display.set_pixel(get_rand_coord(), get_rand_coord(), 9)
    sleep(1000)

```

If you run this now it should keep scrolling "Press any button to play" until you press something.

Finally we'll add a "Score" screen and demonstrate resetting the game once the user clicks a button.

``` python
from microbit import *
import random

def get_rand_coord(limit=4):
    return random.randint(0, limit)

# Display our game name
display.scroll("Dot")

# Display start screen
display.scroll('Press any button to play', wait=False, loop=True)

# Start waiting for buttons to be clicked
while True:
    if button_a.is_pressed() or button_b.is_pressed():
        # Wait until the button is released
        while button_a.is_pressed() or button_b.is_pressed():
            continue
        # Break the loop and continue to the rest of the game
        break

# Do our "game" stuff
counter = 1
now = running_time()
display.clear()
display.set_pixel(get_rand_coord(), get_rand_coord(), 9)
while True:

    # Light up a differnet pixel every second
    if running_time() - now >= 1000:
        display.clear()
        display.set_pixel(get_rand_coord(), get_rand_coord(), 9)
        now = running_time()
        counter += 1

    # When a button is pressed we want to display the number of lights we've displayed
    if button_a.is_pressed() or button_b.is_pressed():
        # Wait until the button is released
        while button_a.is_pressed() or button_b.is_pressed():
            continue

        # Display the number of lights and wait for a button to be pressed to restart
        display.scroll("Lights: %d" % counter, wait=False, loop=True)

        while True:
            if button_a.is_pressed() or button_b.is_pressed():
                while button_a.is_pressed() or button_b.is_pressed():
                    continue
                counter = 1
                now = running_time()
                display.clear()
                display.set_pixel(get_rand_coord(), get_rand_coord(), 9)
                break

    # Sleep a little bit to save cpu
    sleep(0.1)
```

We've now changed our game mechanic slightly so rather than sleeping for a second it checks the `running_time` and only executes when it's been a second since it last displayed a pixel. This lets us be more responsive to the button press.

Once a button is pressed the game will loop the "Lights" message with the number of times we've lit up a pixel until a button is pressed. When we press the button it will reset everything back to the start and continue as before. In practice you'd want to wrap that up into a reusable function.

So there you have a neat way of creating holding screens for your program, how are you going to use them?
