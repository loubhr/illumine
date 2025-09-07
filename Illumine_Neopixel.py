import time
import sys
import select
import ipdb

import board
import adafruit_pixelbuf
#https://docs.circuitpython.org/en/latest/shared-bindings/adafruit_pixelbuf/

from adafruit_raspberry_pi5_neopixel_write import neopixel_write

# NeoPixels works with PWM so it must be connected to D12 or D13 on RPi5

# The order of the pixel colors - RGB or GRB. Some NeoPixels have red and green reversed ! In our case it is RGBW or GRBW

class Pi5Pixelbuf(adafruit_pixelbuf.PixelBuf):
    def __init__(self, pin, size, **kwargs):
        self._pin = pin
        super().__init__(size=size, **kwargs)

    def _transmit(self, buf):
        neopixel_write(self._pin, buf)

def wheel(pos):
     # Let's divide the tape in 3 parts, one for red nuances, green nuances, blue nuances
    if pos < 0 or pos > 255:
         r = g = b = 0
    elif pos < 85:
         r = int(pos * 3)
         g = int(255 - pos * 3)
         b = 0
    elif pos < 170:
         pos -= 85
         r = int(255 - pos * 3)
         g = 0 
         b = int(pos * 3)
    else:
         pos -= 170
         r = 0
         g = int(pos * 3)
         b = int(255 - pos * 3)
    return (r, g, b, 0)


class Illumine_Neopixel: #je ne fais pas une classe fille, héritage

    def __init__(self): #ma classe est un chef d'orchestre, je créé l'attribut
        self.pixels = Pi5Pixelbuf(board.D12, 60, auto_write=False, byteorder='GRBW') #en C++ ça s'appelle un pointeur vers l'objet hardware (vers ma pin hardware qui ne peut être controlée que par un code en même temps)

    def rainbow_cycle(self, wait):
        num_pixels = 60
        for j in range(255):
            for i in range(num_pixels):
               # ipdb.set_trace()
                pixel_index = (i * 256 // num_pixels) + j
                self.pixels[i] = wheel(pixel_index & 255)
            self.pixels.show()
            time.sleep(wait)


def main():
    try:
        illumine = Illumine_Neopixel()
        while True:
            illumine.rainbow_cycle(0.05)

    except KeyboardInterrupt:
        print("LED turned off by user. Exiting...")
        illumine.pixels.fill((0, 0, 0))
        illumine.pixels.show()
        sys.exit(0)


if __name__ == '__main__':
    main()
