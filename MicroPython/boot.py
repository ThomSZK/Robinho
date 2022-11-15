# This file is executed on every boot (including wake-boot from deepsleep)
#import esp
#esp.osdebug(None)
import webrepl
import network
import machine 
from machine import Pin
import time 
import camera 

webrepl.start()
sta_if = network.WLAN(network.STA_IF); sta_if.active(True)
sta_if.connect("It hurts when IP 2.4","SzK$45%63@")
#uart = machine.UART(1, 9600 , rx=12, tx=13)
#uart.init(9600, bits=8, parity=None, stop=1)


