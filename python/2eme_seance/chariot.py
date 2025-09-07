import RPi5_Neopixel as np

ruban = np.Neopixel_Tape()

"""Déplace une LED allumée d'avant en arrière sur la bande un certain nombre de fois avec le nom de couleur donné
        
    color_name: nom de la couleur à utiliser
         
"""

num_pixels = 60
ruban.on_led(0, ) # n'oublie pas le nom de la couleur que tu veux utiliser

