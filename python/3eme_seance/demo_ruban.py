import time
import RPi5_Neopixel as np

ruban = np.Neopixel_Tape()

"""Démo de toutes les fonctions élémetantaires du ruban LED"""

ruban.on_all_led('medium_turquoise')
time.sleep(0.9)

ruban.off_all_led()