import RPi5_Neopixel as np

ruban = np.Neopixel_Tape()

"""Fait se croiser deux LEDs allumées depuis les deux extrémités de la bande un certain nombre de fois avec le nom de couleur donné
        
    color_name: nom de la couleur à utiliser

"""

num_pixels = 60
ruban.on_led(0, ) # n'oublie pas le nom de la couleur que tu veux utiliser
ruban.on_led(59, )