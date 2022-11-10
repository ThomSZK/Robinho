import machine
from machine import Pin
import time
import camera

flash = Pin(4, Pin.OUT)
for i in range(3):
    flash.value(1)
    time.sleep(0.1)
    flash.value(0)
    time.sleep(0.1)
    print("desligou")
    
#camera.init(10)
#camera.quality(12)
#camera.framesize(9) 