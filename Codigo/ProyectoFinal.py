from gpiozero import LED, DistanceSensor, AngularServo
from gpiozero.pins.pigpio import PiGPIOFactory
import RPi.GPIO as GPIO
import time
from time import sleep

factory = PiGPIOFactory()

LedLleno = LED(9)
LedMedioLleno = LED(10)
LedMedio = LED(22)
LedMedioVacio = LED(27)
LedVacio = LED(17)
sensor = DistanceSensor(echo=24, trigger=23)
servo180 = AngularServo(21, min_pulse_width=.5/1000, max_pulse_width=2.3/1000, pin_factory=factory)

FLOW_SENSOR_PIN = 14
GPIO.setmode(GPIO.BCM)
GPIO.setup(FLOW_SENSOR_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

flow_rate = 0.0
total_flow = 0.0
last_pin_state = 0
last_pin_change_time = 0.0
pulses = 0

def pulse_callback(channel):
    global last_pin_state, last_pin_change_time, pulses
    if GPIO.input(FLOW_SENSOR_PIN):
        pulses += 1

GPIO.add_event_detect(FLOW_SENSOR_PIN, GPIO.RISING, callback=pulse_callback)

try:
    while True:
        distancia = sensor.distance * 100
        
        if pulses >= 8:
            servo180.angle = 2.5
        else:
            servo180.angle = -90

        if distancia < 4.25:
            LedLleno.on()
            LedMedioLleno.off()
            LedMedio.off()
            LedMedioVacio.off()
            LedVacio.off()
            servo180.angle = -90
        elif distancia >= 4.25 and distancia < 7:
            LedLleno.off()
            LedMedioLleno.on()
            LedMedio.off()
            LedMedioVacio.off()
            LedVacio.off()
        elif distancia >= 7 and distancia < 9:
            LedLleno.off()
            LedMedioLleno.off()
            LedMedio.on()
            LedMedioVacio.off()
            LedVacio.off()
        elif distancia >= 9 and distancia < 11:
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

        if pulses >= 1:
            flow_rate = pulses / (time.time() - last_pin_change_time)
            last_pin_change_time = time.time()
            total_flow += pulses / 450.0
            print("Flujo: %.2f L/min - Total: %.2f L" % (flow_rate, total_flow))
            pulses = 0

        time.sleep(1)

except KeyboardInterrupt:
    GPIO.cleanup()
