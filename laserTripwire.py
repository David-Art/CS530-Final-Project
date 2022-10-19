from gpiozero import LightSensor, Buzzer #Import the lightsensor and buzzer functionality from the gpiozero library.
from time import sleep #Import the time library to allow timing commands.

# LDR (the pin #, the queue used to store values read from the circuit, and the charge limit)
ldr = LightSensor(4, 5, 0.2) # Le LightSensor. ldr is the variable call for the LightSensor.
buzzer = Buzzer(17) # Le Buzzer. buzzer is the variable call for the Buzzer.

while True:
	sleep(0.1)
	if ldr.value < 0.5:
		buzzer.on()
	else:
		buzzer.off()
