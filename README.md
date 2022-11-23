# CS530-Final-Project
- Project: Laser Alarm Security System
The goal of the project is to create a simple laser security system with a Raspberry Pi.
In addition, we wanted to make sure that it was afforadable AND easily expandable.
Therefore, the raspberry pi was a perfect fit.

To use our final device the user simply has to turn on the raspberry pi and start up the python script. Once the script is active, the laser trip will be effective in detecting any "intruder" across from where it is posted/set up. The laser can be mounted anywhere with any desireable mounting device or tool as long as it maintains level sight to the receiver connected to the pi. Once it is tripped, the device will trigger, setting off the buzzer and sending an alert to the log. It will reset on its own as soon as it once again maintains laser sight.

The GPIO library also provides a simple yet powerful functionality that allows the Pi hardware to interact with other devices, such as buttons, LED lights, etc.

For more information about the GPIOZERO library, here is the link: https://gpiozero.readthedocs.io/en/stable/index.html
