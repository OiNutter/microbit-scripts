# Import required modules and methods
from microbit import display, button_a, button_b, sleep

# Define constants
MAX_ROWS=4

# Set up defaults
reverse = False

#Define our reusable scan function
def scan(level, pause=500):
    # Mark reverse as global so we can update it from this method
    global reverse

    # Loop through the various rows of our square. As we're going diagonally we need to loop
    # 9 times.
    for i in range(0, 10):
        rows = i

        # if we press a button reverse the direction
        if button_a.is_pressed() or button_b.is_pressed():
            reverse = False if reverse else True

        # Start looping over the pixel grid
        for x in range(0, i+1):
            for y in range(0, rows+1):

                # If the pixel we're trying to set wouldn't be on the grid
                # then don't try and set it
                if x <= MAX_ROWS and y <= MAX_ROWS:
                    x_coord = MAX_ROWS - x if reverse else x
                    y_coord = MAX_ROWS - y if reverse else y

                    display.set_pixel(x_coord, y_coord, level)
            rows = rows-1

        i+=1
        sleep(pause)

while True:

    # turn the lights on
    scan(9,150)

    # turn the lights off
    scan(0,150)
