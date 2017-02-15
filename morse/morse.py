# Import modules
from microbit import *

# define morse code dictionary
morse = {
    "a": ".-",
    "b": "-...",
    "c": "-.-.",
    "d": "-..",
    "e": ".",
    "f": "..-.",
    "g": "--.",
    "h": "....",
    "i": "..",
    "j": ".---",
    "k": "-.-",
    "l": ".-..",
    "m": "--",
    "n": "-.",
    "o": "---",
    "p": ".--.",
    "q": "--.-",
    "r": ".-.",
    "s": "...",
    "t": "-",
    "u": "..-",
    "v": "...-",
    "w": ".--",
    "x": "-..-",
    "y": "-.--",
    "z": "--..",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    "0": "-----"
}

current_letter = ""
pressed = 0
paused = 0
letters = []

def detect_dot_dash(time_pressed):
    return "." if time_pressed <= 50 else "-"

def get_letter(code):
    global morse
    for key,value in morse.items():
        if code == value:
            return key

    return ""

while True:
    sleep(1) # do not use all the cpu power
    # make a loop to test for the button being pressed
    if button_a.is_pressed():
        if paused >= 100:
            letters.append(get_letter(current_letter))
            current_letter = ""

            if paused >= 200:
                letters.append("_")

            paused = 0

        pressed = 1
        while button_a.is_pressed():
            # wait until the button is not pressed any more
            sleep(1) # do not use all the cpu power
            pressed += 1
        # measure the time
        current_letter += detect_dot_dash(pressed)
        paused = 1
    else:
        if paused > 0:
            paused +=1

    if button_b.is_pressed() or accelerometer.current_gesture() == "shake":
        letters.append(get_letter(current_letter))
        display.scroll("".join(letters))
        paused = 0
        pressed = 0
        current_letter = ""
        letters = []
