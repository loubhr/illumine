import time
import RPi5_Neopixel as np

ruban = np.Neopixel_Tape()

"""Démo de toutes les fonctions élémentaires du ruban LED"""

ruban.on_all_led('medium_turquoise')

time.sleep(0.9)

ruban.croise('rosy_brown', 2)

ruban.charge('dark_green')

ruban.clignote_all('blue_violet')

ruban.on_all_led('teal')

time.sleep(0.1)

ruban.on_led(25, 'rust')
time.sleep(0.05)

ruban.on_led(36, 'lemon_yellow')
time.sleep(0.05)

ruban.on_led(47, 'coral')
time.sleep(0.05)

ruban.random('thistle_purple', 40)

ruban.rainbow_cycle(5)
