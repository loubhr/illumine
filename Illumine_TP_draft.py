import time
import sys
import select
import ipdb

import board
import adafruit_pixelbuf
#https://docs.circuitpython.org/en/latest/shared-bindings/adafruit_pixelbuf/

from adafruit_raspberry_pi5_neopixel_write import neopixel_write

# NeoPixels works with PWM so it must be connected to D12 or D13 on RPi5
pixel_pin = board.D12

# Number of LED
number_LED = 60

#brightness
bright = 0.5

# Ther order of the pixel colors - RGB or GRB. Some NeoPixels have red and green reversed ! In our case it is RGBW or GRBW
order = 'GRBW'

class Pi5Pixelbuf(adafruit_pixelbuf.PixelBuf):
    def __init__(self, pin, size, **kwargs):
        self._pin = pin
        super().__init__(size=size, **kwargs)

    def _transmit(self, buf):
        neopixel_write(self._pin, buf)

pixels = Pi5Pixelbuf(pixel_pin, number_LED, auto_write=False, byteorder=order) 
red = 0
green = 0
blue = 0

try:
    while True:
        if select.select([sys.stdin], [], [], 0.0)[0]:
            key = sys.stdin.read(1)
            if key == 'i':
                print("Give a new color to NeoPixel")
                red = int(input("Red channel value: "))
                green = int(input("Green channel value: "))
                blue = int(input("Blue channel value: "))
                #Clamp value to 0-255
                red = max(0, min(255, red))
                green = max(0, min(255, green))
                blue = max(0, min(255, blue))
                pixels.fill((red, green, blue))
                pixels.show()

            if key == 'q':
                print("Quitting...")
                pixels.fill((0, 0, 0))
                pixels.show()
                exit()

        pixels.fill((red*bright, green*bright, blue*bright))
        pixels.show()
        time.sleep(1)
        pixels.fill((255*bright, 0, 0))
        pixels.show()
        time.sleep(1)
        pixels.fill((255*bright, 0, 255*bright))
        pixels.show()
        time.sleep(1)
        pixels.fill((0, 0, 255*bright))
        pixels.show()
        time.sleep(1)

except KeyboardInterrupt:
    print("\nLoop stopped by user")
    pixels.fill((0, 0, 0))
    pixels.show()

