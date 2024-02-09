from gpiozero import LED, DistanceSensor, AngularServo
from gpiozero.pins.pigpio import PiGPIOFactory
from time import sleep

factory = PiGPIOFactory()

LedLleno = LED(9)
LedMedioLleno = LED(10)
LedMedio = LED(22)
LedMedioVacio = LED(27)
LedVacio = LED(17)
sensor = DistanceSensor(echo=24, trigger=23)
servo180 = AngularServo(21, min_pulse_width=.5/1000, max_pulse_width=2.3/1000, pin_factory=factory)

while True:
    distancia = sensor.distance * 100
    print("distancia:", distancia)
    if distancia < 4.5:
        LedLleno.on()
        LedMedioLleno.off()
        LedMedio.off()
        LedMedioVacio.off()
        LedVacio.off()
        servo180.angle = -90
    elif distancia >= 4.5 and distancia < 6:
        LedLleno.off()
        LedMedioLleno.on()
        LedMedio.off()
        LedMedioVacio.off()
        LedVacio.off()
        servo180.angle = 2.5
    elif distancia >= 6 and distancia < 8:
        LedLleno.off()
        LedMedioLleno.off()
        LedMedio.on()
        LedMedioVacio.off()
        LedVacio.off()
        servo180.angle = 2.5
    elif distancia >= 8 and distancia < 10:
        LedLleno.off()
        LedMedioLleno.off()
        LedMedio.off()
        LedMedioVacio.on()
        LedVacio.off()
        servo180.angle = 2.5
    else:
        LedLleno.off()
        LedMedioLleno.off()
        LedMedio.off()
        LedMedioVacio.off()
        LedVacio.blink()
        sleep(.2)