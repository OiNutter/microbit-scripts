# Import modules
from microbit import *
import radio

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
morse_string = ""
pressed = 0
paused = 0
letters = []

radio.on()

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

    #check for incoming messages
    incoming = radio.receive()
    if incoming is not None:
        print(incoming.split("|"))
        sent_letters = []

        for letter in incoming.split("|"):
            sent_letters.append(get_letter(letter) if letter != " " else " ")

        display.scroll("".join(sent_letters))

    # make a loop to test for the button being pressed
    if button_a.is_pressed():
        if paused >= 100:
            letters.append(get_letter(current_letter))
            morse_string += current_letter + "|"
            current_letter = ""

            if paused >= 200:
                letters.append(" ")
                morse_string += "| |"

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
        morse_string += current_letter
        display.scroll("".join(letters))
        paused = 0
        pressed = 0
        print(morse_string)
        radio.send(morse_string)
        current_letter = ""
        morse_string = ""
        letters = []
