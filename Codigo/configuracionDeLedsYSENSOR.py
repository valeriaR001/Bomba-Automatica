from gpiozero import LED, DistanceSensor
from time import sleep

LedLleno = LED(9)
LedMedioLleno = LED(10)
LedMedio = LED(22)
LedMedioVacio = LED(27)
LedVacio = LED(17)
sensor = DistanceSensor(echo=24, trigger=23)

while True:
    distancia = sensor.distance * 100
    print ("distancia: ",distancia)
    if(distancia < 4):
        LedLleno.on()
        LedMedioLleno.off()
        LedMedio.off()
        LedMedioVacio.off()
        LedVacio.off()
    elif(distancia < 5.25):
        LedLleno.off()
        LedMedioLleno.on()
        LedMedio.off()
        LedMedioVacio.off()
        LedVacio.off()
    elif(distancia < 7.5):
        LedLleno.off()
        LedMedioLleno.off()
        LedMedio.on()
        LedMedioVacio.off()
        LedVacio.off()
    elif(distancia < 9.75):
        LedLleno.off()
        LedMedioLleno.off()
        LedMedio.off()
        LedMedioVacio.on()
        LedVacio.off()
    else:
        LedLleno.off()
        LedMedioLleno.off()
        LedMedio.off()
        LedMedioVacio.off()
        LedVacio.blink()
        sleep(.2)