from gpiozero import LED, Servo
import time
led = LED(14)
led.on()
time.sleep(5)
led.off()

