# Projet Illumine

## Contenu du repository

Le projet est découpé en deux dossiers. Dans le dossier `python` vous trouverez les scripts utilisés lors des différentes séances, et dans le dossier `documentation` vous trouverez le projet Latex pour éditer votre propre TP, ainsi qu'une version pdf.

Toutes les informations qui vont suivre se trouvent aussi dans l'annexe à destination des encadrants à la fin du TP.

## Matériel

- **Raspberry Pi 5** 4 Go BCM2712 2,4 GHz [RS Online](https://fr.rs-online.com/web/p/raspberry-pi/0219253)
- **Carte mémoire** micro-SD A2 class DDR50/SDR104 32GB [Mouser](https://mou.sr/3Km0bGc)
- **Alimentation pour Raspberry Pi** USB type C, 1.2m, fiche femelle européenne [RS Online](https://fr.rs-online.com/web/p/alimentations-raspberry-pi/0219261)
- **Adafruit NeoPixel** Digital RGBW LED Strip, White PCB, 60 LED/m, 1m [Mouser](https://mou.sr/40tlNWa)
- **Female DC Power Adapter** [Mouser](https://mou.sr/3NrRk6Y)
- **Adaptateur AC/DC** 5V c.c., 4A, 24W, C14 [RS Online](https://fr.rs-online.com/web/p/adaptateurs-ac-dc/9048474)
- **Cordon d'alimentation RS PRO** Connecteur CEI C13 CEE 7/7, 1m, 10A / 250V [RS Online](https://fr.rs-online.com/web/p/cordons-d-alimentation/6266751)
- **TXB0104 Bi-Direction Level Shifter** [Mouser](https://mou.sr/4heobXq)
- **HDMI vers micro HDMI** 1m [RS Online](https://fr.rs-online.com/web/p/cables-raspberry-pi/2012171)
- **Platine d'essai** [RS Online](https://fr.rs-online.com/web/p/platines-d-essais/2153175)
- **Strap pour platine d'essai mâle-mâle** [RS Online](https://fr.rs-online.com/web/p/straps-pour-platines-d-essai/2048241)
- **Strap pour platine d'essai mâle-femelle** [RS Online](https://fr.rs-online.com/web/p/straps-pour-platines-d-essai/2048243)

## Configuration du Raspberry Pi 5

**Lien vers l'image de la carte SD du RPi 5 :** [https://drive.proton.me/urls/3HZFCYNRZ4#hk5mEik54Qc6](https://drive.proton.me/urls/3HZFCYNRZ4#hk5mEik54Qc6)

Pour décompresser l'image, utilisez la commande:
`tar -xvzf rpi5-illumine.tar.gz`
Puis voici une référence pour vous aider à la copier sur votre carte SD: [Cloner une carte SD](https://raspberrytips.fr/cloner-carte-sd-raspberry-pi/)

L'environnement virtuel Python `illumine_env` est déjà créé et contient toutes les librairies nécessaires. Voici la liste des librairies spécifiques à installer si vous souhaitez recréer l'environnement :

- `gpiozero`
- `Adafruit-Blinka-Raspberry-Pi5-Neopixel` [Repository Adafruit Blinka](https://github.com/adafruit/Adafruit_Blinka_Raspberry_Pi5_Neopixel)
- `adafruit-circuitpython-pixelbuf`
- `adafruit-circuitpython-led-animation`
- `ipython`

Vous aurez également besoin de librairies plus classiques comme `numpy`, `time`, etc.

## Références

Toutes les explications claires et détaillées sont disponibles sur le merveilleux site d'Adafruit :

- [Présentation des rubans LED NeoPixel](https://learn.adafruit.com/neopixels-on-raspberry-pi)
- [Comment réaliser le montage électronique](https://learn.adafruit.com/neopixels-on-raspberry-pi/raspberry-pi-wiring)
- [Librairies Python à installer et exemple de code](https://learn.adafruit.com/neopixels-on-raspberry-pi/python-usage)
- [Modifications nécessaires pour le Raspberry Pi 5](https://learn.adafruit.com/circuitpython-on-raspberrypi-linux/using-neopixels-on-the-pi-5)
- [Présentation du Level Shifter TXB0104](https://www.adafruit.com/product/1875)

Si vous souhaitez réaliser la première séance avec une LED unique, voici des ressources utiles :

- [Circuit électronique simple](https://raspberry-pi.fr/led-raspberry-pi/)
- [Librairie gpiozero](https://raspberrypi.stackexchange.com/questions/148686/raspberry-pi-5-gpiozero)

 ## Remerciements

 Merci à **Airbus** pour les financements qui ont permis d'acheter le matériel nécessaire.
 Merci à l'**ISAE-SUPAERO** et aux équipes de **OSE** pour leur accompagnement.
 Merci à **Prophesee** de me permettre de réaliser ce genre de projets.

 Merci à [Adafruit](https://www.adafruit.com/) pour tout ce qu'ils proposent.

 Merci à [gza-soro](https://github.com/gza-soro).
