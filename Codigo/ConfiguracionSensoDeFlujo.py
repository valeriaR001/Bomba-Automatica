import RPi.GPIO as GPIO
import time

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
        if pulses >= 1:
            flow_rate = pulses / (time.time() - last_pin_change_time)
            last_pin_change_time = time.time()
            total_flow += pulses / 450.0
            print("Flujo: %.2f L/min - Total: %.2f L" % (flow_rate, total_flow))
            pulses = 0

        time.sleep(1)

except KeyboardInterrupt:
    GPIO.cleanup() 