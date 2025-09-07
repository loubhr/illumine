import time
import sys
import select
import ipdb
import argparse
import numpy

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


class Neopixel_Tape: 

    def __init__(self): #ma classe est un chef d'orchestre, je créé l'attribut
        self.pixels = Pi5Pixelbuf(board.D12, 60, auto_write=False, byteorder='GRBW') #en C++ ça s'appelle un pointeur vers l'objet hardware (vers ma pin hardware qui ne peut être controlée que par un code en même temps)
        self.colors_list = {
                    "red": (255, 0, 0),
                    "dark_red": (255, 5, 0),
                    "red_orange": (255, 12, 0),
                    "crimson": (255, 26, 0),
                    "rust": (255, 45, 0),
                    "blood_red": (255, 80, 0),
                    "tomato": (255, 102, 0),
                    "reddish_orange": (255, 129, 0),
                    "burnt_orange": (255, 141, 0),
                    "pumpkin": (255, 153, 0),
                    "orange": (255, 180, 0),
                    "dark_orange": (255, 192, 0),
                    "golden_orange": (255, 219, 0),
                    "yellow_orange": (255, 231, 0),
                    "yellow": (243, 255, 0),
                    "bright_yellow": (231, 255, 0),
                    "lemon_yellow": (204, 255, 0),
                    "pale_yellow": (192, 255, 0),
                    "lime_yellow": (165, 255, 0),
                    "chartreuse": (150, 255, 0),
                    "spring_green": (123, 255, 0),
                    "light_green": (111, 255, 0),
                    "green": (84, 255, 0),
                    "dark_green": (69, 255, 0),
                    "forest_green": (57, 255, 0),
                    "teal_green": (30, 255, 0),
                    "teal": (0, 255, 18),
                    "bright_turquoise": (0, 255, 57),
                    "medium_turquoise": (0, 255, 75),
                    "dark_turquoise": (0, 255, 96),
                    "cyan": (0, 255, 114),
                    "light_cyan": (0, 255, 135),
                    "aqua": (0, 255, 153),
                    "light_sky_blue": (0, 255, 192),
                    "cornflower_blue": (0, 255, 213),
                    "steel_blue": (0, 255, 231),
                    "dodger_blue": (0, 231, 255),
                    "light_blue": (0, 204, 255),
                    "powder_blue": (0, 192, 255),
                    "cadet_blue": (0, 177, 255),
                    "lavender_blue": (0, 150, 255),
                    "light_indigo": (18, 0, 255),
                    "indigo": (36, 0, 255),
                    "blue_violet": (57, 0, 255),
                    "purple": (96, 0, 255),
                    "medium_purple": (114, 0, 255),
                    "orchid": (135, 0, 255),
                    "violet": (153, 0, 255),
                    "thistle_purple": (192, 0, 255),
                    "pink_purple": (213, 0, 255),
                    "magenta": (231, 0, 255),
                    "fuchsia": (255, 0, 243),
                    "hot_pink": (255, 0, 228),
                    "light_pink": (255, 0, 201),
                    "pink": (255, 0, 174),
                    "light_coral": (255, 0, 147),
                    "salmon_pink": (255, 0, 120),
                    "coral": (255, 0, 93),
                    "tomato_pink": (255, 0, 50),
                    "rosy_brown": (255, 0, 18)
                }


    def find_color(self, color_name='purple'):
        """Trouve le tuple RGB correspondant au nom de couleur donné
        
        color_name: nom de la couleur à trouver
        
        """
        if color_name in self.colors_list:
            return self.colors_list[color_name]
        else:
            print(f"Color '{color_name}' not found. Using default color purple..")
            return (128, 0, 128)  # Default to purple if color not found
            

    def on_led(self, num, color_name='purple'):
        """Allume une LED spécifique avec le nom de couleur donné

        color_name: nom de la couleur à utiliser
        
        """
        color = self.find_color(color_name)
        self.pixels[num] = color
        self.pixels.show()
        time.sleep(0.03)

    
    def off_led(self, num):
        """Éteint une LED spécifique"""

        self.pixels[num] = (0, 0, 0)
        self.pixels.show()
        time.sleep(0.03)


    def on_all_led(self, color_name='purple'):
        """Allume toutes les LEDs avec le nom de couleur donné
            
        color_name: nom de la couleur à utiliser
        
        """
        color = self.find_color(color_name)
        self.pixels.fill(color)
        self.pixels.show()
        time.sleep(0.03)

    
    def off_all_led(self): 
        """Éteint toutes les LEDs"""

        self.pixels.fill((0, 0, 0))
        self.pixels.show()
        time.sleep(0.03)

    
    def avance(self, num, color_name, add=1):
        """Déplace la LED allumée vers l'avant d'un certain nombre de positions, en éteignant la LED précédente.

         color_name: nom de la couleur à utiliser
         add: nombre de positions à avancer
         
         """
        color = self.find_color(color_name)
        self.pixels[num] = (0, 0, 0)
        self.pixels[num + add] = color
        self.pixels.show()
        time.sleep(0.03)

    
    def recule(self, num, color_name, sub=1):
        """Déplace la LED allumée vers l'arrière d'un certain nombre de positions, en éteignant la LED précédente.

         color_name: nom de la couleur à utiliser
         sub: nombre de positions à reculer
         
         """
        color = self.find_color(color_name)
        self.pixels[num] = (0, 0, 0)
        self.pixels[num - sub] = color
        self.pixels.show()
        time.sleep(0.03)


    def clignote(self, num, color_name, times=5, wait=0.03):
        """Fait clignoter une LED spécifique un certain nombre de fois avec le nom de couleur donné
        
         color_name: nom de la couleur à utiliser
         wait: temps d'attente entre allumé et éteint
         times: nombre de clignotements
         
         """
        for i in range(times):
            self.on_led(num, color_name)
            time.sleep(wait)
            self.off_led(num)
            time.sleep(wait)


    def clignote_all(self, color_name, times=5, wait=0.03):
        """Fait clignoter toutes les LEDs un certain nombre de fois avec le nom de couleur donné
        
         color_name: nom de la couleur à utiliser
         wait: temps d'attente entre allumé et éteint
         times: nombre de clignotements
         
         """
        for i in range(times):
            self.on_all_led(color_name)
            time.sleep(wait)
            self.off_all_led()
            time.sleep(wait)

    
    def random(self, color_name, times=5, wait=0.03):
        """Allume des LEDs aléatoires un certain nombre de fois avec le nom de couleur donné
        
         color_name: nom de la couleur à utiliser
         wait: temps d'attente entre allumé et éteint
         times: nombre de fois où une LED aléatoire est allumée
         
         """
        num_pixels = 60
        for i in range(times):
            rand_pos = numpy.random.randint(0, num_pixels)
            self.on_led(rand_pos, color_name)
            time.sleep(wait)
            self.off_led(rand_pos)
            time.sleep(wait)

    
    def chariot(self, color_name, times=2):
        """Déplace une LED allumée d'avant en arrière sur la bande un certain nombre de fois avec le nom de couleur donné
        
         color_name: nom de la couleur à utiliser
         times: nombre d'allers-retours
         
         """
        num_pixels = 60
        self.on_led(0, color_name)
        i = 0
        for j in range(times):
            while i < num_pixels - 1:
                self.avance(i, color_name, add=1)
                i += 1
            while i > 0:
                self.recule(i, color_name, sub=1)
                i -= 1
        self.off_all_led()

    
    def deux_chariots(self, color_name, times=2):
        """Déplace deux LEDs allumées d'avant en arrière sur la bande un certain nombre de fois avec le nom de couleur donné
        
         color_name: nom de la couleur à utiliser
         times: nombre d'allers-retours
         
         """
        num_pixels = 60
        self.on_led(0, color_name)
        self.on_led(1, color_name)
        i = 0
        for j in range(times):
            while i < num_pixels - 2:
                self.avance(i, color_name, add=1)
                self.avance(i + 1, color_name, add=1)
                i += 1
            while i > 0:
                self.recule(i + 1, color_name, sub=1)
                self.recule(i, color_name, sub=1)
                i -= 1
        self.off_all_led()


    def croise(self, color_name, times=2):
        """Fait se croiser deux LEDs allumées depuis les deux extrémités de la bande un certain nombre de fois avec le nom de couleur donné
        
         color_name: nom de la couleur à utiliser
         times: nombre d'allers-retours
         
         """
        num_pixels = 60
        self.on_led(0, color_name)
        self.on_led(59, color_name)
        i = 0
        for j in range(times):
            while i < num_pixels - 1:
                self.avance(i, color_name, add=1)
                self.recule(59 - i, color_name, sub=1)
                i += 1
            i = 0 
            while i < num_pixels - 1:
                self.avance(i, color_name, add=1)
                self.recule(59 - i, color_name, sub=1)
                i += 1
        self.off_all_led()


    def charge(self, color_name, times=2):
        """Remplit et vide la bande un certain nombre de fois avec le nom de couleur donné
        
         color_name: nom de la couleur à utiliser
         times: nombre de cycles de remplissage et vidage
         
         """
        num_pixels = 60
        self.on_led(0, color_name)
        i = 0
        for j in range(times):
            while i < num_pixels:
                self.on_led(i, color_name)
                i += 1
            i = 59
            while i > 0:
                self.off_led(i)
                i -= 1
        self.off_all_led()
        

    def fill_rainbow(self, shift=0):
        """Attribue une couleur arc-en-ciel à chaque pixel, décalée d'une certaine valeur

         shift: décalage des couleurs de l'arc-en-ciel, sinon le rouge sera à la position 0
         
         """
        num_pixels = 60
        for key in self.colors_list.items():
            color = key[1]
            self.pixels[shift] = color
            shift += 1
            shift = shift % 60
        self.pixels.show()


    def rainbow_cycle(self, times=2, wait=0.01):
        """Fait défiler les couleurs de l'arc-en-ciel sur la bande un certain nombre de fois

         wait: temps d'attente entre chaque décalage de couleur
         times: nombre de cycles de l'arc-en-ciel
         
         """
        num_pixels = 60
        for k in range(times):
            for i in range(num_pixels):
                self.fill_rainbow(shift=i)
                time.sleep(wait)
        self.off_all_led()
    

def main():

    parser = argparse.ArgumentParser(description="Arguments to choose the function to run")
    
    parser.add_argument('-r', '--rainbow', action='store_true', help='Rainbow on the LED tap')
    
    parser.add_argument('-c', '--chariot', action='store_true', help='LEDs are turned on one after another')
    
    parser.add_argument('-l', '--load', action='store_true', help='Fill and empty the tape')

    args = parser.parse_args()

    tape = Neopixel_Tape()

    try:
        if args.rainbow == True:
            while True:
                tape.rainbow_cycle(0.01, 10)

        if args.chariot == True:
            tape.chariot('purple')

        if args.fill == True:
            tape.charge('purple')

    except KeyboardInterrupt:
        print("LED turned off by user. Exiting...")
        tape.pixels.fill((0, 0, 0))
        tape.pixels.show()
        sys.exit(0)


if __name__ == '__main__':
    main()
