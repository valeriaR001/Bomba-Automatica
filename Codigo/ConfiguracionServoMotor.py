from gpiozero import AngularServo
from time import sleep
from gpiozero.pins.pigpio import PiGPIOFactory

factory = PiGPIOFactory()

servo180 = AngularServo(21, min_pulse_width=.5/1000, max_pulse_width=2.3/1000, pin_factory=factory)


for i in range(-90, 0, 50):
    print(i)
    servo180.angle = i
    sleep(1)
servo180.angle = 2.5 