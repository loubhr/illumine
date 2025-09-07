import time
import sys
import board
import adafruit_pixelbuf

import RPi5_Neopixel as np

# Demo of all the functions

tape = np.Neopixel_Tape()

def main():

    tape.on_all_led('medium_turquoise')
    time.sleep(0.9)

    tape.on_led(20, 'pink')
    time.sleep(0.5)

    tape.on_led(30, 'chartreuse')
    time.sleep(0.5)

    tape.on_led(38, 'light_indigo')
    time.sleep(0.5)

    tape.on_led(47, 'coral')
    time.sleep(0.5)

    tape.on_led(55, 'tomato_pink')
    time.sleep(0.5)

    tape.on_led(34, 'pale_yellow')
    time.sleep(0.5)

    tape.on_all_led('cornflower_blue')
    time.sleep(0.9)

    tape.croise('golden_orange', 1)
    time.sleep(0.1)

    tape.fill_rainbow()
    time.sleep(0.9)

    tape.random('thistle_purple', 30, 0.03)
    time.sleep(0.1)

    tape.clignote_all('pumpkin', 10, 0.03)
    tape.clignote_all('rosy_brown', 10, 0.03)
    tape.clignote_all('dodger_blue', 10, 0.03)
    time.sleep(0.5)

    tape.on_all_led('hot_pink')
    time.sleep(0.9)

    tape.chariot('blood_red', 1)
    time.sleep(0.1)

    tape.on_all_led('blue_violet')
    time.sleep(0.9)

    tape.charge('forest_green', 1)
    time.sleep(0.1)

    tape.rainbow_cycle(10, 0.005)


if __name__ == "__main__":

    try: 
        while True:
            main()
    
    except KeyboardInterrupt:
        tape.off_all_led()
        sys.exit()

