from gpiozero import LED
from time import sleep

rouge = LED(16)

n = 10

for i in range(n):
	rouge.on()
	sleep(0.5)
	rouge.off()
	sleep(0.5)

